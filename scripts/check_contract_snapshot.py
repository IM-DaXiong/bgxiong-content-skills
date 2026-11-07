# -*- coding: utf-8 -*-
"""Check contract snapshot bytes against the recorded source hash."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from skill_lib import ROOT


def main() -> int:
    base = ROOT / "contracts" / "snapshots"
    failed = False
    for source in base.glob("*/source.json"):
        meta = json.loads(source.read_text(encoding="utf-8"))
        for item in meta["files"]:
            path = source.parent / item["name"]
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            if digest != item["sha256"]:
                print("snapshot mismatch", path, file=sys.stderr)
                failed = True
    if failed:
        return 1
    print("contract snapshots ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
