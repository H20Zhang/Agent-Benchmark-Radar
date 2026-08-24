from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
AREAS = ("agent-memory", "rag", "data-agent")
ID_RE = re.compile(r"<!--\s*benchmark-id:([a-z0-9-]+)\s*-->")


class CitationProjectionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads((ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8"))
        cls.by_id = {record["id"]: record for record in cls.records}

    def test_every_record_has_auditable_citation_state(self):
        for record in self.records:
            with self.subTest(benchmark=record["id"]):
                citation = record.get("citations")
                self.assertIsInstance(citation, dict)
                self.assertEqual("semantic-scholar", citation.get("source"))
                self.assertRegex(citation.get("updated_at", ""), r"^\d{4}-\d{2}-\d{2}$")
                self.assertIn(citation.get("status"), {"ok", "no-paper", "unmatched"})
                if citation.get("status") == "ok":
                    self.assertIsInstance(citation.get("count"), int)
                    self.assertGreaterEqual(citation["count"], 0)
                    self.assertTrue(citation.get("paper_id"))
                    self.assertTrue(citation.get("url"))
                else:
                    self.assertIsNone(citation.get("count"))

    def test_complete_area_tables_show_registry_counts(self):
        for filename in ("README.md", "README.en.md"):
            text = (ROOT / filename).read_text(encoding="utf-8")
            with self.subTest(filename=filename):
                self.assertIn("CITATION-META:START", text)
                for area in AREAS:
                    block = text.split(f"<!-- TABLE-FIRST:AREA:{area}:START -->", 1)[1].split(
                        f"<!-- TABLE-FIRST:AREA:{area}:END -->", 1
                    )[0]
                    rows = [line for line in block.splitlines() if ID_RE.search(line)]
                    expected_ids = [record["id"] for record in self.records if record["area"] == area]
                    self.assertEqual(len(expected_ids), len(rows))
                    for line in rows:
                        identity = ID_RE.search(line).group(1)
                        cells = [cell.strip() for cell in line.split("|")[1:-1]]
                        self.assertEqual(5, len(cells))
                        citation = self.by_id[identity]["citations"]
                        if citation["status"] == "ok":
                            self.assertIn(f"{citation['count']:,}", cells[2])
                            self.assertIn(citation["url"], cells[2])
                        else:
                            self.assertEqual("—", cells[2])


if __name__ == "__main__":
    unittest.main()
