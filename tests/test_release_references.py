"""Frozen release-reference contract; tests are not factual certification."""
from __future__ import annotations
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('release_reference_renderer',ROOT/'scripts/render-release-references.py')
renderer=importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


def example():
    return {
        'status':'release-best','period':{'zh':'2024-02 · 论文 v1','en':'2024-02 · paper v1'},
        'results':[{'system':'Example agent','metric':'Accuracy','score':'0%'}],
        'scope':{'zh':'原始测试集中的已比较配置。','en':'Compared configurations on the original test set.'},
        'source':'https://example.org/paper-v1','locator':'Table 2',
        'comparison_scope':'Original test, Table 2','initial_release':True,
        'caveat':{'zh':'历史参考，不是当前最佳。','en':'Historical reference, not current SOTA.'},
    }


class ReleaseReferenceRenderingTests(unittest.TestCase):
    def test_block_is_directly_below_existing_h1(self):
        old='# Example\n\n**中文** | English\n\n## 正文\n\nExisting evidence.\n'
        text=renderer.render_note(old,example(),'zh')
        self.assertTrue(text.startswith('# Example\n\n'+renderer.START+'\n'))
        self.assertLess(text.index(renderer.END),text.index('**中文**'))
        self.assertEqual(renderer.strip_reference(text),old)

    def test_rendering_is_idempotent_and_preserves_body(self):
        old='# Example\n\n[Source](https://example.org)\n\n## Body\nText.\n'
        once=renderer.render_note(old,example(),'en')
        twice=renderer.render_note(once,example(),'en')
        self.assertEqual(once,twice)
        self.assertEqual(renderer.strip_reference(twice),old)
        self.assertEqual(twice.count(renderer.START),1)

    def test_zero_is_a_real_score_not_unknown(self):
        renderer.validate_record('example',example())
        self.assertIn('0%',renderer.render_block(example(),'en'))
        missing=renderer.fallback({'id':'example','released':'2024-02','artifacts':{'paper':'https://example.org/paper'}})
        self.assertEqual(missing['results'],[])
        self.assertNotIn('0%',renderer.render_block(missing,'en'))

    def test_unknown_does_not_consume_current_best(self):
        item={'id':'example','released':'2024-02','artifacts':{'paper':'https://example.org/paper'},'current_best':{'score':99.9,'model':'Future model'},'citations':{'count':999}}
        ref=renderer.fallback(item)
        self.assertEqual(ref['status'],'unverified')
        self.assertEqual(ref['results'],[])
        self.assertNotIn('99.9',renderer.render_block(ref,'en'))
        self.assertNotIn('Future model',renderer.render_block(ref,'en'))

    def test_unverified_result_cannot_smuggle_in_numbers(self):
        ref=example();ref['status']='unverified'
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)

    def test_best_claim_requires_explicit_comparison_and_initial_version(self):
        ref=example();ref.pop('comparison_scope')
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)
        ref=example();ref['initial_release']=False
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)

    def test_baseline_and_revised_paper_get_different_labels(self):
        ref=example();ref['status']='release-reference'
        self.assertIn('not a best claim',renderer.render_block(ref,'en'))
        ref['status']='later-version';ref['initial_release']=False
        renderer.validate_record('example',ref)
        self.assertIn('not the initial version',renderer.render_block(ref,'en'))
        ref['initial_release']=True
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)

    def test_unknown_version_does_not_get_release_label(self):
        ref=example();ref['status']='paper-reference';ref['initial_release']=None
        renderer.validate_record('example',ref)
        self.assertIn('initial version unverified',renderer.render_block(ref,'en'))
        ref['status']='release-reference'
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)

    def test_sources_and_bilingual_fields_are_required(self):
        ref=example();ref['source']='javascript:alert(1)'
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)
        ref=example();del ref['scope']['zh']
        with self.assertRaises(ValueError):renderer.validate_record('example',ref)

    def test_duplicate_or_unbalanced_markers_are_rejected(self):
        with self.assertRaises(ValueError):renderer.strip_reference('# X\n'+renderer.START)
        block=renderer.render_block(example(),'en')
        with self.assertRaises(ValueError):renderer.strip_reference('# X\n'+block+'\n'+block)


class RepositoryReleaseReferenceContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.items=json.loads((ROOT/'data/benchmarks.json').read_text())
        cls.data=json.loads((ROOT/'data/release-references.json').read_text())

    def test_no_orphan_records_and_every_record_validates(self):
        self.assertEqual(self.data['schema_version'],1)
        ids={r['id'] for r in self.items}
        self.assertFalse(set(self.data['benchmarks'])-ids)
        for r in self.items:
            renderer.validate_record(r['id'],self.data['benchmarks'].get(r['id'],renderer.fallback(r)))

    def test_all_bilingual_notes_have_the_exact_shared_reference(self):
        for r in self.items:
            record=self.data['benchmarks'].get(r['id'],renderer.fallback(r))
            for lang,ext in [('zh',''),('en','.en')]:
                text=(ROOT/f'benchmarks/{r["id"]}{ext}.md').read_text()
                self.assertEqual(text.count(renderer.START),1,r['id'])
                self.assertEqual(text.count(renderer.END),1,r['id'])
                self.assertIn(renderer.render_block(record,lang),text,r['id'])
                self.assertTrue(text.startswith(text.split('\n',1)[0]+'\n\n'+renderer.START),r['id'])
                for row in record['results']:
                    self.assertIn(row['score'],renderer.render_block(record,lang),r['id'])
                    self.assertIn(row['system'],renderer.render_block(record,lang),r['id'])

    def test_full_projection_is_current(self):
        process=subprocess.run([sys.executable,str(ROOT/'scripts/render-release-references.py'),'--check'],cwd=ROOT,text=True,capture_output=True,timeout=30)
        self.assertEqual(process.returncode,0,process.stdout+process.stderr)

    def test_known_later_live_scores_cannot_replace_launch_anchors(self):
        refs=self.data['benchmarks']
        self.assertEqual(refs['locomo']['results'][0]['score'],'41.4')
        self.assertEqual(refs['ds-1000']['results'][0]['score'],'43.3%')
        self.assertEqual(refs['mle-bench']['results'][0]['score'],'16.9%')
        self.assertEqual(refs['spider']['source'],'https://arxiv.org/abs/1809.08887v1')
        self.assertEqual(refs['pm-bench']['results'][0]['score'],'79.1%')


if __name__=='__main__':
    unittest.main()
