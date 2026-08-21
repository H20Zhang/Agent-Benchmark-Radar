from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TableFirstReadmeContractTest(unittest.TestCase):
    def setUp(self):
        self.readmes = {
            "README.md": (ROOT / "README.md").read_text(encoding="utf-8"),
            "README.en.md": (ROOT / "README.en.md").read_text(encoding="utf-8"),
        }

    @staticmethod
    def _block(text: str, label: str) -> str:
        start = f"<!-- {label}:START -->"
        end = f"<!-- {label}:END -->"
        assert text.count(start) == 1, (label, "start", text.count(start))
        assert text.count(end) == 1, (label, "end", text.count(end))
        return text.split(start, 1)[1].split(end, 1)[0]

    def test_release_table_is_the_first_research_timeline_surface(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                release = text.index('<a id="release-timeline"></a>')
                deep = text.index('<a id="timeline"></a>')
                periods = text.index('<a id="periods"></a>')
                self.assertLess(release, deep)
                self.assertLess(deep, periods)

                block = self._block(text, "TABLE-FIRST:RECENT")
                rows = [
                    line
                    for line in block.splitlines()
                    if line.startswith("| 2026-")
                ]
                self.assertGreaterEqual(len(rows), 40)
                self.assertNotIn("<details", block.lower())
                self.assertNotIn("radar_published_at", block)
                self.assertIn("data-exploration-benchmark", block)

    def test_complete_area_tables_remain_in_main_readme(self):
        minimum_rows = {
            "agent-memory": 25,
            "rag": 25,
            "data-agent": 25,
        }
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                field_map = text.index('<a id="field-map"></a>')
                all_tables = text.index('<a id="all-benchmarks"></a>')
                reading = text.index('<a id="reading-paths"></a>')
                self.assertLess(field_map, all_tables)
                self.assertLess(all_tables, reading)

                for area, minimum in minimum_rows.items():
                    block = self._block(text, f"TABLE-FIRST:AREA:{area}")
                    rows = [
                        line
                        for line in block.splitlines()
                        if "<!-- benchmark-id:" in line
                    ]
                    self.assertGreaterEqual(
                        len(rows), minimum, f"{language} {area} was thinned"
                    )

    def test_library_is_not_the_only_complete_table_surface(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                before_library = text[: text.index('<a id="library"></a>')]
                self.assertIn("TABLE-FIRST:AREA:agent-memory:START", before_library)
                self.assertIn("TABLE-FIRST:AREA:rag:START", before_library)
                self.assertIn("TABLE-FIRST:AREA:data-agent:START", before_library)


if __name__ == "__main__":
    unittest.main()
