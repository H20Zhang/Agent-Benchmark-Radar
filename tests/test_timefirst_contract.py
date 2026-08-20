from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from timefirst_contract import validate_pair


def make_pair(count: int) -> tuple[str, str]:
    zh_entries = []
    en_entries = []
    for index in range(1, count + 1):
        day = 21 - index
        date = f"2026-08-{day:02d}"
        zh_entries.append(
            f'''<a id="entry-work-{index}"></a>
<details><summary>{date} · Work {index} · Area / problem {index} <!-- timefirst:area=area-problem-{index} --> — delta {index} <!-- timefirst:delta=delta-{index} --></summary>

**问题。** research question <!-- timefirst:question=question-{index} -->

**证据。** retrieval coverage ablation <!-- timefirst:evidence=evidence-{index}~retrieval-coverage-ablation -->

**限制。** ingestion latency overhead <!-- timefirst:caveat=caveat-{index}~ingestion-latency-overhead -->

**地图。** `early_signal`

**链接。** [Primary](https://example.com/work-{index}) · [Local](notes/work-{index}.md)

</details>'''
        )
        en_entries.append(
            f'''<a id="entry-work-{index}"></a>
<details><summary>{date} · Work {index} · Area / problem {index} <!-- timefirst:area=area-problem-{index} --> — delta {index} <!-- timefirst:delta=delta-{index} --></summary>

**Question.** research question <!-- timefirst:question=question-{index} -->

**Evidence.** retrieval coverage ablation <!-- timefirst:evidence=evidence-{index}~retrieval-coverage-ablation -->

**Caveat.** ingestion latency overhead <!-- timefirst:caveat=caveat-{index}~ingestion-latency-overhead -->

**Map.** `early_signal`

**Links.** [Primary](https://example.com/work-{index}) · [Local](notes/work-{index}.en.md)

</details>'''
        )

    zh = f'''<a id="timeline"></a><a id="latest"></a>
## 最新时间线

{chr(10).join(zh_entries)}

<a id="periods"></a>
## 时间窗变化

<a id="last-7-days"></a>
### 过去 7 天

2026-08-14—2026-08-20

<a id="last-30-days"></a>
### 过去 30 天

2026-07-22—2026-08-20

<a id="field-map"></a>
## 领域地图

<a id="reading-paths"></a>
## 阅读路径

<a id="library"></a>
## 资料库
'''
    en = f'''<a id="timeline"></a><a id="latest"></a>
## Latest Timeline

{chr(10).join(en_entries)}

<a id="periods"></a>
## Period Changes

<a id="last-7-days"></a>
### Last 7 days

2026-08-14—2026-08-20

<a id="last-30-days"></a>
### Last 30 days

2026-07-22—2026-08-20

<a id="field-map"></a>
## Field Map

<a id="reading-paths"></a>
## Reading Paths

<a id="library"></a>
## Library
'''
    return zh, en


