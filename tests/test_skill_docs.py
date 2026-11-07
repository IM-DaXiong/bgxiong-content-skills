# -*- coding: utf-8 -*-
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from skill_lib import ROOT


class CoverageTests(unittest.TestCase):
    def test_catalog_pages_exist(self):
        catalog = json.loads((ROOT / "catalog" / "packages.json").read_text(encoding="utf-8"))
        self.assertGreater(len(catalog["packages"]), 0)
        for item in catalog["packages"]:
            self.assertTrue((ROOT / "docs" / "skills" / f"{item['name']}.zh-CN.md").is_file())
            desc = json.loads((ROOT / "catalog" / "descriptions" / f"{item['name']}.zh-CN.json").read_text(encoding="utf-8"))
            self.assertNotEqual(desc["observedEvidence"]["status"], "measured")
            self.assertIsNone(desc["download"])


if __name__ == "__main__":
    unittest.main()
