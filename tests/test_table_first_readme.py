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
        return text.split(f"<!-- {label}:START -->", 1)[1].split(f"<!-- {label}:END -->", 1)[0]

    def test_release_table_precedes_compact_benchmark_map(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                release = text.index('<a id="release-timeline"></a>')
                field_map = text.index('<a id="field-map"></a>')
                self.assertLess(release, field_map)
                self.assertNotIn("<details", text[release:field_map].lower())
                for heading in (
                    "## 最新条目深读",
                    "## 7 天 / 30 天：评价对象发生了什么变化",
                    "## 三个方向的演化",
                    "## 7 days / 30 days: What Changed in the Evaluation Object",
                    "## Three Areas",
                ):
                    self.assertNotIn(heading, text)

    def test_main_tables_use_one_what_it_tests_column(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                for label in (
                    "TABLE-FIRST:RECENT",
                    "TABLE-FIRST:AREA:agent-memory",
                    "TABLE-FIRST:AREA:rag",
                    "TABLE-FIRST:AREA:data-agent",
                ):
                    block = self._block(text, label)
                    expected_columns = 4 if label == "TABLE-FIRST:RECENT" else 5
                    for line in block.splitlines():
                        visible = line.split("<!--", 1)[0].strip()
                        if visible.startswith("|") and visible.endswith("|"):
                            self.assertEqual(
                                expected_columns,
                                len(visible.split("|")[1:-1]),
                                (language, label, line),
                            )
                    self.assertNotIn("相较以往", block)
                    self.assertNotIn("带来的变化", block)
                    self.assertNotIn("What changed", block)
                    self.assertNotIn("Why it changed the question", block)

    def test_each_map_area_has_an_accessible_capability_map(self):
        sections = (
            ("agent-memory", "benchmark-memory", "benchmark-rag"),
            ("rag", "benchmark-rag", "benchmark-data"),
            ("data-agent", "benchmark-data", "all-benchmarks"),
        )
        for filename, text in self.readmes.items():
            for area, start_anchor, end_anchor in sections:
                with self.subTest(filename=filename, area=area):
                    start = text.index(f'<a id="{start_anchor}"></a>')
                    end = text.index(f'<a id="{end_anchor}"></a>', start)
                    section = text[start:end]
                    start_marker = f"<!-- CAPABILITY-MAP:{area}:START -->"
                    end_marker = f"<!-- CAPABILITY-MAP:{area}:END -->"
                    self.assertEqual(1, section.count(start_marker))
                    self.assertEqual(1, section.count(end_marker))
                    diagram = section.split(start_marker, 1)[1].split(end_marker, 1)[0]
                    self.assertEqual(1, diagram.count("```mermaid"))
                    self.assertEqual(1, diagram.count("flowchart TB"))
                    self.assertIn("accTitle:", diagram)
                    self.assertIn("accDescr:", diagram)
                    for stage in ("Foundation", "Transition", "Frontier"):
                        self.assertIn(stage, diagram)
                    self.assertNotIn("**主干：**", section)
                    self.assertNotIn("**Defining chain:**", section)

    def test_complete_area_tables_remain_in_main_readme(self):
        for language, text in self.readmes.items():
            with self.subTest(language=language):
                before_library = text[: text.index('<a id="library"></a>')]
                for area in ("agent-memory", "rag", "data-agent"):
                    self.assertIn(f"TABLE-FIRST:AREA:{area}:START", before_library)


if __name__ == "__main__":
    unittest.main()
