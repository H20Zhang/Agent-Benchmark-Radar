from pathlib import Path
import json, re, unittest
ROOT = Path(__file__).resolve().parents[1]
class EvaluationRecipeRoutingTest(unittest.TestCase):
    def test_area_lists_precede_optional_recipe_guidance(self):
        for suffix in ("", ".en"):
            text=(ROOT/f"README{suffix}.md").read_text()
            for area in ("memory", "rag", "data"):
                self.assertIn(f"#registry-{area}", text.split("ONBOARDING:END")[0])
            self.assertLess(text.index('TABLE-FIRST:AREA:data-agent:END'),text.index('<a id="evaluation-recipes"></a>'))
            self.assertIn(f"library/evaluation-recipes{suffix}.md", text)
    def test_recipe_tables_preserve_bilingual_membership_and_roles(self):
        expected=json.loads((ROOT/'data/recipes.json').read_text())
        for lang,suffix in (("zh",""),("en",".en")):
            text=(ROOT/f"library/evaluation-recipes{suffix}.md").read_text()
            rows=[x for x in text.splitlines() if x.startswith('| **')]
            self.assertEqual(len(expected),len(rows))
            for recipe,row in zip(expected,rows):
                cells=[x.strip() for x in row.split('|')[1:-1]]
                self.assertEqual(4,len(cells))
                for index,key in ((1,'core'),(2,'complement')):
                    ids=re.findall(r'benchmarks/([a-z0-9-]+)(?:\.en)?\.md',cells[index])
                    self.assertEqual(recipe[key],ids)
                self.assertIn(recipe['claim_boundary'][lang],cells[3])
                self.assertIn(recipe['next_validation'][lang],cells[3])
