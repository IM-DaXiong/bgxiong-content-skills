# -*- coding: utf-8 -*-
"""Copy host skill bytes into this repo without changing package files."""
from __future__ import annotations

import json
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_lib import HOST_ROOT, ROOT, package_digest, sha256_file, load_skill, publication_blocked

BUILTIN = HOST_ROOT / "src-tauri" / "resources" / "builtin-agent-skills"
FIXTURES = HOST_ROOT / "fixtures" / "agent-skills"


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def digest_of(path: Path) -> str:
    files = {}
    for file in path.rglob("*"):
        if file.is_file():
            files[file.relative_to(path).as_posix()] = file.read_bytes()
    return package_digest(files)


def main() -> int:
    if not BUILTIN.is_dir() or not FIXTURES.is_dir():
        print("host skill directories missing", HOST_ROOT, file=sys.stderr)
        return 2
    skills = ROOT / "skills"
    examples = ROOT / "examples" / "teaching"
    skills.mkdir(parents=True, exist_ok=True)
    examples.mkdir(parents=True, exist_ok=True)
    inventory = []
    builtin_dirs = [p for p in BUILTIN.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()]
    fixture_dirs = [p for p in FIXTURES.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()]
    for src in sorted(builtin_dirs, key=lambda p: p.name):
        record = {
            "name": src.name,
            "kind": "builtin",
            "sourcePath": str(src.relative_to(HOST_ROOT)).replace("\\", "/"),
            "sourceDigest": digest_of(src),
            "blocked": publication_blocked(load_skill(src)[0]),
        }
        if publication_blocked(load_skill(src)[0]):
            record["disposition"] = "blocked_pending_legal"
            record["copiedTo"] = None
        else:
            dst = skills / src.name
            copy_tree(src, dst)
            record["disposition"] = "source-retained"
            record["copiedTo"] = str(dst.relative_to(ROOT)).replace("\\", "/")
            record["copiedDigest"] = digest_of(dst)
        inventory.append(record)
    skill_digest = {item["name"]: item.get("copiedDigest") for item in inventory}
    for src in sorted(fixture_dirs, key=lambda p: p.name):
        digest = digest_of(src)
        same = skill_digest.get(src.name)
        record = {
            "name": src.name,
            "kind": "fixture",
            "sourcePath": str(src.relative_to(HOST_ROOT)).replace("\\", "/"),
            "sourceDigest": digest,
            "blocked": False,
        }
        if same and same == digest:
            record["disposition"] = "same-bytes-as-builtin"
            record["copiedTo"] = None
            record["derivesFrom"] = f"skills/{src.name}"
        else:
            dst = examples / src.name
            copy_tree(src, dst)
            record["disposition"] = "teaching-variant" if src.name in skill_digest else "teaching-or-fixture"
            record["copiedTo"] = str(dst.relative_to(ROOT)).replace("\\", "/")
            record["copiedDigest"] = digest_of(dst)
            if src.name in skill_digest:
                record["derivesFrom"] = f"skills/{src.name}"
        inventory.append(record)
    out = ROOT / "docs" / "maintenance" / "import-inventory.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps(
            {
                "importedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                "hostRootName": HOST_ROOT.name,
                "packages": inventory,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"imported {len(inventory)} records -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
