from pathlib import Path
import re
import unittest
ROOT=Path(__file__).resolve().parents[1]
class LibraryTableShapeTest(unittest.TestCase):
    def test_complete_tables_have_five_cells(self):
        for filename in ('README.md','README.en.md'):
            text=(ROOT/'library'/filename).read_text()
            blocks=re.findall(r'<!-- COMPLETE-(?:TIMELINE|MAP:[a-z-]+):START -->(.*?)<!-- COMPLETE-(?:TIMELINE|MAP:[a-z-]+):END -->',text,re.S)
            self.assertEqual(4,len(blocks))
            for block in blocks:
                for row in block.splitlines():
                    if row.startswith('|'):
                        self.assertEqual(5,len(row.strip().strip('|').split('|')),row)