class TimeFirstContractTest(unittest.TestCase):
    def test_repository_readmes_satisfy_contract(self):
        errors = validate_pair(
            (ROOT / "README.md").read_text(encoding="utf-8"),
            (ROOT / "README.en.md").read_text(encoding="utf-8"),
        )
        self.assertEqual([], errors)

    def test_contract_does_not_impose_a_fixed_latest_cap(self):
        zh, en = make_pair(11)
        self.assertEqual([], validate_pair(zh, en))

    def test_domain_pair_without_benchmark_aliases_is_valid(self):
        zh, en = make_pair(1)
        self.assertEqual([], validate_pair(zh, en))

    def test_missing_common_anchor_is_rejected(self):
        zh, en = make_pair(1)
        zh = zh.replace('<a id="library"></a>', "", 1)
        self.assertTrue(
            any("missing stable anchor library" in error.lower() for error in validate_pair(zh, en))
        )

    def test_duplicate_common_anchor_is_rejected(self):
        zh, en = make_pair(1)
        zh = zh.replace(
            '<a id="timeline"></a>',
            '<a id="timeline"></a><a id="timeline"></a>',
            1,
        )
        self.assertTrue(
            any("duplicate stable anchor timeline" in error.lower() for error in validate_pair(zh, en))
        )

    def test_html_commented_common_anchor_does_not_satisfy_required_anchor(self):
        for anchor in (
            "timeline",
            "latest",
            "periods",
            "last-7-days",
            "last-30-days",
            "field-map",
            "reading-paths",
            "library",
        ):
            with self.subTest(anchor=anchor):
                zh, en = make_pair(1)
                marker = f'<a id="{anchor}"></a>'
                zh = zh.replace(marker, f"<!-- {marker} -->", 1)
                self.assertTrue(
                    any(
                        f"missing stable anchor {anchor}" in error.lower()
                        for error in validate_pair(zh, en)
                    )
                )

    def test_hidden_anchor_decoy_does_not_duplicate_legitimate_visible_anchor(self):
        for anchor in (
            "timeline",
            "latest",
            "periods",
            "last-7-days",
            "last-30-days",
            "field-map",
            "reading-paths",
            "library",
        ):
            with self.subTest(anchor=anchor):
                zh, en = make_pair(1)
                marker = f'<a id="{anchor}"></a>'
                zh = zh.replace(marker, f"<!-- {marker} -->{marker}", 1)
                self.assertEqual([], validate_pair(zh, en))

    def test_language_identity_or_date_order_drift_is_rejected(self):
        zh, en = make_pair(2)
        en = en.replace("entry-work-1", "entry-wrong-work", 1)
        self.assertTrue(
            any("identity" in error.lower() for error in validate_pair(zh, en))
        )

    def test_title_area_and_delta_semantic_drift_is_rejected(self):
        mutations = (
            ("Work 1", "Wrong Work", "title"),
            ("timefirst:area=area-problem-1", "timefirst:area=other-area", "area/problem"),
            ("timefirst:delta=delta-1", "timefirst:delta=other-delta", "delta"),
        )
        for old, new, expected in mutations:
            with self.subTest(expected=expected):
                zh, en = make_pair(1)
                en = en.replace(old, new, 1)
                self.assertTrue(
                    any(expected in error.lower() for error in validate_pair(zh, en))
                )

    def test_evidence_and_caveat_scope_drift_is_rejected(self):
        mutations = (
            ("timefirst:evidence=evidence-1", "timefirst:evidence=other-evidence", "evidence"),
            ("timefirst:caveat=caveat-1", "timefirst:caveat=other-caveat", "caveat"),
        )
        for old, new, expected in mutations:
            with self.subTest(expected=expected):
                zh, en = make_pair(1)
                en = en.replace(old, new, 1)
                self.assertTrue(
                    any(expected in error.lower() for error in validate_pair(zh, en))
                )

    def test_visible_evidence_and_caveat_must_carry_contract_witness(self):
        mutations = (
            ("retrieval coverage ablation", "unrelated result", "evidence"),
            ("ingestion latency overhead", "unrelated caveat", "caveat"),
        )
        for old, new, expected in mutations:
            with self.subTest(expected=expected):
                zh, en = make_pair(1)
                en = en.replace(old, new, 1)
                self.assertTrue(
                    any(expected in error.lower() for error in validate_pair(zh, en))
                )

    def test_witness_requires_a_distinctive_phrase(self):
        mutations = (
            (
                "timefirst:evidence=evidence-1~retrieval-coverage-ablation",
                "timefirst:evidence=evidence-1~100",
                "retrieval coverage ablation",
                "unrelated result 100",
                "evidence",
            ),
            (
                "timefirst:caveat=caveat-1~ingestion-latency-overhead",
                "timefirst:caveat=caveat-1~strongest-caveat",
                "ingestion latency overhead",
                "strongest caveat",
                "caveat",
            ),
        )
        for old_contract, new_contract, old_visible, new_visible, expected in mutations:
            with self.subTest(expected=expected):
                zh, en = make_pair(1)
                zh = zh.replace(old_contract, new_contract, 1).replace(
                    old_visible, new_visible, 1
                )
                en = en.replace(old_contract, new_contract, 1).replace(
                    old_visible, new_visible, 1
                )
                self.assertTrue(
                    any(
                        f"{expected} semantic contract needs a distinctive" in error.lower()
                        for error in validate_pair(zh, en)
                    )
                )

    def test_generic_contract_boilerplate_is_not_a_distinctive_witness(self):
        zh, en = make_pair(1)
        for old, new in (
            (
                "timefirst:evidence=evidence-1~retrieval-coverage-ablation",
                "timefirst:evidence=evidence-1~same-matched-evidence",
            ),
            ("retrieval coverage ablation", "same matched evidence"),
        ):
            zh = zh.replace(old, new, 1)
            en = en.replace(old, new, 1)

        self.assertTrue(
            any(
                "evidence semantic contract needs a distinctive" in error.lower()
                for error in validate_pair(zh, en)
            )
        )

    def test_witness_must_match_a_bounded_visible_phrase(self):
        zh, en = make_pair(1)
        en = en.replace("retrieval coverage ablation", "preretrieval coverage ablation", 1)
        self.assertTrue(
            any(
                "visible evidence does not carry contract witness" in error.lower()
                for error in validate_pair(zh, en)
            )
        )

    def test_primary_and_local_link_drift_is_rejected(self):
        mutations = (
            ("https://example.com/work-1", "https://example.com/wrong", "link"),
            ("notes/work-1.en.md", "notes/wrong.en.md", "link"),
        )
        for old, new, expected in mutations:
            with self.subTest(old=old):
                zh, en = make_pair(1)
                en = en.replace(old, new, 1)
                self.assertTrue(
                    any(expected in error.lower() for error in validate_pair(zh, en))
                )

    def test_empty_labeled_field_is_rejected(self):
        zh, en = make_pair(1)
        zh = zh.replace("**证据。** retrieval coverage ablation", "**证据。**")
        self.assertTrue(any("evidence" in error.lower() for error in validate_pair(zh, en)))

    def test_whitespace_only_link_target_is_rejected(self):
        zh, en = make_pair(1)
        zh = zh.replace("https://example.com/work-1", " ", 1)
        self.assertTrue(any("link" in error.lower() for error in validate_pair(zh, en)))

    def test_html_comments_cannot_mask_visible_link_drift(self):
        zh, en = make_pair(1)
        zh = zh.replace(
            "**链接。** [Primary](https://example.com/work-1)",
            "**链接。** <!-- [Hidden](https://example.com/wrong) --> "
            "[Primary](https://example.com/work-1)",
            1,
        )
        en = en.replace(
            "**Links.** [Primary](https://example.com/work-1)",
            "**Links.** [Primary](https://example.com/wrong) "
            "<!-- [Hidden](https://example.com/work-1) -->",
            1,
        )
        self.assertTrue(
            any("link" in error.lower() for error in validate_pair(zh, en))
        )

    def test_html_comments_cannot_override_a_visible_map_token(self):
        zh, en = make_pair(1)
        en = en.replace(
            "**Map.** `early_signal`",
            "**Map.** <!-- `early_signal` --> `none`",
            1,
        )
        self.assertTrue(
            any("map token" in error.lower() for error in validate_pair(zh, en))
        )

    def test_html_commented_field_label_cannot_launder_a_hidden_field(self):
        zh, en = make_pair(1)
        zh = zh.replace(
            "**证据。** retrieval coverage ablation "
            "<!-- timefirst:evidence=evidence-1~retrieval-coverage-ablation -->",
            "<!-- **证据。** retrieval coverage ablation --> "
            "<!-- timefirst:evidence=evidence-1~retrieval-coverage-ablation -->",
            1,
        )
        en = en.replace(
            "**Evidence.** retrieval coverage ablation "
            "<!-- timefirst:evidence=evidence-1~retrieval-coverage-ablation -->",
            "<!-- **Evidence.** retrieval coverage ablation --> "
            "<!-- timefirst:evidence=evidence-1~retrieval-coverage-ablation -->",
            1,
        )

        self.assertTrue(
            any("missing evidence" in error.lower() for error in validate_pair(zh, en))
        )

    def test_missing_evidence_or_caveat_is_rejected(self):
        zh, en = make_pair(1)
        zh = zh.replace("**证据。** retrieval coverage ablation", "")
        self.assertTrue(
            any("evidence" in error.lower() for error in validate_pair(zh, en))
        )

    def test_period_window_drift_is_rejected(self):
        mutations = (
            ("2026-08-14—2026-08-20", "2026-08-13—2026-08-20", "last-7-days"),
            ("2026-07-22—2026-08-20", "2026-07-21—2026-08-20", "last-30-days"),
        )
        for old, new, expected in mutations:
            with self.subTest(expected=expected):
                zh, en = make_pair(1)
                en = en.replace(old, new, 1)
                self.assertTrue(
                    any(
                        expected in error.lower() and "window" in error.lower()
                        for error in validate_pair(zh, en)
                    )
                )

    def test_period_windows_have_exact_inclusive_cardinality(self):
        zh, en = make_pair(1)
        zh = zh.replace("2026-08-14—2026-08-20", "2026-08-13—2026-08-20", 1)
        en = en.replace("2026-08-14—2026-08-20", "2026-08-13—2026-08-20", 1)
        self.assertTrue(
            any("exactly 7 inclusive days" in error for error in validate_pair(zh, en))
        )

    def test_period_windows_share_one_synthesis_endpoint(self):
        zh, en = make_pair(1)
        zh = zh.replace("2026-08-14—2026-08-20", "2026-08-13—2026-08-19", 1)
        en = en.replace("2026-08-14—2026-08-20", "2026-08-13—2026-08-19", 1)
        self.assertTrue(
            any("same synthesis endpoint" in error for error in validate_pair(zh, en))
        )

    def test_each_period_section_requires_exactly_one_visible_date_range(self):
        fixtures = (
            (
                "last-7-days",
                "2026-08-14—2026-08-20",
                "2026-08-13—2026-08-19",
            ),
            (
                "last-30-days",
                "2026-07-22—2026-08-20",
                "2026-07-21—2026-08-19",
            ),
        )
        for anchor, correct, contradictory in fixtures:
            for mutation, replacement in (
                ("zero", ""),
                ("duplicate", f"{correct}\n\n{contradictory}"),
            ):
                with self.subTest(anchor=anchor, mutation=mutation):
                    zh, en = make_pair(1)
                    zh = zh.replace(correct, replacement, 1)
                    en = en.replace(correct, replacement, 1)
                    self.assertTrue(
                        any(
                            anchor in error
                            and "exactly one visible date range" in error
                            for error in validate_pair(zh, en)
                        )
                    )


if __name__ == "__main__":
    unittest.main()
