from copy import deepcopy
from datetime import datetime
import json
from pathlib import Path
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_reading


V2_FIELDS = (
    "published_at",
    "first_seen_at",
    "radar_published_at",
    "time_provenance",
    "map_delta",
)


def repository_inputs() -> tuple[str, str, list[dict[str, object]]]:
    return (
        (ROOT / "README.md").read_text(encoding="utf-8"),
        (ROOT / "README.en.md").read_text(encoding="utf-8"),
        json.loads((ROOT / "data" / "benchmarks.json").read_text(encoding="utf-8")),
    )


def shift_period_windows_one_day_earlier(text: str) -> str:
    return text.replace(
        "2026-08-15—2026-08-21", "2026-08-14—2026-08-20", 1
    ).replace(
        "2026-07-23—2026-08-21", "2026-07-22—2026-08-20", 1
    )


def native_record(
    identity: str,
    radar_published_at: str,
    *,
    map_delta: str = "early_signal",
    direction_keys: tuple[str, ...] = ("benchmark-acceptance-time",),
) -> dict[str, object]:
    radar_date = radar_published_at[:10]
    return {
        "id": identity,
        "name": identity.upper(),
        "released": "2026-08",
        "published_at": "2026-08-01T00:00:00Z",
        "first_seen_at": f"{radar_date}T00:00:00Z",
        "radar_published_at": radar_published_at,
        "time_provenance": "native_v2",
        "map_delta": map_delta,
        "direction_keys": list(direction_keys),
        "artifacts": {"paper": f"https://example.com/{identity}"},
    }


def insert_timeline_entry(
    text: str,
    record: dict[str, object],
) -> str:
    identity = str(record["id"])
    title = str(record["name"])
    displayed_date = str(record["radar_published_at"])[:10]
    map_delta = str(record["map_delta"])
    primary = str(record["artifacts"]["paper"])
    entry = f'''<a id="entry-{identity}"></a>
<details><summary>{displayed_date} · {title} · Synthetic area — Synthetic delta</summary>

**Map.** `{map_delta}`

**Links.** [Paper]({primary})

</details>

'''
    _, _, canonical = repository_inputs()
    native = [
        candidate
        for candidate in canonical + [record]
        if candidate.get("time_provenance") == "native_v2"
    ]
    native.sort(
        key=lambda candidate: (
            -datetime.fromisoformat(
                str(candidate["radar_published_at"]).replace("Z", "+00:00")
            ).timestamp(),
            str(candidate["id"]),
        )
    )
    position = next(index for index, candidate in enumerate(native) if candidate["id"] == identity)
    marker = (
        f'<a id="entry-{native[position + 1]["id"]}"></a>'
        if position + 1 < len(native)
        else '<a id="entry-dsagentbench"></a>'
    )
    return text.replace(marker, entry + marker, 1)


def direction_line(
    language: str,
    *,
    key: str = "benchmark-acceptance-time",
    state: str = "no_material_change",
    supports: tuple[str, ...] = (),
    confidence: str = "high",
    implication: str = "require-native-v2-times-for-period-claims",
    timing: str = "radar_published_at",
    synthesized: str = "2026-08-21T00:48:57Z",
    prior: str = "none",
    visible_supports: tuple[str, ...] | None = None,
) -> str:
    support_value = ",".join(supports) if supports else "none"
    visible_supports = supports if visible_supports is None else visible_supports
    if visible_supports:
        support_links = " · ".join(
            f"[{identity.upper()}](#entry-{identity})" for identity in visible_supports
        )
    else:
        support_links = "**none**"
    prior_visible = "`none`" if prior == "none" else f"[Field Map](#{prior})"
    heading_witness = key.replace("-", " ")
    metadata = (
        f'<!-- timefirst:direction key="{key}" '
        f'state="{state}" supports="{support_value}" confidence="{confidence}" '
        f'implication="{implication}" timing="{timing}" '
        f'synthesized="{synthesized}" prior="{prior}" -->'
    )
    if language == "zh":
        return (
            f"- **`{state}` · {heading_witness}：本窗口的可辩护方向判断。** "
            f"{metadata} 支撑：{support_links}；置信度：**{confidence}**；"
            f"时间依据：`{timing}`；先验地图证据：{prior_visible}。"
            f"研究设计含义（{implication.replace('-', ' ')}）："
            "只有可审计的原生 Radar 接受时间才能支持窗口判断。"
            f"精确合成时间：`{synthesized}`（UTC）。"
        )
    return (
        f"- **`{state}` · {heading_witness}: the defensible direction judgment "
        f"for this window.** {metadata} Supports: {support_links}; confidence: "
        f"**{confidence}**; timing basis: `{timing}`; prior map evidence: "
        f"{prior_visible}. Research-design implication ({implication.replace('-', ' ')}): "
        "only auditable native Radar acceptance times support the window. "
        f"Exact synthesis time: `{synthesized}` (UTC)."
    )


