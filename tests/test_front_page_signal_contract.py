from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FrontPageSignalContractTest(unittest.TestCase):
    def test_signal_table_is_first_research_surface(self):
        cases = (
            (
                "README.md",
                "近 30 天：三个变化",
                ("Agent Memory", "RAG / Agentic Retrieval", "Data Agents"),
            ),
            (
                "README.en.md",
                "Last 30 Days: Three Shifts",
                ("Agent Memory", "RAG / Agentic Retrieval", "Data Agents"),
            ),
        )
        for filename, heading, areas in cases:
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding="utf-8")
                release = text.index('<a id="release-timeline"></a>')
                prefix = text[:release]
                self.assertIn(heading, prefix)
                self.assertEqual(1, prefix.count("<!-- FRONTIER-SIGNALS:START -->"))
                self.assertEqual(1, prefix.count("<!-- FRONTIER-SIGNALS:END -->"))
                block = prefix.split("<!-- FRONTIER-SIGNALS:START -->", 1)[1].split(
                    "<!-- FRONTIER-SIGNALS:END -->", 1
                )[0]
                rows = [line for line in block.splitlines() if line.startswith("| **")]
                self.assertEqual(3, len(rows))
                for area in areas:
                    self.assertIn(area, block)
                self.assertGreaterEqual(len(re.findall(r"\]\(https?://", block)), 9)

    def test_mechanical_intro_does_not_return(self):
        banned = {
            "README.md": ("默认入口", "先从这里理解", "[30 秒：", "> **比较规则："),
            "README.en.md": (
                "The entry point to the Research Radar family",
                "Start here to see",
                "[30 sec:",
                "> **Comparison rule.",
            ),
        }
        for filename, phrases in banned.items():
            with self.subTest(filename=filename):
                text = (ROOT / filename).read_text(encoding="utf-8")
                prefix = text[: text.index('<a id="release-timeline"></a>')]
                for phrase in phrases:
                    self.assertNotIn(phrase, prefix)


if __name__ == "__main__":
    unittest.main()
