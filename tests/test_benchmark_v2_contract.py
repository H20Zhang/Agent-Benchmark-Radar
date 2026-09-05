from copy import deepcopy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


class CanonicalTimeContractTest(unittest.TestCase):
    def test_repository_registry_satisfies_time_contract(self):
        records = json.loads((ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8"))
        self.assertEqual([], validate_reading.validate_benchmark_registry(records))

    def test_partial_v2_record_is_rejected(self):
        record = {"id": "partial", "released": "2026-08", "map_delta": "early_signal"}
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(errors)

    def test_native_v2_event_order_is_enforced(self):
        record = {
            "id": "native",
            "released": "2026-08-20",
            "published_at": "2026-08-20T02:00:00Z",
            "first_seen_at": "2026-08-20T01:00:00Z",
            "radar_published_at": "2026-08-20T03:00:00Z",
            "time_provenance": "native_v2",
            "map_delta": "early_signal",
        }
        self.assertTrue(any("published_at <= first_seen_at <= radar_published_at" in e for e in validate_reading.validate_record_time_contract(record)))


class PublicProjectionV3Test(unittest.TestCase):
    def setUp(self):
        self.zh = (ROOT / "README.md").read_text(encoding="utf-8")
        self.en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        self.records = json.loads((ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8"))

    def test_repository_projection_is_compact_and_bilingual(self):
        self.assertEqual([], validate_reading.validate_public_readme(self.zh, self.en, self.records))

    def test_retired_deep_read_surface_is_rejected(self):
        mutated = self.zh.replace('<a id="field-map"></a>', '## 最新条目深读\n\n<a id="field-map"></a>', 1)
        errors = validate_reading.validate_public_readme(mutated, self.en, self.records)
        self.assertTrue(any("retired reader surface" in e for e in errors), errors)

    def test_parallel_change_column_is_rejected(self):
        for header in ("| Time | Area | Benchmark | What it tests |", "| Time | Area | Benchmark | What it measures |"):
            if header in self.en:
                mutated = self.en.replace(header, header[:-1] + " What changed |", 1)
                break
        else:
            self.fail("release table header not found")
        errors = validate_reading.validate_public_readme(self.zh, mutated, self.records)
        self.assertTrue(any("four visible columns" in e or "parallel change column" in e for e in errors), errors)


if __name__ == "__main__":
    unittest.main()