def replace_period_direction(
    text: str,
    language: str,
    line: str,
    *,
    anchor: str = "last-7-days",
) -> str:
    next_anchor = "last-30-days" if anchor == "last-7-days" else "evolution"
    start = text.index(f'<a id="{anchor}"></a>')
    end = text.index(f'<a id="{next_anchor}"></a>', start)
    section = text[start:end]
    direction_start = section.index("\n- ") + 1
    absolute_start = start + direction_start
    return text[:absolute_start] + line.rstrip() + "\n\n" + text[end:]


def multiline_direction_line(language: str) -> str:
    line = direction_line(language)
    field_marker = " 支撑：" if language == "zh" else " Supports:"
    heading, continuation = line.split(field_marker, 1)
    label = "支撑：" if language == "zh" else "Supports:"
    return f"{heading}\n  {label}{continuation}"


def set_first_period_direction(
    text: str,
    *,
    state: str,
    supports: tuple[str, ...],
    prior: str = "none",
) -> str:
    language = "en" if "What Changed in the Evaluation Object" in text else "zh"
    return replace_period_direction(
        text,
        language,
        direction_line(language, state=state, supports=supports, prior=prior),
    )


class CanonicalBenchmarkTimeContractTest(unittest.TestCase):
    def test_repository_registry_satisfies_v2_contract(self):
        _, _, records = repository_inputs()
        self.assertEqual([], validate_reading.validate_benchmark_registry(records))

    def test_untouched_legacy_record_remains_field_absent_compatible(self):
        record = {"id": "untouched", "released": "2024-08"}
        self.assertEqual([], validate_reading.validate_record_time_contract(record))

    def test_any_v2_field_requires_the_complete_contract(self):
        record = {"id": "partial", "released": "2026-08", "map_delta": "early_signal"}
        errors = validate_reading.validate_record_time_contract(record)
        for field in set(V2_FIELDS) - {"map_delta"}:
            self.assertTrue(any(field in error for error in errors), (field, errors))

    def test_native_v2_requires_strict_utc_timestamps_and_event_order(self):
        record = native_record("native", "2026-08-20T01:00:00Z")
        for field, value in (
            ("published_at", "2026-08-01T00:00:00+00:00"),
            ("first_seen_at", "2026-08-20T00:00Z"),
            ("radar_published_at", "2026-08-20 01:00:00Z"),
        ):
            with self.subTest(field=field):
                mutated = deepcopy(record)
                mutated[field] = value
                self.assertTrue(
                    any("strict UTC" in error for error in validate_reading.validate_record_time_contract(mutated))
                )

        record["published_at"] = "2026-08-21T00:00:00Z"
        self.assertTrue(
            any(
                "published_at <= first_seen_at <= radar_published_at" in error
                for error in validate_reading.validate_record_time_contract(record)
            )
        )

    def test_native_direction_keys_are_unique_stable_tokens_when_declared(self):
        record = native_record("native", "2026-08-21T00:48:57Z")
        mutations = (
            ("not-a-list", "benchmark-acceptance-time"),
            ("empty", []),
            ("duplicate", ["benchmark-acceptance-time", "benchmark-acceptance-time"]),
            ("free-form", ["Benchmark acceptance time"]),
        )
        for name, value in mutations:
            with self.subTest(name=name):
                mutated = deepcopy(record)
                mutated["direction_keys"] = value
                errors = validate_reading.validate_record_time_contract(mutated)
                self.assertTrue(any("direction_keys" in error for error in errors), errors)

    def test_explicit_legacy_forbids_fabricated_discovery_or_radar_time(self):
        record = {
            "id": "legacy",
            "released": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": "2026-08-21T00:48:57Z",
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "early_signal",
        }
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(any("first_seen_at=null" in error for error in errors), errors)

        record["first_seen_at"] = None
        record["radar_published_at"] = "2026-08-20T01:00:00Z"
        errors = validate_reading.validate_record_time_contract(record)
        self.assertTrue(any("radar_published_at=null" in error for error in errors), errors)

    def test_explicit_legacy_preserves_honest_released_precision(self):
        month = {
            "id": "legacy",
            "released": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": None,
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "early_signal",
        }
        self.assertEqual([], validate_reading.validate_record_time_contract(month))

        day = deepcopy(month)
        day.update(released="2026-08-17", published_at="2026-08-17")
        self.assertEqual([], validate_reading.validate_record_time_contract(day))

        fabricated = deepcopy(month)
        fabricated["published_at"] = "2026-08-01"
        self.assertTrue(
            any("released precision" in error for error in validate_reading.validate_record_time_contract(fabricated))
        )

    def test_invalid_map_delta_is_rejected_for_native_and_explicit_legacy(self):
        native = native_record("native", "2026-08-20T01:00:00Z", map_delta="trend")
        legacy = {
            "id": "legacy",
            "released": "2026-08",
            "published_at": "2026-08",
            "first_seen_at": None,
            "radar_published_at": None,
            "time_provenance": "legacy_unknown",
            "map_delta": "trend",
        }
        for record in (native, legacy):
            with self.subTest(provenance=record["time_provenance"]):
                self.assertTrue(
                    any("map_delta" in error for error in validate_reading.validate_record_time_contract(record))
                )

    def test_only_fixed_timeline_records_are_explicitly_migrated(self):
        _, _, records = repository_inputs()
        migrated = {
            str(record["id"])
            for record in records
            if record.get("time_provenance") == "legacy_unknown"
        }
        self.assertEqual(set(validate_reading.LEGACY_TIMELINE_COMPATIBILITY_IDS), migrated)
        for record in records:
            if record["id"] in migrated:
                self.assertEqual(record["released"], record["published_at"])
                self.assertIsNone(record["first_seen_at"])
                self.assertIsNone(record["radar_published_at"])
                self.assertEqual("early_signal", record["map_delta"])
            elif record.get("time_provenance") != "native_v2":
                self.assertFalse(any(field in record for field in V2_FIELDS), record["id"])


