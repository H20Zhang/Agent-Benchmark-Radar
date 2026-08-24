import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def _load_updater():
    path = ROOT / "scripts" / "update_citations.py"
    spec = importlib.util.spec_from_file_location("citation_updater", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class CitationRefreshResilienceTest(unittest.TestCase):
    def test_confirmed_citation_survives_transient_lookup_miss(self):
        updater = _load_updater()
        record = {
            "id": "example",
            "artifacts": {"paper": "https://aclanthology.org/2026.acl-long.1/"},
            "citations": {
                "count": 6,
                "source": "semantic-scholar",
                "updated_at": "2026-08-24",
                "status": "ok",
                "paper_id": "confirmed-paper-id",
                "url": "https://www.semanticscholar.org/paper/confirmed-paper-id",
            },
        }
        before = dict(record["citations"])
        with patch.object(updater, "_request_json", return_value=[None]), patch.object(
            updater, "_s2_title_fallback", return_value=None
        ):
            changed = updater._refresh_citations([record], "2026-08-25")
        self.assertFalse(changed)
        self.assertEqual(before, record["citations"])


if __name__ == "__main__":
    unittest.main()
