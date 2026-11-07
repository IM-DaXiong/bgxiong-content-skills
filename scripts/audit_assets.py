# -*- coding: utf-8 -*-
"""Inventory and legacy-release checks using the standard library."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_lib import ROOT


def main(argv: list[str]) -> int:
    if "--inventory" in argv:
        rows = []
        for path in sorted(ROOT.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith(("dist/", ".git/")) or "/__pycache__/" in rel:
                continue
            rows.append({"path": rel, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        out = ROOT / "docs" / "maintenance" / "ASSET-INVENTORY.json"
        out.write_text(json.dumps(rows, indent=2) + "\n", encoding="utf-8")
        print(f"inventory {len(rows)}")
    if "--release-no-legacy" in argv:
        catalog = json.loads((ROOT / "catalog" / "packages.json").read_text(encoding="utf-8"))
        for item in catalog["packages"]:
            skill = (ROOT / item["path"] / "SKILL.md").read_text(encoding="utf-8")
            if "skill.manifest.json" in skill or "local." in skill:
                print("legacy contract in release package", item["path"], file=sys.stderr)
                return 1
        print("release catalog has no legacy manifest requirement")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
