from pathlib import Path
import json
import unittest


ROOT = Path(__file__).resolve().parents[1]


class DetailPageContractTest(unittest.TestCase):
    def setUp(self):
        self.records = json.loads(
            (ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8")
        )

    def test_every_record_has_detail_page_baseline_fields(self):
        for item in self.records:
            with self.subTest(id=item.get("id")):
                for field in ("summary", "measurement_strength", "scale", "coverage_gap"):
                    self.assertIsInstance(item.get(field), str)
                    self.assertTrue(item[field].strip())
                for field in ("environment", "protocol", "confounders"):
                    self.assertIsInstance(item.get(field), list)
                    self.assertTrue(item[field])
                self.assertTrue(
                    any(
                        isinstance(url, str) and url.startswith("https://")
                        for url in (item.get("artifacts") or {}).values()
                    )
                )

    def test_existing_deep_notes_are_bilingual_pairs(self):
        notes = ROOT / "benchmarks"
        for path in notes.glob("*.md"):
            if path.name.endswith(".en.md"):
                counterpart = notes / path.name.replace(".en.md", ".md")
            else:
                counterpart = notes / path.name.replace(".md", ".en.md")
            with self.subTest(path=path.name):
                self.assertTrue(counterpart.exists())
                self.assertGreaterEqual(len(path.read_text(encoding="utf-8").strip()), 450)

    def test_web_model_builds_benchmark_specific_fallback(self):
        model = (ROOT / "web" / "src" / "lib" / "research-model.mjs").read_text(
            encoding="utf-8"
        )
        detail = (
            ROOT / "web" / "src" / "components" / "BenchmarkDetail.astro"
        ).read_text(encoding="utf-8")

        self.assertIn("item.coverage_gap", model)
        self.assertIn("item.confounders", model)
        self.assertIn("evidence_brief", model)
        self.assertIn("research.evidenceBrief", detail)
        self.assertIn("resultSet", detail)

    def test_detail_validator_is_part_of_ci(self):
        workflow = (ROOT / ".github" / "workflows" / "validate.yml").read_text(
            encoding="utf-8"
        )
        self.assertIn("python scripts/validate_detail_pages.py", workflow)


if __name__ == "__main__":
    unittest.main()
