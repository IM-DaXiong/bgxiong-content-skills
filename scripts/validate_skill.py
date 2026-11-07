# -*- coding: utf-8 -*-
"""Validate a standard SKILL.md package. Profiles: format, author-current, publish."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from skill_lib import (
    BLOCKED_PACKAGES,
    CURRENT_WORKFLOW,
    NAME_RE,
    SEMVER_RE,
    ROOT,
    host_tokens,
    load_hosts,
    load_skill,
    safe_rel,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))


class Report:
    def __init__(self) -> None:
        self.findings: list[tuple[str, str, str]] = []

    def add(self, level: str, code: str, message: str) -> None:
        self.findings.append((level, code, message))

    def failed(self, profile: str) -> bool:
        if profile == "format":
            return any(level == "error" and code.startswith("FORMAT_") for level, code, _ in self.findings)
        if profile == "author-current":
            return any(level == "error" for level, code, _ in self.findings if not code.startswith("PUBLISH_"))
        return any(level == "error" for _, _, _ in self.findings)


def check_package(package: Path, profile: str) -> Report:
    report = Report()
    skill_path = package / "SKILL.md"
    if not skill_path.is_file():
        report.add("error", "FORMAT_MISSING_SKILL", f"{package}: missing SKILL.md")
        return report
    try:
        meta, _body, files = load_skill(package)
    except Exception as exc:
        report.add("error", "FORMAT_FRONTMATTER", f"{package}: {exc}")
        return report
    name = meta.get("name", "")
    if not NAME_RE.match(name) or len(name) > 64:
        report.add("error", "FORMAT_NAME", f"{package}: name must be lowercase hyphenated, <=64")
    if name != package.name:
        report.add("error", "FORMAT_NAME_DIR", f"{package}: name {name} does not match directory")
    description = meta.get("description", "")
    if not description or len(description) > 1024:
        report.add("error", "FORMAT_DESCRIPTION", f"{package}: description required and <=1024")
    for rel in files:
        if not safe_rel(rel):
            report.add("error", "FORMAT_PATH", f"{package}: unsafe path {rel}")
    layout_rel = "references/layout.json"
    if layout_rel in files:
        try:
            layout = json.loads(files[layout_rel].decode("utf-8"))
        except Exception as exc:
            report.add("error", "FORMAT_LAYOUT", f"{package}: layout.json {exc}")
            layout = None
        if isinstance(layout, dict):
            views = layout.get("views")
            if views is not None and not isinstance(views, dict):
                report.add("error", "FORMAT_LAYOUT", f"{package}: views must be an object")
            anchor = layout.get("identityAnchor")
            if isinstance(views, dict) and anchor:
                for mode, slots in views.items():
                    if isinstance(slots, list) and slots and slots[0] != anchor:
                        report.add(
                            "error",
                            "FORMAT_LAYOUT",
                            f"{package}: {mode} must list identityAnchor first",
                        )
    if profile == "format":
        return report
    current, historical = load_hosts()
    tokens = host_tokens(meta)
    if not tokens:
        report.add("error", "AUTHOR_HOSTS_EMPTY", f"{package}: bgx-hosts is empty")
    unknown = [token for token in tokens if token not in historical]
    if unknown:
        report.add("error", "AUTHOR_HOSTS_UNKNOWN", f"{package}: unknown hosts {unknown}")
    stale = [token for token in tokens if token not in current]
    if stale:
        report.add(
            "error" if profile == "author-current" else "warning",
            "AUTHOR_HOSTS_NOT_CURRENT",
            f"{package}: hosts not in currentAuthoringHosts {stale}",
        )
    workflow = meta.get("bgx-workflow", "")
    if workflow != CURRENT_WORKFLOW:
        report.add(
            "warning" if profile == "format" else "error",
            "AUTHOR_WORKFLOW",
            f"{package}: current execution requires bgx-workflow {CURRENT_WORKFLOW}; import may still be readable",
        )
    if profile != "publish":
        return report
    version = meta.get("version", "")
    if not SEMVER_RE.match(version):
        report.add("error", "PUBLISH_VERSION", f"{package}: publish requires MAJOR.MINOR.PATCH")
    if name in BLOCKED_PACKAGES:
        report.add("error", "PUBLISH_BLOCKED", f"{package}: blocked_pending_legal")
    rights = ROOT / "docs" / "maintenance" / "SOURCES-AND-RIGHTS.md"
    if not rights.is_file():
        report.add("error", "PUBLISH_RIGHTS", f"{package}: missing rights record")
    return report


def packages_under(root: Path) -> list[Path]:
    found = []
    if (root / "SKILL.md").is_file():
        return [root]
    for path in sorted(root.rglob("SKILL.md")):
        found.append(path.parent)
    return found


def main(argv: list[str]) -> int:
    profile = "author-current"
    args = argv[1:]
    if "--profile" in args:
        index = args.index("--profile")
        profile = args[index + 1]
        del args[index : index + 2]
    if "--all" in args:
        args.remove("--all")
    if not args:
        print("usage: validate_skill.py <package-or-root> [--all] [--profile format|author-current|publish]", file=sys.stderr)
        return 2
    if profile not in {"format", "author-current", "publish"}:
        print("unknown profile", file=sys.stderr)
        return 2
    failed = False
    for arg in args:
        root = Path(arg)
        if not root.is_absolute():
            root = ROOT / root
        targets = [root] if (root / "SKILL.md").is_file() else packages_under(root)
        if not targets:
            print(f"FAIL no SKILL.md under {root}", file=sys.stderr)
            failed = True
            continue
        for package in targets:
            report = check_package(package, profile)
            if report.failed(profile):
                failed = True
                for level, code, message in report.findings:
                    if level == "error" or (profile != "format" and level == "warning" and code == "AUTHOR_WORKFLOW"):
                        print(f"{level.upper()} {code} {message}")
            else:
                print(f"OK {package.relative_to(ROOT) if package.is_relative_to(ROOT) else package} {profile}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main(sys.argv))
