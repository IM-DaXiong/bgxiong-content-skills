#!/usr/bin/env python3
"""Publish a signed official Skill release from the CDN origin and verify public downloads."""

import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import quote
from urllib.request import Request, urlopen

from online_index_signer import CHANNEL, verify

KEY_ID = "content-skill-catalog-20261119"
DEFAULT_ROOT = Path("/var/www/r.bgxiong.com/client/ai-story/bgxiong-content-skills")
DEFAULT_BASE = "https://r.bgxiong.com/client/ai-story/bgxiong-content-skills/"
INDEX_LIMIT = 1 << 20
ZIP_LIMIT = 256 << 20


def read_index(path, trust):
    with path.open("rb") as source:
        envelope = source.read(INDEX_LIMIT + 1)
    if len(envelope) > INDEX_LIMIT:
        raise ValueError("Skill index exceeds byte limit")
    catalog = json.loads(verify(json.loads(envelope), KEY_ID, trust).decode("utf-8"))
    sequence = catalog.get("sequence")
    if catalog.get("channel") != CHANNEL or catalog.get("schemaVersion") != 1 or type(sequence) is not int or not 0 < sequence < 2**53:
        raise ValueError("Invalid official Skill index")
    return envelope, catalog


def fingerprint(source, limit):
    digest = hashlib.sha256()
    total = 0
    while True:
        chunk = source.read(1 << 20)
        if not chunk:
            return total, digest.hexdigest()
        total += len(chunk)
        if total > limit:
            raise ValueError("Object exceeds its signed size")
        digest.update(chunk)


def verify_file(path, expected):
    with path.open("rb") as source:
        if fingerprint(source, expected[0]) != expected:
            raise ValueError("File bytes differ from the signed release: " + path.name)


def verify_public(base, name, expected, sequence):
    url = base.rstrip("/") + "/" + quote(name) + "?catalogSequence=" + str(sequence)
    req = Request(url, headers={"Accept-Encoding": "identity", "Cache-Control": "no-cache"})
    with urlopen(req, timeout=30) as response:
        if response.status != 200 or response.geturl() != url or fingerprint(response, expected[0]) != expected:
            raise ValueError("Public download differs from the signed release: " + name)


def install_file(source_path, target, replace=False):
    with tempfile.NamedTemporaryFile(dir=str(target.parent), prefix=".skill-release-", delete=False) as writable:
        stage = Path(writable.name)
        try:
            with source_path.open("rb") as source:
                shutil.copyfileobj(source, writable)
            writable.flush()
            os.fsync(writable.fileno())
            stage.chmod(0o644)
            if replace:
                os.replace(str(stage), str(target))
            else:
                os.link(str(stage), str(target))
        finally:
            if stage.exists():
                stage.unlink()


def publish(staging, root, base, trust):
    index_bytes, catalog = read_index(staging / "latest.json", trust)
    sequence = catalog["sequence"]
    index_fingerprint = len(index_bytes), hashlib.sha256(index_bytes).hexdigest()
    archives = {}
    for entry in catalog["packages"]:
        name = entry["file"]
        size = entry["bytes"]
        digest = entry["sha256"]
        if (not re.fullmatch(r"[a-z0-9][a-z0-9._-]{1,180}\.zip", name) or name in archives
                or type(size) is not int or not 0 < size <= ZIP_LIMIT or not re.fullmatch(r"[0-9a-f]{64}", digest)):
            raise ValueError("Invalid Skill ZIP identity in the signed release")
        archives[name] = size, digest
        verify_file(staging / name, archives[name])
    if not archives:
        raise ValueError("No signed Skill packages")

    root.mkdir(mode=0o755, parents=True, exist_ok=True)
    with (root.parent / ("." + root.name + ".lock")).open("ab") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        current_path = root / "latest.json"
        if current_path.exists():
            current_bytes, current = read_index(current_path, trust)
            if current["sequence"] > sequence or (current["sequence"] == sequence and current_bytes != index_bytes):
                raise ValueError("Skill index sequence rollback or reuse")
        for name, expected in archives.items():
            target = root / name
            if not target.exists():
                install_file(staging / name, target)
            verify_file(target, expected)
            verify_public(base, name, expected, sequence)
        if not current_path.exists() or current_path.read_bytes() != index_bytes:
            install_file(staging / "latest.json", current_path, replace=True)
        verify_public(base, "latest.json", index_fingerprint, sequence)

    print(json.dumps({"sequence": sequence, "indexSha256": index_fingerprint[1],
                      "packages": len(archives), "zipBytes": sum(size for size, _ in archives.values())}))


if __name__ == "__main__":
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("staging", type=Path)
    cli.add_argument("--public-trust", required=True)
    cli.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    cli.add_argument("--public-base", default=DEFAULT_BASE)
    args = cli.parse_args()
    publish(args.staging.resolve(), args.root.resolve(), args.public_base, args.public_trust)
