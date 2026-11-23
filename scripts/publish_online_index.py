#!/usr/bin/env python3
"""Build and sign a reviewable official Skill directory from the content catalog."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey

from build_packages import build_one
from online_index_signer import CHANNEL, b64, sign, sign_file, verify
from skill_lib import ROOT, NAME_RE, SEMVER_RE, host_tokens, load_skill, package_digest
from validate_skill import check_package

MAX_ZIP = 256 << 20


def canonical(data: object) -> bytes:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sign_remotely(payload: bytes, host: str, key_id: str, expected_public: str) -> tuple[dict, str]:
    if not re.fullmatch(r"[a-zA-Z0-9_]+@[a-zA-Z0-9][a-zA-Z0-9.-]*", host):
        raise ValueError("Enter the SSH signer as user@host")
    signer = Path(__file__).with_name("online_index_signer.py").read_bytes()
    command = f"\nsign_on_host({b64(payload)!r}, {key_id!r})\n".encode("ascii")
    reply = subprocess.check_output(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", host, "python3", "-"],
                                    input=signer + command, timeout=60)
    envelope, public = json.loads(reply)
    if public != expected_public or verify(envelope, key_id, public) != payload:
        raise ValueError("Signing host response differs from the requested payload or configured trust")
    return envelope, public


def version_key(value: str) -> tuple[int, ...]:
    if not SEMVER_RE.fullmatch(value):
        raise ValueError(f"Invalid release version: {value}")
    parts = tuple(map(int, value.split(".")))
    if any(part >= 2**64 for part in parts):
        raise ValueError(f"Invalid release version: {value}")
    return parts


def source_rows(document: dict) -> dict:
    indexed = {}
    for row in document["packages"]:
        if row.get("distribution") != "source-approved":
            continue
        if not NAME_RE.fullmatch(row["name"]) or not row.get("rights"):
            raise ValueError("Approved release requires identity and rights")
        version_key(row["version"])
        fingerprint = row["packageDigest"]
        if len(fingerprint) != 71 or not fingerprint.startswith("sha256:") or any(c not in "0123456789abcdef" for c in fingerprint[7:]):
            raise ValueError(f"Invalid Skill source digest: {row['name']}")
        if row["name"] in indexed:
            raise ValueError(f"Duplicate approved Skill: {row['name']}")
        indexed[row["name"]] = row
    return indexed


def older_sources(row: dict, history: list[dict]) -> list[dict]:
    sources = {}
    version = version_key(row["version"])
    for inventory in history:
        prior = inventory.get(row["name"])
        if prior is None:
            continue
        previous = version_key(prior["version"])
        if previous > version or (previous == version and prior["packageDigest"] != row["packageDigest"]):
            raise ValueError(f"Version rollback or replacement: {row['name']}")
        if previous < version:
            previous_digest = sources.setdefault(prior["version"], prior["packageDigest"])
            if previous_digest != prior["packageDigest"]:
                raise ValueError(f"Conflicting prior version: {row['name']}")
    return [{"version": v, "sourceSha256": sources[v][7:]} for v in sorted(sources, key=version_key)]


def build(args: argparse.Namespace) -> None:
    inventory = source_rows(json.loads((ROOT / "catalog/packages.json").read_bytes()))
    prior_catalogs = [
        source_rows(json.loads(subprocess.check_output(
            ["git", "show", f"{revision}:catalog/packages.json"], cwd=ROOT,
        ))) for revision in args.prior_commit
    ]
    names = sorted(set(args.package or inventory))
    if not names:
        raise ValueError("No approved Skills selected")
    for name in names:
        row = inventory[name]
        src = (ROOT / row["path"]).resolve()
        if not src.is_relative_to(ROOT / "skills") or src.name != name:
            raise ValueError(f"Invalid catalog source path: {name}")
        report = check_package(src, "publish")
        if report.failed("publish"):
            raise ValueError(f"Skill failed publication checks: {name}: {report.findings}")
        meta, _, files = load_skill(src)
        if (meta["version"] != row["version"] or host_tokens(meta) != row["hosts"]
                or meta["bgx-workflow"] != row["workflow"] or package_digest(files) != row["packageDigest"]):
            raise ValueError(f"Skill bytes or host contract differ from catalog: {name}")
        older_sources(row, prior_catalogs)
    private_key_path = None if args.test else os.environ.get("BGX_CONTENT_SKILL_INDEX_KEY_FILE")
    if not args.test and (not (private_key_path or args.signing_host) or not args.key_id or args.key_id.endswith("-test")):
        raise ValueError("Production requires a dedicated key file and key ID")

    output = args.output.resolve()
    if output.is_relative_to(ROOT / "skills"):
        raise ValueError("Output cannot be inside Skill sources")
    output.mkdir(parents=True)
    packages = []
    for name in names:
        row = inventory[name]
        src = (ROOT / row["path"]).resolve()
        meta, _, _ = load_skill(src)
        filename = f"{name}-{row['version']}.zip"
        package = build_one(src, output / filename)
        if package["packageDigest"] != row["packageDigest"] or not 0 < package["size"] <= MAX_ZIP:
            raise ValueError(f"Built ZIP differs from the approved source: {name}")
        packages.append({
            "packageId": name, "version": row["version"], "displayName": meta.get("bgx-display-name", name),
            "newInstall": True, "hostVersionRange": args.host_version_range,
            "upgradeFrom": older_sources(row, prior_catalogs),
            "file": filename, "bytes": package["size"], "sha256": package["sha256"],
            "sourceSha256": row["packageDigest"][7:],
        })
    payload = {
        "schemaVersion": 1, "channel": CHANNEL, "sequence": args.sequence,
        "publishedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "packages": packages,
    }
    payload_bytes = canonical(payload)
    if args.test:
        envelope, public = sign(payload_bytes, Ed25519PrivateKey.generate(), "content-skill-catalog-test")
    elif args.signing_host:
        envelope, public = sign_remotely(payload_bytes, args.signing_host, args.key_id, args.public_trust)
    else:
        envelope, public = sign_file(payload_bytes, args.key_id, private_key_path)
    (output / "latest.json").write_bytes(canonical(envelope))
    (output / "public-trust.txt").write_text(public + "\n", encoding="ascii")


def main() -> None:
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--output", type=Path, default=Path("L:/00Dev/bgxiong-00-release/cdn-bgxiong-content-skills"))
    cli.add_argument("--sequence", type=int, required=True)
    cli.add_argument("--package", action="append")
    cli.add_argument("--prior-commit", action="append", default=[])
    cli.add_argument("--host-version-range", required=True)
    cli.add_argument("--test", action="store_true")
    cli.add_argument("--key-id")
    cli.add_argument("--signing-host", help="SSH user@host holding the dedicated Skill key")
    cli.add_argument("--public-trust", help="Expected base64 Minisign public key text")
    args = cli.parse_args()
    if not 0 < args.sequence < 2**53 or not args.host_version_range.strip():
        cli.error("A positive safe sequence and a host version range are required")
    if args.signing_host and (args.test or not args.public_trust or not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", args.key_id or "")):
        cli.error("Remote signing requires a production key ID and its pinned public trust")
    build(args)


if __name__ == "__main__":
    main()