class TimelineProjectionContractTest(unittest.TestCase):
    def test_repository_projection_is_complete_and_canonical(self):
        zh, en, records = repository_inputs()
        self.assertEqual([], validate_reading.validate_benchmark_projection(zh, en, records))

    def test_in_window_native_record_cannot_be_omitted(self):
        zh, en, records = repository_inputs()
        records.append(native_record("native-missing", "2026-08-21T00:48:57Z"))
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("native-missing" in error and "missing from Timeline" in error for error in errors), errors)

    def test_unexpected_timeline_identity_is_rejected(self):
        zh, en, records = repository_inputs()
        unexpected = native_record("not-canonical", "2026-08-20T03:00:00Z")
        zh = insert_timeline_entry(zh, unexpected)
        en = insert_timeline_entry(en, unexpected)
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("not-canonical" in error and "unexpected" in error for error in errors), errors)

    def test_same_day_native_records_use_full_timestamp_order(self):
        zh, en, records = repository_inputs()
        earlier = native_record("native-earlier", "2026-08-19T01:00:00Z")
        later = native_record("native-later", "2026-08-19T02:00:00Z")
        records.extend((earlier, later))
        for record in (earlier, later):
            zh = insert_timeline_entry(zh, record)
            en = insert_timeline_entry(en, record)
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("full Radar timestamp order" in error for error in errors), errors)

    def test_native_timeline_rejects_acceptance_after_public_synthesis_cutoff(self):
        zh, en, records = repository_inputs()
        record = native_record("native-after-cutoff", "2026-08-21T00:48:58Z")
        records.append(record)
        zh = insert_timeline_entry(zh, record)
        en = insert_timeline_entry(en, record)

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(
            any(
                "native-after-cutoff" in error
                and "Timeline" in error
                and "synthesis cutoff" in error
                for error in errors
            ),
            errors,
        )

    def test_visible_title_date_map_and_primary_link_match_canonical_record(self):
        mutations = (
            ("DSAgentBench ·", "Wrong Title ·", "title"),
            ("2026-08 · DSAgentBench", "2026-08-01 · DSAgentBench", "displayed date"),
            ("**地图。** `early_signal`", "**地图。** `none`", "map_delta"),
            ("https://arxiv.org/abs/2608.10366", "https://example.com/wrong", "primary"),
        )
        for old, new, expected in mutations:
            with self.subTest(expected=expected):
                zh, en, records = repository_inputs()
                if expected == "primary":
                    zh_head, zh_tail = zh.split('<a id="timeline"></a>', 1)
                    en_head, en_tail = en.split('<a id="timeline"></a>', 1)
                    zh = zh_head + '<a id="timeline"></a>' + zh_tail.replace(old, new, 1)
                else:
                    zh = zh.replace(old, new, 1)
                english_old = old.replace("**地图。**", "**Map.**")
                english_new = new.replace("**地图。**", "**Map.**")
                if expected == "primary":
                    en = en_head + '<a id="timeline"></a>' + en_tail.replace(
                        english_old, english_new, 1
                    )
                else:
                    en = en.replace(english_old, english_new, 1)
                errors = validate_reading.validate_benchmark_projection(zh, en, records)
                self.assertTrue(any(expected in error for error in errors), errors)

    def test_existing_local_note_link_must_match_identity_and_language(self):
        zh, en, records = repository_inputs()
        zh = zh.replace("benchmarks/dsagentbench.md", "benchmarks/vakra.md", 1)
        en = en.replace("benchmarks/dsagentbench.en.md", "benchmarks/vakra.en.md", 1)
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("dsagentbench" in error and "local note" in error for error in errors), errors)

    def test_hidden_canonical_link_cannot_rescue_a_wrong_visible_link(self):
        zh, en, records = repository_inputs()
        zh = zh.replace(
            "**链接。** [论文](https://arxiv.org/abs/2608.10366) · "
            "[本地深度笔记](benchmarks/dsagentbench.md)",
            "**链接。** [论文](https://example.com/wrong) · "
            "[本地深度笔记](benchmarks/dsagentbench.md) "
            "<!-- [Hidden](https://arxiv.org/abs/2608.10366) -->",
            1,
        )
        en = en.replace(
            "**Links.** [Paper](https://arxiv.org/abs/2608.10366) · "
            "[Local deep note](benchmarks/dsagentbench.en.md)",
            "**Links.** [Paper](https://example.com/wrong) · "
            "[Local deep note](benchmarks/dsagentbench.en.md) "
            "<!-- [Hidden](https://arxiv.org/abs/2608.10366) -->",
            1,
        )
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(
            any("dsagentbench" in error and "primary" in error for error in errors),
            errors,
        )

    def test_hidden_map_token_cannot_override_the_visible_map(self):
        zh, en, records = repository_inputs()
        zh = zh.replace(
            "**地图。** `early_signal`",
            "**地图。** <!-- `early_signal` --> `none`",
            1,
        )
        en = en.replace(
            "**Map.** `early_signal`",
            "**Map.** <!-- `early_signal` --> `none`",
            1,
        )
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(
            any("map_delta" in error for error in errors),
            errors,
        )


