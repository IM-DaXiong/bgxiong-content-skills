# -*- coding: utf-8 -*-
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from skill_lib import package_digest
from validate_skill import check_package

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT.parent / "bgxiong-ai-story" / "packages" / "app-contracts" / "v1" / "agent-skills.json"


class DigestTests(unittest.TestCase):
    def test_golden_vectors(self):
        data = json.loads(CONTRACT.read_text(encoding="utf-8"))
        for vector in data["packageDigest"]["goldenVectors"]:
            files = {item["path"]: item["utf8"].encode("utf-8") for item in vector["files"]}
            self.assertEqual(package_digest(files), vector["digest"])


class ValidateTests(unittest.TestCase):
    def write_package(self, folder: Path, body: str) -> None:
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(body, encoding="utf-8")

    def test_format_rejects_bad_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "Bad Name"
            self.write_package(
                package,
                "---\nname: Bad Name\ndescription: x\n---\n\n# T\n",
            )
            report = check_package(package, "format")
            self.assertTrue(report.failed("format"))

    def test_author_current_rejects_old_workflow(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "old-flow"
            self.write_package(
                package,
                "---\nname: old-flow\ndescription: old\nmetadata:\n  bgx-workflow: legacy-v0\n  bgx-hosts: multi-view\n---\n\n# T\n",
            )
            report = check_package(package, "author-current")
            self.assertTrue(any(code == "AUTHOR_WORKFLOW" for _, code, _ in report.findings))

    def test_publish_rejects_blocked_name_when_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            package = Path(tmp) / "h3-prompt-writing"
            self.write_package(
                package,
                "---\nname: h3-prompt-writing\ndescription: blocked\nmetadata:\n  version: \"1.0.0\"\n  bgx-workflow: clips-v1\n  bgx-hosts: video-prompt-projection\n---\n\n# T\n",
            )
            report = check_package(package, "publish")
            self.assertTrue(any(code == "PUBLISH_BLOCKED" for _, code, _ in report.findings))


if __name__ == "__main__":
    unittest.main()
