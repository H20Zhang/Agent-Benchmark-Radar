from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FrontPageSignalContractTest(unittest.TestCase):
    def test_editorial_guide_is_secondary_to_complete_benchmark_tables(self):
        for suffix in ("", ".en"):
            main = (ROOT / f"README{suffix}.md").read_text()
            guide = (ROOT / f"docs/reading-guide{suffix}.md").read_text()
            self.assertLess(main.index('TABLE-FIRST:AREA:data-agent:END'), main.index('<a id="frontier-signals"></a>'))
            self.assertNotIn('FRONTIER-SIGNALS:START', main)
            block = guide.split('<!-- FRONTIER-SIGNALS:START -->')[1].split('<!-- FRONTIER-SIGNALS:END -->')[0]
            self.assertEqual(3, len([x for x in block.splitlines() if x.startswith('| **')]))
            for area in ('Agent Memory', 'RAG / Agentic Retrieval', 'Data Agents'):
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