class PeriodDirectionContractTest(unittest.TestCase):
    def test_repository_periods_are_parseable_bound_directions(self):
        zh, en, records = repository_inputs()
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertFalse(any("direction" in error.lower() for error in errors), errors)
        for text in (zh, en):
            self.assertEqual(0, text.count('state="no_material_change"'))
            self.assertEqual(0, text.count('supports="none"'))
            self.assertEqual(8, text.count('timing="radar_published_at"'))
            self.assertEqual(
                8, text.count('synthesized="2026-08-21T00:48:57Z"')
            )
            self.assertEqual(4, text.count('prior="none"'))
            self.assertEqual(4, text.count('prior="field-map"'))
            self.assertEqual(16, text.count("2026-08-21T00:48:57Z"))

    def test_direction_requires_complete_stable_metadata(self):
        zh, en, records = repository_inputs()
        zh = zh.replace(' timing="radar_published_at"', "", 1)
        en = en.replace(' timing="radar_published_at"', "", 1)
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("timing" in error for error in errors), errors)

    def test_direction_requires_all_visible_fields_once_and_scoped(self):
        zh, en, records = repository_inputs()
        fixtures = (
            (
                "missing",
                direction_line("en").replace("confidence: **high**; ", "", 1),
            ),
            (
                "duplicate-aside",
                direction_line("en") + " Aside: confidence: **high**;",
            ),
        )
        for name, line in fixtures:
            with self.subTest(name=name):
                mutated_en = replace_period_direction(en, "en", line)
                errors = validate_reading.validate_benchmark_projection(
                    zh, mutated_en, records
                )
                self.assertTrue(
                    any("exactly one visible confidence field" in error for error in errors),
                    errors,
                )

    def test_duplicate_visible_direction_fields_cannot_be_laundered_as_asides(self):
        zh, en, records = repository_inputs()
        duplicate_fields = {
            "state": " Aside: **`no_material_change` · contradictory state.**",
            "supports": " Aside: Supports: **none**;",
            "confidence": " Aside: confidence: **high**;",
            "timing basis": " Aside: timing basis: `radar_published_at`;",
            "synthesis": (
                " Aside: Exact synthesis time: `2026-08-21T00:48:57Z` (UTC)."
            ),
            "implication": (
                " Aside: Research-design implication "
                "(require native v2 times for period claims): duplicate."
            ),
            "prior": " Aside: prior map evidence: `none`.",
        }
        for field, aside in duplicate_fields.items():
            with self.subTest(field=field):
                line = direction_line("en") + aside
                mutated_en = replace_period_direction(en, "en", line)
                errors = validate_reading.validate_benchmark_projection(
                    zh, mutated_en, records
                )
                self.assertTrue(
                    any(f"exactly one visible {field} field" in error for error in errors),
                    errors,
                )

    def test_visible_confidence_must_match_metadata_and_language_pair(self):
        zh, en, records = repository_inputs()
        drifted = direction_line("en").replace(
            "confidence: **high**", "confidence: **low**", 1
        )
        en = replace_period_direction(en, "en", drifted)

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(any("visible confidence" in error for error in errors), errors)

    def test_direction_metadata_must_be_owned_by_one_visible_block(self):
        zh, en, records = repository_inputs()
        orphan = (
            '<!-- timefirst:direction key="orphan-direction" '
            'state="no_material_change" supports="none" confidence="high" '
            'implication="require-native-v2-times-for-period-claims" '
            'timing="radar_published_at" synthesized="2026-08-21T00:48:57Z" '
            'prior="none" -->\n'
        )
        marker = "### Last 7 days: 2026-08-15—2026-08-21\n\n"
        en = en.replace(marker, marker + orphan, 1)

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(any("orphan direction metadata" in error for error in errors), errors)

    def test_true_duplicate_direction_metadata_is_rejected(self):
        zh, en, records = repository_inputs()
        line = direction_line("en")
        metadata = line[line.index("<!-- timefirst:direction") : line.index("-->") + 3]
        en = replace_period_direction(en, "en", f"{line}\n  {metadata}")

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(
            any("exactly one stable direction metadata block" in error for error in errors),
            errors,
        )

    def test_natural_multiline_direction_fields_remain_in_one_block(self):
        zh, en, records = repository_inputs()
        zh = replace_period_direction(zh, "zh", multiline_direction_line("zh"))
        en = replace_period_direction(en, "en", multiline_direction_line("en"))

        self.assertEqual(
            [], validate_reading.validate_benchmark_projection(zh, en, records)
        )

    def test_trailing_direction_metadata_stays_owned_by_multiline_block(self):
        zh, en, records = repository_inputs()
        lines: dict[str, str] = {}
        for language in ("zh", "en"):
            line = multiline_direction_line(language)
            start = line.index("<!-- timefirst:direction")
            end = line.index("-->", start) + 3
            metadata = line[start:end]
            lines[language] = (line[:start] + line[end:]).rstrip() + f"\n  {metadata}"
        zh = replace_period_direction(zh, "zh", lines["zh"])
        en = replace_period_direction(en, "en", lines["en"])

        self.assertEqual(
            [], validate_reading.validate_benchmark_projection(zh, en, records)
        )

    def test_inline_emphasis_cannot_split_direction_labels(self):
        zh, en, records = repository_inputs()
        zh_line = direction_line("zh").replace(
            "置信度：**high**", "置**信**度：**high**", 1
        )
        en_line = direction_line("en").replace(
            "confidence: **high**", "confi**dence**: **high**", 1
        )
        zh = replace_period_direction(zh, "zh", zh_line)
        en = replace_period_direction(en, "en", en_line)

        self.assertEqual(
            [], validate_reading.validate_benchmark_projection(zh, en, records)
        )

    def test_rendered_field_labels_survive_code_entities_and_html_tags(self):
        zh, en, records = repository_inputs()
        fixtures = (
            (
                "inline-code",
                direction_line("zh").replace("置信度：", "置信`度`：", 1),
                direction_line("en").replace("confidence:", "confi`dence`:", 1),
            ),
            (
                "entity",
                direction_line("zh").replace("置信度：", "置信&#24230;：", 1),
                direction_line("en").replace("confidence:", "confi&#100;ence:", 1),
            ),
            (
                "html",
                direction_line("zh").replace("置信度：", "置信<em>度</em>：", 1),
                direction_line("en").replace(
                    "confidence:", "confi<em>dence</em>:", 1
                ),
            ),
        )
        for name, zh_line, en_line in fixtures:
            with self.subTest(name=name):
                case_zh = replace_period_direction(zh, "zh", zh_line)
                case_en = replace_period_direction(en, "en", en_line)
                self.assertEqual(
                    [],
                    validate_reading.validate_benchmark_projection(
                        case_zh, case_en, records
                    ),
                )

    def test_link_split_duplicate_fields_are_counted_in_rendered_text(self):
        zh, en, records = repository_inputs()
        fixtures = (
            (
                "zh",
                direction_line("zh")
                + " 旁注：[置信](https://example.com/not-visible \"持久趋势\")度：**high**；",
            ),
            (
                "en",
                direction_line("en")
                + " Aside: confi[dence](https://example.com/not-visible \"durable trend\"): **high**;",
            ),
        )
        for language, line in fixtures:
            with self.subTest(language=language):
                case_zh = (
                    replace_period_direction(zh, "zh", line)
                    if language == "zh"
                    else zh
                )
                case_en = (
                    replace_period_direction(en, "en", line)
                    if language == "en"
                    else en
                )
                errors = validate_reading.validate_benchmark_projection(
                    case_zh, case_en, records
                )
                self.assertTrue(
                    any(
                        "exactly one visible confidence field" in error
                        for error in errors
                    ),
                    errors,
                )

    def test_entity_split_low_support_durable_claims_are_rejected(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z")
        records.append(record)
        base_zh = direction_line(
            "zh", state="new_signal", supports=("native-one",)
        )
        base_en = direction_line(
            "en", state="new_signal", supports=("native-one",)
        )
        fixtures = (
            ("zh", base_zh + "\n  这个续行宣称已形成趋&#21183;。"),
            ("en", base_en + "\n  This continuation calls it dura&#98;le."),
        )
        for language, line in fixtures:
            with self.subTest(language=language):
                case_zh = insert_timeline_entry(zh, record)
                case_en = insert_timeline_entry(en, record)
                if language == "zh":
                    case_zh = replace_period_direction(case_zh, "zh", line)
                    case_en = replace_period_direction(case_en, "en", base_en)
                else:
                    case_zh = replace_period_direction(case_zh, "zh", base_zh)
                    case_en = replace_period_direction(case_en, "en", line)
                errors = validate_reading.validate_benchmark_projection(
                    case_zh, case_en, records
                )
                self.assertTrue(
                    any("fewer than two distinct supports" in error for error in errors),
                    errors,
                )

    def test_link_destinations_and_titles_do_not_make_visible_durable_claims(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z")
        records.append(record)
        zh_line = direction_line(
            "zh", state="new_signal", supports=("native-one",)
        ) + ' [补充材料](https://example.com/durable-trend "持久趋势")'
        en_line = direction_line(
            "en", state="new_signal", supports=("native-one",)
        ) + ' [Background](https://example.com/durable-trend "durable trend")'
        zh = replace_period_direction(insert_timeline_entry(zh, record), "zh", zh_line)
        en = replace_period_direction(insert_timeline_entry(en, record), "en", en_line)

        self.assertEqual(
            [], validate_reading.validate_benchmark_projection(zh, en, records)
        )

    def test_post_synthesis_native_record_cannot_support_a_direction(self):
        zh, en, records = repository_inputs()
        record = native_record("native-after-cutoff", "2026-08-21T00:48:58Z")
        records.append(record)
        zh = set_first_period_direction(
            insert_timeline_entry(zh, record),
            state="new_signal",
            supports=("native-after-cutoff",),
        )
        en = set_first_period_direction(
            insert_timeline_entry(en, record),
            state="new_signal",
            supports=("native-after-cutoff",),
        )

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(
            any(
                "native-after-cutoff" in error
                and "accepted after direction synthesized" in error
                for error in errors
            ),
            errors,
        )

    def test_every_visible_direction_requires_stable_metadata(self):
        zh, en, records = repository_inputs()
        marker = '<a id="last-30-days"></a>'
        zh = zh.replace(
            marker,
            "- **`new_signal` · 未标注的方向。**\n\n" + marker,
            1,
        )
        en = en.replace(
            marker,
            "- **`new_signal` · Unannotated direction.**\n\n" + marker,
            1,
        )
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("stable direction metadata" in error for error in errors), errors)

    def test_direction_key_confidence_and_implication_are_stable_tokens(self):
        zh, en, records = repository_inputs()
        for old, new in (
            ('key="structured-evidence-coverage"', 'key="free form"'),
            ('confidence="high"', 'confidence="not stable"'),
            (
                'implication="measure-coverage-not-only-single-hit-relevance"',
                'implication="free form prose"',
            ),
        ):
            with self.subTest(attribute=old.split("=", 1)[0]):
                mutated_zh = zh.replace(old, new, 1)
                mutated_en = en.replace(old, new, 1)
                errors = validate_reading.validate_benchmark_projection(
                    mutated_zh, mutated_en, records
                )
                self.assertTrue(any("stable token" in error for error in errors), errors)

    def test_legacy_context_cannot_count_as_period_support(self):
        zh, en, records = repository_inputs()
        zh = set_first_period_direction(zh, state="new_signal", supports=("dsagentbench",))
        en = set_first_period_direction(en, state="new_signal", supports=("dsagentbench",))
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("dsagentbench" in error and "native_v2" in error for error in errors), errors)

    def test_one_paper_cannot_be_reinforced(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z")
        records.append(record)
        zh = set_first_period_direction(insert_timeline_entry(zh, record), state="reinforced", supports=("native-one",))
        en = set_first_period_direction(insert_timeline_entry(en, record), state="reinforced", supports=("native-one",))
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("reinforced" in error and "two distinct" in error for error in errors), errors)

    def test_new_signal_requires_one_early_signal_record(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z", map_delta="none")
        records.append(record)
        zh = set_first_period_direction(insert_timeline_entry(zh, record), state="new_signal", supports=("native-one",))
        en = set_first_period_direction(insert_timeline_entry(en, record), state="new_signal", supports=("native-one",))
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("new_signal" in error and "early_signal" in error for error in errors), errors)

    def test_revised_direction_requires_support(self):
        zh, en, records = repository_inputs()
        zh = set_first_period_direction(zh, state="revised", supports=())
        en = set_first_period_direction(en, state="revised", supports=())
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("revised" in error and "support" in error for error in errors), errors)

    def test_durable_direction_requires_prior_field_map_evidence(self):
        zh, en, records = repository_inputs()
        first = native_record("native-first", "2026-08-19T02:00:00Z")
        second = native_record(
            "native-second", "2026-08-19T01:00:00Z", map_delta="reinforces"
        )
        records.extend((first, second))
        for record in (first, second):
            zh = insert_timeline_entry(zh, record)
            en = insert_timeline_entry(en, record)
        zh = set_first_period_direction(
            zh,
            state="reinforced",
            supports=("native-first", "native-second"),
        )
        en = set_first_period_direction(
            en,
            state="reinforced",
            supports=("native-first", "native-second"),
        )

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(any("prior" in error and "Field Map" in error for error in errors), errors)

    def test_reinforced_supports_must_share_the_declared_direction_key(self):
        zh, en, records = repository_inputs()
        direction_key = "benchmark-revision-direction"
        revises = native_record(
            "native-revises",
            "2026-08-19T02:00:00Z",
            map_delta="revises",
            direction_keys=(direction_key,),
        )
        retires = native_record(
            "native-retires",
            "2026-08-19T01:00:00Z",
            map_delta="retires",
            direction_keys=("benchmark-retirement-direction",),
        )
        records.extend((revises, retires))
        for record in (revises, retires):
            zh = insert_timeline_entry(zh, record)
            en = insert_timeline_entry(en, record)
        zh = replace_period_direction(
            zh,
            "zh",
            direction_line(
                "zh",
                key=direction_key,
                state="reinforced",
                supports=("native-revises", "native-retires"),
                prior="field-map",
            ),
        )
        en = replace_period_direction(
            en,
            "en",
            direction_line(
                "en",
                key=direction_key,
                state="reinforced",
                supports=("native-revises", "native-retires"),
                prior="field-map",
            ),
        )

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(
            any(
                "native-retires" in error
                and "direction_keys" in error
                and direction_key in error
                for error in errors
            ),
            errors,
        )

    def test_same_direction_reinforcement_with_two_bound_supports_can_pass(self):
        zh, en, records = repository_inputs()
        direction_key = "benchmark-shared-direction"
        first = native_record(
            "native-first",
            "2026-08-19T02:00:00Z",
            direction_keys=(direction_key,),
        )
        second = native_record(
            "native-second",
            "2026-08-19T01:00:00Z",
            map_delta="reinforces",
            direction_keys=(direction_key,),
        )
        records.extend((first, second))
        for record in (first, second):
            zh = insert_timeline_entry(zh, record)
            en = insert_timeline_entry(en, record)
        zh = replace_period_direction(
            zh,
            "zh",
            direction_line(
                "zh",
                key=direction_key,
                state="reinforced",
                supports=("native-first", "native-second"),
                prior="field-map",
            ),
        )
        en = replace_period_direction(
            en,
            "en",
            direction_line(
                "en",
                key=direction_key,
                state="reinforced",
                supports=("native-first", "native-second"),
                prior="field-map",
            ),
        )

        self.assertEqual(
            [], validate_reading.validate_benchmark_projection(zh, en, records)
        )

    def test_revision_split_and_retirement_require_support_and_prior_map(self):
        for state, map_delta in (
            ("revised", "revises"),
            ("splits", "splits"),
            ("retires", "retires"),
        ):
            with self.subTest(state=state):
                zh, en, records = repository_inputs()
                record = native_record(
                    f"native-{state}",
                    "2026-08-21T00:48:57Z",
                    map_delta=map_delta,
                )
                records.append(record)
                zh = set_first_period_direction(
                    insert_timeline_entry(zh, record),
                    state=state,
                    supports=(f"native-{state}",),
                )
                en = set_first_period_direction(
                    insert_timeline_entry(en, record),
                    state=state,
                    supports=(f"native-{state}",),
                )

                errors = validate_reading.validate_benchmark_projection(zh, en, records)

                self.assertTrue(
                    any("prior" in error and "Field Map" in error for error in errors),
                    errors,
                )

    def test_no_material_change_requires_zero_support_and_prior_none(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z")
        records.append(record)
        zh = replace_period_direction(
            insert_timeline_entry(zh, record),
            "zh",
            direction_line(
                "zh",
                supports=("native-one",),
                prior="field-map",
            ),
        )
        en = replace_period_direction(
            insert_timeline_entry(en, record),
            "en",
            direction_line(
                "en",
                supports=("native-one",),
                prior="field-map",
            ),
        )

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(any("no_material_change requires zero" in error for error in errors), errors)
        self.assertTrue(any("no_material_change requires prior=none" in error for error in errors), errors)

    def test_low_support_durable_claim_in_continuation_is_rejected(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z")
        records.append(record)
        zh_line = direction_line(
            "zh", state="new_signal", supports=("native-one",)
        ) + "\n  这个续行宣称已形成持久趋势。"
        en_line = direction_line(
            "en", state="new_signal", supports=("native-one",)
        ) + "\n  This continuation calls the result an established durable trend."
        zh = replace_period_direction(insert_timeline_entry(zh, record), "zh", zh_line)
        en = replace_period_direction(insert_timeline_entry(en, record), "en", en_line)

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(any("fewer than two distinct supports" in error for error in errors), errors)

    def test_url_only_durable_keyword_is_not_a_visible_claim(self):
        zh, en, records = repository_inputs()
        record = native_record("native-one", "2026-08-21T00:48:57Z")
        records.append(record)
        zh_line = direction_line(
            "zh", state="new_signal", supports=("native-one",)
        ) + " [补充材料](https://example.com/durable-trend)"
        en_line = direction_line(
            "en", state="new_signal", supports=("native-one",)
        ) + " [Background](https://example.com/durable-trend)"
        zh = replace_period_direction(insert_timeline_entry(zh, record), "zh", zh_line)
        en = replace_period_direction(insert_timeline_entry(en, record), "en", en_line)

        self.assertEqual(
            [], validate_reading.validate_benchmark_projection(zh, en, records)
        )

    def test_support_membership_uses_radar_time_not_release_time(self):
        zh, en, records = repository_inputs()
        record = native_record("native-old-radar", "2026-08-01T01:00:00Z")
        records.append(record)
        zh = set_first_period_direction(insert_timeline_entry(zh, record), state="new_signal", supports=("native-old-radar",))
        en = set_first_period_direction(insert_timeline_entry(en, record), state="new_signal", supports=("native-old-radar",))
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("native-old-radar" in error and "outside" in error for error in errors), errors)

    def test_direction_metadata_parity_is_binding(self):
        zh, en, records = repository_inputs()
        en = en.replace('confidence="high"', 'confidence="low"', 1)
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("direction parity" in error for error in errors), errors)

    def test_paired_period_window_drift_from_current_dates_is_rejected(self):
        zh, en, records = repository_inputs()
        zh = shift_period_windows_one_day_earlier(zh)
        en = shift_period_windows_one_day_earlier(en)
        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("current expected window" in error for error in errors), errors)

    def test_each_period_section_requires_exactly_one_visible_date_range(self):
        fixtures = (
            (
                "last-7-days",
                "2026-08-15—2026-08-21",
                "2026-08-13—2026-08-19",
            ),
            (
                "last-30-days",
                "2026-07-23—2026-08-21",
                "2026-07-21—2026-08-19",
            ),
        )
        for anchor, correct, contradictory in fixtures:
            for mutation, replacement in (
                ("zero", ""),
                ("duplicate", f"{correct}\n\n{contradictory}"),
            ):
                with self.subTest(anchor=anchor, mutation=mutation):
                    zh, en, records = repository_inputs()
                    zh = zh.replace(correct, replacement, 1)
                    en = en.replace(correct, replacement, 1)
                    errors = validate_reading.validate_benchmark_projection(
                        zh, en, records
                    )
                    self.assertTrue(
                        any(
                            anchor in error
                            and "exactly one visible date range" in error
                            for error in errors
                        ),
                        errors,
                    )

    def test_poisoned_period_window_cannot_drive_timeline_completeness(self):
        zh, en, records = repository_inputs()
        record = native_record("native-poison", "2026-07-21T01:00:00Z")
        record["published_at"] = "2026-07-01T00:00:00Z"
        records.append(record)
        zh = shift_period_windows_one_day_earlier(zh)
        en = shift_period_windows_one_day_earlier(en)

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(any("current expected window" in error for error in errors), errors)
        self.assertFalse(
            any(
                "native-poison" in error and "missing from Timeline" in error
                for error in errors
            ),
            errors,
        )

    def test_poisoned_period_window_cannot_admit_out_of_window_support(self):
        zh, en, records = repository_inputs()
        record = native_record("native-poison-support", "2026-08-13T01:00:00Z")
        records.append(record)
        zh = set_first_period_direction(
            insert_timeline_entry(shift_period_windows_one_day_earlier(zh), record),
            state="new_signal",
            supports=("native-poison-support",),
        )
        en = set_first_period_direction(
            insert_timeline_entry(shift_period_windows_one_day_earlier(en), record),
            state="new_signal",
            supports=("native-poison-support",),
        )

        errors = validate_reading.validate_benchmark_projection(zh, en, records)

        self.assertTrue(
            any(
                "native-poison-support" in error
                and "outside 2026-08-15—2026-08-21" in error
                for error in errors
            ),
            errors,
        )

    def test_hidden_support_links_do_not_satisfy_visible_support_parity(self):
        zh, en, records = repository_inputs()
        record = native_record("native-hidden-support", "2026-08-21T00:48:57Z")
        records.append(record)
        for language in ("zh", "en"):
            text = zh if language == "zh" else en
            text = set_first_period_direction(
                insert_timeline_entry(text, record),
                state="new_signal",
                supports=("native-hidden-support",),
            )
            visible_support = (
                "支撑：[NATIVE-HIDDEN-SUPPORT](#entry-native-hidden-support)；"
                if language == "zh"
                else "Supports: [NATIVE-HIDDEN-SUPPORT](#entry-native-hidden-support);"
            )
            text = text.replace(
                visible_support, f"<!-- {visible_support} -->", 1
            )
            if language == "zh":
                zh = text
            else:
                en = text

        errors = validate_reading.validate_benchmark_projection(zh, en, records)
        self.assertTrue(any("visible support" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
