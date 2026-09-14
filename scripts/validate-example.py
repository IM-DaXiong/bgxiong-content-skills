# -*- coding: utf-8 -*-
"""Minimal Content Skill example validator (offline)."""
from __future__ import annotations
import json, sys
from pathlib import Path

CLOSED = {
    "content.plan",
    "generation.policy",
    "optimize.storyboard_shot",
    "optimize.segment",
}

def die(msg: str) -> None:
    print("FAIL:", msg, file=sys.stderr)
    sys.exit(1)

def main(argv: list[str]) -> None:
    if len(argv) < 2:
        die("usage: validate-example.py <pack-dir> [<pack-dir>...]")
    root = Path(__file__).resolve().parents[1]
    caps_pin = root / "contracts" / "v1" / "content-skill-capabilities.json"
    if caps_pin.is_file():
        try:
            pin = json.loads(caps_pin.read_text(encoding="utf-8"))
            # tolerate several shapes
            if isinstance(pin, dict):
                for key in ("capabilities", "enum", "values"):
                    if key in pin and isinstance(pin[key], list):
                        closed = set(pin[key])
                        break
                else:
                    closed = CLOSED
            else:
                closed = CLOSED
        except Exception:
            closed = CLOSED
    else:
        closed = CLOSED

    for arg in argv[1:]:
        d = Path(arg)
        if not d.is_dir():
            die(f"not a dir: {d}")
        man = d / "skill.manifest.json"
        if not man.is_file():
            die(f"missing skill.manifest.json in {d}")
        m = json.loads(man.read_text(encoding="utf-8"))
        caps = set(m.get("capabilities") or [])
        if not caps:
            die(f"{d}: empty capabilities")
        if not caps.issubset(closed):
            die(f"{d}: capabilities not in closed set: {caps - closed}")
        if not str(m.get("id", "")).startswith("local."):
            die(f"{d}: id must start with local.")
        readme = d / "README.md"
        if not readme.is_file():
            die(f"{d}: missing README.md")
        if "content.plan" in caps and not (d / "pipeline.json").is_file():
            die(f"{d}: content.plan requires pipeline.json")
        if "generation.policy" in caps and not (d / "generation-policy.json").is_file():
            die(f"{d}: generation.policy requires generation-policy.json")
        if "optimize.storyboard_shot" in caps:
            op = d / "optimize-storyboard-shot.json"
            if not op.is_file():
                die(f"{d}: missing optimize-storyboard-shot.json")
            o = json.loads(op.read_text(encoding="utf-8"))
            if not o.get("outputSchema"):
                die(f"{d}: optimize-storyboard-shot outputSchema empty")
        if "optimize.segment" in caps:
            op = d / "optimize-segment.json"
            if not op.is_file():
                die(f"{d}: missing optimize-segment.json")
            o = json.loads(op.read_text(encoding="utf-8"))
            if not o.get("outputSchema"):
                die(f"{d}: optimize-segment outputSchema empty")
        print("OK", d)

if __name__ == "__main__":
    main(sys.argv)
