# -*- coding: utf-8 -*-
"""Shared readers for standard Agent Skill packages. Not a host runtime."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST_ROOT = ROOT.parent / "bgxiong-ai-story"
DOMAIN = b"bgx-agent-skill-digest-v1\n"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
FRONT_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n(.*)\Z", re.S)

BLOCKED_PACKAGES = {"h3-prompt-writing"}
CURRENT_WORKFLOW = "clips-v1"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def package_digest(files: dict[str, bytes]) -> str:
    lines = []
    for rel in sorted(files, key=lambda item: item.encode("utf-8")):
        digest = sha256_bytes(files[rel])
        lines.append(f"{digest}  {rel}\n")
    body = DOMAIN + "".join(lines).encode("utf-8")
    return "sha256:" + sha256_bytes(body)


def iter_package_files(package: Path) -> dict[str, bytes]:
    files: dict[str, bytes] = {}
    for path in package.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(package).as_posix()
        if rel.startswith(".git/") or "/.git/" in rel:
            continue
        files[rel] = path.read_bytes()
    return files


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = FRONT_RE.match(text)
    if not match:
        raise ValueError("SKILL.md is missing opening frontmatter")
    raw, body = match.group(1), match.group(2)
    data: dict[str, str] = {}
    section = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith(" ") or line.startswith("\t"):
            if section != "metadata":
                raise ValueError("unexpected indented frontmatter")
            key, value = line.strip().split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
            continue
        if ":" not in line:
            raise ValueError(f"frontmatter line is not key: value: {line}")
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key == "metadata" and value == "":
            section = "metadata"
            continue
        section = None
        data[key] = value
    return data, body


def load_skill(package: Path) -> tuple[dict[str, str], str, dict[str, bytes]]:
    skill = package / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    return meta, body, iter_package_files(package)


def load_hosts() -> tuple[list[str], list[str]]:
    path = ROOT / "contracts" / "snapshots" / "agent-skill-hosts" / "agent-skill-hosts.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    return list(payload["currentAuthoringHosts"]), list(payload["hosts"])


def host_tokens(meta: dict[str, str]) -> list[str]:
    raw = meta.get("bgx-hosts", "")
    return [part for part in raw.split() if part]


def safe_rel(path: str) -> bool:
    parts = path.replace("\\", "/").split("/")
    if path.startswith("/") or re.match(r"^[A-Za-z]:", path):
        return False
    return ".." not in parts and all(part not in {"", ".", ".."} for part in parts)
