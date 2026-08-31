from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class EvaluationRecipeRoutingTest(unittest.TestCase):
    def _read(self, filename: str) -> str:
        return (ROOT / filename).read_text(encoding="utf-8")

    def test_area_router_reaches_map_recipe_and_registry(self):
        for filename in ("README.md", "README.en.md"):
            with self.subTest(filename=filename):
                text = self._read(filename)
                onboarding = text.split("<!-- ONBOARDING:START -->", 1)[1].split("<!-- ONBOARDING:END -->", 1)[0]
                for area in ("memory", "rag", "data"):
                    for target in (f"#benchmark-{area}", f"#recipe-{area}", f"#registry-{area}"):
                        self.assertIn(target, onboarding)
                self.assertLess(text.index('<a id="evaluation-recipes"></a>'), text.index('<a id="frontier-signals"></a>'))

    def test_recipe_tables_are_bounded_and_bilingual(self):
        observed_links = {}
        for filename in ("README.md", "README.en.md"):
            with self.subTest(filename=filename):
                text = self._read(filename)
                block = text.split("<!-- EVALUATION-RECIPES:START -->", 1)[1].split("<!-- EVALUATION-RECIPES:END -->", 1)[0]
                for index, area in enumerate(("memory", "rag", "data")):
                    start = block.index(f'<a id="recipe-{area}"></a>')
                    next_area = ("rag", "data", None)[index]
                    end = block.index(f'<a id="recipe-{next_area}"></a>', start + 1) if next_area else len(block)
                    rows = [line for line in block[start:end].splitlines() if line.startswith("| **")]
                    self.assertEqual(5, len(rows))
                    for row in rows:
                        self.assertGreaterEqual(len(re.findall(r"\]\(https?://[^)]+\)", row)), 2)
                observed_links[filename] = re.findall(r"\]\((https?://[^)]+)\)", block)
        self.assertEqual(observed_links["README.md"], observed_links["README.en.md"])


if __name__ == "__main__":
    unittest.main()
