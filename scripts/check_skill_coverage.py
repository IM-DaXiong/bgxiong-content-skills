# -*- coding: utf-8 -*-
"""Fail when an approved package has no explanation page."""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_lib import ROOT


def main() -> int:
    catalog = json.loads((ROOT / "catalog" / "packages.json").read_text(encoding="utf-8"))
    missing = []
    for item in catalog["packages"]:
        page = ROOT / "docs" / "skills" / f"{item['name']}.zh-CN.md"
        desc = ROOT / "catalog" / "descriptions" / f"{item['name']}.zh-CN.json"
        if not page.is_file() or not desc.is_file():
            missing.append(item["name"])
        data = json.loads(desc.read_text(encoding="utf-8")) if desc.is_file() else {}
        if data.get("download"):
            missing.append(item["name"] + ":download")
    blocked = ROOT / "catalog" / "descriptions" / "h3-prompt-writing.zh-CN.json"
    if blocked.is_file():
        data = json.loads(blocked.read_text(encoding="utf-8"))
        if data.get("distribution") != "blocked" or data.get("download"):
            missing.append("h3-status")
    else:
        missing.append("h3-missing")
    if missing:
        print("coverage failed", missing, file=sys.stderr)
        return 1
    print("coverage ok", len(catalog["packages"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
