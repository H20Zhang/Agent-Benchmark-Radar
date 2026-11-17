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
    def _with_citation(self, text, record, replacement):
        block = table_block(text, f"TABLE-FIRST:AREA:{record['area']}")
        rows = [
            line for line in block.splitlines()
            if (match := ID.search(line)) and match.group(1) == record['id']
        ]
        self.assertEqual(1, len(rows), record['id'])
        row = rows[0]
        cells = row.split('|')
        self.assertEqual(7, len(cells), record['id'])
        citation = record['citations']
        expected = (
            f"[{citation['count']:,}]({citation['url']})"
            if citation['status'] == 'ok' else '—'
        )
        self.assertEqual(expected, cells[5].strip())
        self.assertNotEqual(expected, replacement)
        cells[5] = f' {replacement} '
        changed = text.replace(row, '|'.join(cells), 1)
        self.assertNotEqual(text, changed)
        return changed

    def test_citations_do_not_confuse_zero_and_unknown(self):
        verified = [x for x in self.records if x['citations']['status'] == 'ok']
        positive = next(x for x in verified if x['citations']['count'] > 0)
        zero = next(x for x in verified if x['citations']['count'] == 0)
        unknown = next(x for x in self.records if x['citations']['status'] != 'ok')
        cases = (
            (positive, f"[0]({positive['citations']['url']})", 'citation drift'),
            (zero, '—', 'citation drift'),
            (unknown, f"[0]({positive['citations']['url']})", 'unknown citations must not become zero'),
        )
        for language, text in (('zh', self.zh), ('en', self.en)):
            for record, replacement, error in cases:
                with self.subTest(language=language, benchmark=record['id']):
                    mutated = self._with_citation(text, record, replacement)
                    errors = validate(
                        mutated if language == 'zh' else self.zh,
                        mutated if language == 'en' else self.en,
                        self.records,
                    )
                    filename = 'README.md' if language == 'zh' else 'README.en.md'
                    self.assertIn(f"{filename}: {record['id']} {error}", errors)

    def test_citation_count_and_url_mismatches_are_rejected(self):
        record = next(x for x in self.records
                      if x['citations']['status'] == 'ok' and x['citations']['count'] > 0)
        citation = record['citations']
        replacements = (
            f"[{citation['count'] + 1:,}]({citation['url']})",
            f"[{citation['count']:,}](https://example.invalid/citation)",
        )
        for language, text in (('zh', self.zh), ('en', self.en)):
            for replacement in replacements:
                with self.subTest(language=language, replacement=replacement):
                    mutated = self._with_citation(text, record, replacement)
                    errors = validate(
                        mutated if language == 'zh' else self.zh,
                        mutated if language == 'en' else self.en,
                        self.records,
                    )
                    filename = 'README.md' if language == 'zh' else 'README.en.md'
                    self.assertIn(f"{filename}: {record['id']} citation drift", errors)

    def test_changed_verified_citation_snapshot_is_accepted(self):
        record = next(x for x in self.records
                      if x['citations']['status'] == 'ok' and x['citations']['count'] > 0)
        updated_count = record['citations']['count'] + 1
        updated_records = deepcopy(self.records)
        updated_record = next(x for x in updated_records if x['id'] == record['id'])
        updated_record['citations']['count'] = updated_count
        updated_link = f"[{updated_count:,}]({record['citations']['url']})"
        zh = self._with_citation(self.zh, record, updated_link)
        en = self._with_citation(self.en, record, updated_link)
        self.assertEqual([], validate(zh, en, updated_records))

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
