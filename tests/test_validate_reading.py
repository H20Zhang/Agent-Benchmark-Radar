import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading
from validate_reading import (
    validate_benchmark_aliases,
    validate_benchmark_library,
    validate_family_routes,
    validate_public_readme,
)


ROUTES = """[Agent Memory](https://github.com/H20Zhang/Agent-Memory-Radar#field-map)
[Agentic RAG](https://github.com/H20Zhang/Agentic-RAG-Radar#field-map)
[Data Agent](https://github.com/H20Zhang/Data-Agent-Radar#field-map)
"""
ALIASES = """<a id="frontier"></a>
<a id="changes"></a>
<a id="evolution"></a>
<a id="benchmark-memory"></a>
<a id="benchmark-rag"></a>
<a id="benchmark-data"></a>
"""


class EvaluationFrontierSurfaceTest(unittest.TestCase):
    def _run_validator(self, zh: str, en: str) -> tuple[int, str]:
        with (
            tempfile.NamedTemporaryFile(
                dir=ROOT, prefix="README.frontier-", suffix=".md", delete=False
            ) as zh_file,
            tempfile.NamedTemporaryFile(
                dir=ROOT, prefix="README.frontier-en-", suffix=".md", delete=False
            ) as en_file,
        ):
            zh_path = Path(zh_file.name)
            en_path = Path(en_file.name)
        try:
            zh_path.write_text(zh, encoding="utf-8")
            en_path.write_text(en, encoding="utf-8")
            output = io.StringIO()
            with (
                patch.object(validate_reading, "ZH", zh_path),
                patch.object(validate_reading, "EN", en_path),
                contextlib.redirect_stdout(output),
            ):
                result = validate_reading.main()
        finally:
            zh_path.unlink()
            en_path.unlink()
        return result, output.getvalue()

    def test_repository_validator_accepts_positive_frontier_headings(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = validate_reading.main()

        self.assertEqual(0, result, output.getvalue())

    def test_stable_frontier_anchor_is_required(self):
        anchor = '<a id="evaluation-frontiers"></a>'
        zh = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        self.assertIn(anchor, zh)
        self.assertIn(anchor, en)

        result, output = self._run_validator(
            zh.replace(anchor, "", 1), en
        )

        self.assertEqual(1, result)
        self.assertIn("evaluation-frontiers", output)


class CapabilityMapSurfaceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads(
            (ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8")
        )
        cls.zh = (ROOT / "README.md").read_text(encoding="utf-8")
        cls.en = (ROOT / "README.en.md").read_text(encoding="utf-8")

    def test_repository_capability_maps_satisfy_public_contract(self):
        self.assertEqual(
            [], validate_public_readme(self.zh, self.en, self.records)
        )

    def test_map_direction_is_validated_without_requiring_a_site_route(self):
        mutated = self.en.replace("flowchart TB", "flowchart LR", 1)
        errors = validate_public_readme(self.zh, mutated, self.records)

        self.assertTrue(any("flowchart TB" in error for error in errors), errors)
        self.assertFalse(any("interactive site route" in error for error in errors), errors)


class AttentionNavigationTest(unittest.TestCase):
    def test_repository_exposes_the_same_attention_layers_in_both_languages(self):
        zh = (ROOT / "README.md").read_text(encoding="utf-8")
        en = (ROOT / "README.en.md").read_text(encoding="utf-8")
        for text in (zh, en):
            positions = [
                text.index('<a id="frontier-signals"></a>'),
                text.index('<a id="release-timeline"></a>'),
                text.index('<a id="timeline"></a>'),
                text.index('<a id="periods"></a>'),
                text.index('<a id="field-map"></a>'),
                text.index('<a id="reading-paths"></a>'),
                text.index('<a id="library"></a>'),
            ]
            self.assertEqual(sorted(positions), positions)

    def test_editorial_contract_preserves_layer_navigation(self):
        standard = (ROOT / "docs" / "EDITORIAL_STANDARD.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("Layer-level attention navigation", standard)
        self.assertNotIn("reading-time navigation (`30 秒`, `5 min`)", standard)


class FamilyRouteTest(unittest.TestCase):
    def test_repository_family_routes_satisfy_contract(self):
        self.assertEqual(
            [],
            validate_family_routes(
                (ROOT / "README.md").read_text(encoding="utf-8"),
                (ROOT / "README.en.md").read_text(encoding="utf-8"),
            ),
        )

    def test_missing_or_wrong_sibling_field_map_route_is_rejected(self):
        mutations = (
            (
                "https://github.com/H20Zhang/Agent-Memory-Radar#field-map",
                "",
            ),
            (
                "https://github.com/H20Zhang/Agentic-RAG-Radar#field-map",
                "https://github.com/H20Zhang/Agentic-RAG-Radar#wrong",
            ),
            (
                "https://github.com/H20Zhang/Data-Agent-Radar#field-map",
                "https://github.com/H20Zhang/Data-Agent-Radar",
            ),
        )
        for expected_route, replacement in mutations:
            with self.subTest(route=expected_route):
                self.assertTrue(
                    any(
                        "route" in error.lower()
                        for error in validate_family_routes(
                            ROUTES,
                            ROUTES.replace(expected_route, replacement),
                        )
                    )
                )

    def test_hidden_exact_routes_cannot_rescue_visible_routes_without_fragments(self):
        visible_routes = ROUTES.replace("#field-map", "")
        hidden_routes = f"<!--\n{ROUTES}-->\n"

        errors = validate_family_routes(
            visible_routes + hidden_routes,
            visible_routes + hidden_routes,
        )

        self.assertEqual(6, len(errors), errors)
        for label in ("Agent Memory", "Agentic RAG", "Data Agent"):
            self.assertEqual(2, sum(label in error for error in errors), errors)


class BenchmarkAliasTest(unittest.TestCase):
    def test_repository_benchmark_aliases_satisfy_contract(self):
        self.assertEqual(
            [],
            validate_benchmark_aliases(
                (ROOT / "README.md").read_text(encoding="utf-8"),
                (ROOT / "README.en.md").read_text(encoding="utf-8"),
            ),
        )

    def test_missing_or_duplicate_benchmark_alias_is_rejected(self):
        for alias in (
            "frontier",
            "changes",
            "evolution",
            "benchmark-memory",
            "benchmark-rag",
            "benchmark-data",
        ):
            anchor = f'<a id="{alias}"></a>'
            with self.subTest(alias=alias, mutation="missing"):
                self.assertTrue(
                    any(
                        "alias" in error.lower()
                        for error in validate_benchmark_aliases(
                            ALIASES.replace(anchor, "", 1), ALIASES
                        )
                    )
                )
            with self.subTest(alias=alias, mutation="duplicate"):
                self.assertTrue(
                    any(
                        "alias" in error.lower()
                        for error in validate_benchmark_aliases(
                            ALIASES.replace(anchor, anchor + anchor, 1), ALIASES
                        )
                    )
                )

    def test_hidden_alias_cannot_satisfy_or_duplicate_a_visible_alias(self):
        for alias in (
            "frontier",
            "changes",
            "evolution",
            "benchmark-memory",
            "benchmark-rag",
            "benchmark-data",
        ):
            anchor = f'<a id="{alias}"></a>'
            with self.subTest(alias=alias, mutation="hidden-only"):
                hidden_only = ALIASES.replace(anchor, f"<!-- {anchor} -->", 1)
                self.assertTrue(
                    any(
                        f"missing benchmark compatibility alias {alias}" in error.lower()
                        for error in validate_benchmark_aliases(hidden_only, ALIASES)
                    )
                )
            with self.subTest(alias=alias, mutation="hidden-decoy"):
                with_decoy = ALIASES.replace(
                    anchor, f"<!-- {anchor} -->\n{anchor}", 1
                )
                self.assertEqual(
                    [], validate_benchmark_aliases(with_decoy, ALIASES)
                )


class BenchmarkLibraryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads(
            (ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8")
        )
        cls.zh = (ROOT / "library" / "README.md").read_text(encoding="utf-8")
        cls.en = (ROOT / "library" / "README.en.md").read_text(encoding="utf-8")

    def test_repository_library_is_complete_canonical_and_bilingual(self):
        self.assertEqual(
            [], validate_benchmark_library(self.zh, self.en, self.records)
        )

    def test_missing_or_duplicate_canonical_identity_is_rejected(self):
        marker = "<!-- benchmark-id:data-exploration-benchmark -->"
        missing = self.en.replace(marker, "", 1)
        duplicate = self.en.replace(marker, marker + marker, 1)

        self.assertTrue(
            any(
                "complete timeline" in error.lower()
                for error in validate_benchmark_library(self.zh, missing, self.records)
            )
        )
        self.assertTrue(
            any(
                "duplicate" in error.lower()
                for error in validate_benchmark_library(self.zh, duplicate, self.records)
            )
        )

    def test_comment_only_identity_cannot_replace_a_visible_canonical_row(self):
        row = next(
            line
            for line in self.en.splitlines()
            if "<!-- benchmark-id:data-exploration-benchmark -->" in line
        )
        hidden_only = self.en.replace(
            row,
            "<!-- benchmark-id:data-exploration-benchmark -->",
            1,
        )

        self.assertTrue(
            any(
                "visible canonical row" in error.lower()
                for error in validate_benchmark_library(self.zh, hidden_only, self.records)
            )
        )

    def test_visible_title_primary_link_and_release_must_match_canonical_record(self):
        mutations = (
            ("[Data Exploration Benchmark]", "[Wrong title]"),
            ("https://arxiv.org/abs/2608.16045", "https://example.com/wrong"),
            ("| 2026-08-17 | [Data Exploration Benchmark]", "| 2026-08-18 | [Data Exploration Benchmark]"),
        )
        for old, new in mutations:
            with self.subTest(mutation=old):
                mutated = self.en.replace(old, new, 1)
                self.assertTrue(
                    any(
                        "visible canonical row" in error.lower()
                        for error in validate_benchmark_library(
                            self.zh, mutated, self.records
                        )
                    )
                )

    def test_area_membership_and_order_are_canonical(self):
        start = self.en.index("<!-- COMPLETE-MAP:agent-memory:START -->")
        end = self.en.index("<!-- COMPLETE-MAP:agent-memory:END -->", start)
        block = self.en[start:end]
        rows = [
            line
            for line in block.splitlines()
            if "<!-- benchmark-id:" in line
        ]
        swapped = block.replace(rows[0], "__ROW_ZERO__", 1)
        swapped = swapped.replace(rows[1], rows[0], 1)
        swapped = swapped.replace("__ROW_ZERO__", rows[1], 1)
        mutated = self.en[:start] + swapped + self.en[end:]

        self.assertTrue(
            any(
                "agent-memory map" in error.lower()
                for error in validate_benchmark_library(self.zh, mutated, self.records)
            )
        )


if __name__ == "__main__":
    unittest.main()
