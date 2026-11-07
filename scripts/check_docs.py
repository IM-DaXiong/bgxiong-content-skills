# -*- coding: utf-8 -*-
"""Local relative-link check for authored docs."""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_lib import ROOT

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def main() -> int:
    failed = False
    for path in (ROOT / "docs").rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for link in LINK.findall(text):
            if link.startswith(("http://", "https://", "mailto:")):
                continue
            target = (path.parent / link.split("#", 1)[0]).resolve()
            if not target.exists():
                print("missing", path, link, file=sys.stderr)
                failed = True
    if failed:
        return 1
    print("docs links ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
