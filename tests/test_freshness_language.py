from pathlib import Path
import json, unittest
ROOT=Path(__file__).resolve().parents[1]
class FreshnessLanguageContract(unittest.TestCase):
    def test_readme_counts_follow_registry(self):
        n=len(json.loads((ROOT/'data/benchmarks.json').read_text()))
        self.assertIn(f'**{n} 个基准**',(ROOT/'README.md').read_text())
        self.assertIn(f'**{n} benchmarks**',(ROOT/'README.en.md').read_text())
    def test_frontier_separates_factual_watchlist_from_interpretation(self):
        t=(ROOT/'web/src/pages/[lang]/frontier/index.astro').read_text()
        self.assertIn('publicationWindow',t)
        self.assertIn('inReleaseWindow',t)
        self.assertIn('Editorial observations',t)
        self.assertIn('timeline/',t)
        self.assertIn('period.asOf',t)
        self.assertNotIn('progress-map__point',t)
        self.assertNotIn('getProgressPoint',t)
    def test_scale_qa_chinese_avoids_unnecessary_english_prose(self):
        t=(ROOT/'benchmarks/scale-qa.md').read_text()
        for phrase in ['memory system','evidence containment','system-level evidence','runtime noise construction','protocol cell']:
            self.assertNotIn(phrase,t)
    def test_freshness_scan_is_current_and_separate(self):
        f=json.loads((ROOT/'data/freshness.json').read_text())
        self.assertEqual('2026-09-05',f['discovery_scan_at'])
        self.assertIn('separately',f['note'])
if __name__=='__main__': unittest.main()
