from contextlib import redirect_stderr
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import refresh_citations_safe as scheduled


class ScheduledCitationRefreshTests(unittest.TestCase):
    def test_rate_limit_is_explicit_deferred_refresh(self):
        before = (ROOT / "data/benchmarks.json").read_bytes()
        error = HTTPError("https://example.test", 429, "Rate limited", {}, None)
        output = io.StringIO()
        with patch.object(scheduled.updater, "_refresh_citations", side_effect=error), \
             patch.object(sys, "argv", ["refresh_citations_safe.py"]), \
             patch.object(scheduled.updater.subprocess, "run") as render, \
             redirect_stderr(output):
            self.assertEqual(0, scheduled.run())
        self.assertEqual(before, (ROOT / "data/benchmarks.json").read_bytes())
        render.assert_not_called()
        self.assertIn("no refresh completed", output.getvalue())

    def test_network_unavailable_does_not_fake_refresh(self):
        output = io.StringIO()
        with patch.object(scheduled.updater, "main", side_effect=URLError("timeout")), redirect_stderr(output):
            self.assertEqual(0, scheduled.run())
        self.assertIn("dates were retained", output.getvalue())

    def test_nontransient_and_schema_errors_remain_fatal(self):
        for error in (HTTPError("https://example.test", 403, "Forbidden", {}, None), RuntimeError("schema drift")):
            with self.subTest(error=type(error).__name__), patch.object(scheduled.updater, "main", side_effect=error):
                with self.assertRaises(type(error)):
                    scheduled.run()

    def test_success_passes_through(self):
        with patch.object(scheduled.updater, "main", return_value=0) as refresh:
            self.assertEqual(0, scheduled.run())
            refresh.assert_called_once()


if __name__ == "__main__":
    unittest.main()
