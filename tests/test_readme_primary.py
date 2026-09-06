from copy import deepcopy
from pathlib import Path
import json, re, subprocess, sys, unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from readme_contract import validate, table_block, ID
class ReadmePrimary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.zh=(ROOT/'README.md').read_text();cls.en=(ROOT/'README.en.md').read_text()
        cls.records=json.loads((ROOT/'data/benchmarks.json').read_text())
    def test_publication_is_deterministic_and_current(self):
        p=subprocess.run(['node',str(ROOT/'scripts/render-readme.mjs'),'--check'],capture_output=True,text=True)
        self.assertEqual(0,p.returncode,p.stdout+p.stderr)
    def test_missing_or_duplicate_rows_are_rejected(self):
        line=next(x for x in table_block(self.zh,'TABLE-FIRST:AREA:agent-memory').splitlines() if ID.search(x))
        self.assertTrue(validate(self.zh.replace(line,'',1),self.en,self.records))
        self.assertTrue(validate(self.zh.replace(line,line+'\n'+line,1),self.en,self.records))
    def test_date_uncertainty_cannot_be_erased(self):
        self.assertTrue(validate(self.zh.replace('2026-09-01†','2026-09-01',1),self.en,self.records))
    def test_wrong_summary_is_rejected(self):
        self.assertTrue(validate(self.zh.replace('测持久记忆中的虚假权限形成','这是错误描述',1),self.en,self.records))
    def test_wrong_language_note_is_rejected(self):
        self.assertTrue(validate(self.zh,self.en.replace('benchmarks/eal-bench.en.md','benchmarks/eal-bench.md',1),self.records))
    def test_direct_code_resource_cannot_be_removed(self):
        self.assertTrue(validate(self.zh.replace('https://github.com/snap-research/locomo','https://example.invalid',1),self.en,self.records))
    def test_citations_do_not_confuse_zero_and_unknown(self):
        self.assertTrue(validate(self.zh.replace('[794]','[0]',1),self.en,self.records))
    def test_root_has_no_score_ranking_or_hidden_rows(self):
        for text in (self.zh,self.en):
            self.assertNotIn('<details',text)
            self.assertNotIn('```mermaid',text)
            self.assertNotIn('RESULT-SNAPSHOTS:START',text)
            self.assertNotIn('h20zhang.github.io/Agent-Benchmark-Radar',text)
    def test_both_languages_keep_the_same_month_jumps(self):
        z=re.findall(r'id="month-([0-9-]+)"',self.zh);e=re.findall(r'id="month-([0-9-]+)"',self.en)
        self.assertTrue(z);self.assertEqual(z,e)
    def test_repo_is_not_mislabeled_as_paper(self):
        self.assertNotRegex(self.zh,r'\[论文\]\(https://github.com/[^)]+(?<!\.pdf)\)')
if __name__=='__main__':unittest.main()
