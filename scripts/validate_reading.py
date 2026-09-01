#!/usr/bin/env python3
from __future__ import annotations

from dataclasses import dataclass
import html
import json
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from urllib.parse import unquote, urlsplit

from timefirst_contract import strip_html_comments, validate_pair

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "README.md"
EN = ROOT / "README.en.md"
LIB_ZH = ROOT / "library" / "README.md"
LIB_EN = ROOT / "library" / "README.en.md"
REGISTRY = ROOT / "data" / "benchmarks.json"
PUBLIC_OPERATIONAL_RUN_PATHS = (ROOT / "runs" / "daily",)
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]*)\)")
ENTRY_ANCHOR_RE = re.compile(r'<a\s+id=["\']entry-([^"\']+)["\']\s*></a>', re.I)
BENCHMARK_ID_RE = re.compile(r"<!--\s*benchmark-id:([a-z0-9-]+)\s*-->")
SUMMARY_IDENTITY_RE = re.compile(
    r"<details>\s*<summary>(?P<date>\d{4}-\d{2}(?:-\d{2})?)\s*·\s*"
    r"(?P<title>[^·\n]+?)\s*·",
    re.I | re.S,
)
VISIBLE_MAP_RE = re.compile(
    r"\*\*(?:Map|地图)(?:[.。:：])?\*\*.*?"
    r"`(none|early_signal|reinforces|revises|splits|retires)`",
    re.I | re.S,
)
PERIOD_RANGE_RE = re.compile(
    r"(?P<start>\d{4}-\d{2}-\d{2})\s*[—–]\s*(?P<end>\d{4}-\d{2}-\d{2})"
)
DIRECTION_COMMENT_RE = re.compile(
    r"<!--\s*timefirst:direction\s+(?P<attributes>.*?)\s*-->", re.I
)
DIRECTION_ATTRIBUTE_RE = re.compile(r'(?P<name>[a-z_]+)="(?P<value>[^"]*)"', re.I)
DIRECTION_STATE_LABEL_RE = re.compile(
    r"(?<![a-z0-9_])(?P<value>new_signal|reinforced|revised|splits|retires|no_material_change)"
    r"(?![a-z0-9_])",
    re.I,
)
DIRECTION_STATE_VALUE_RE = re.compile(
    r"(?<![a-z0-9_])(?P<value>new_signal|reinforced|revised|splits|retires|no_material_change)"
    r"(?![a-z0-9_])\s*\u00b7",
    re.I,
)
DIRECTION_HEADING_RE = re.compile(
    r"^\s*-\s+(?P<state>new_signal|reinforced|revised|splits|retires|no_material_change)"
    r"\s*\u00b7\s*(?P<heading>[^\n]+?)\s*$",
    re.I | re.M,
)
PERIOD_SUPPORT_TARGET_RE = re.compile(r"^#entry-(?P<identity>.+)$", re.I)
VISIBLE_DIRECTION_LABELS = {
    "README.md": {
        "state": DIRECTION_STATE_LABEL_RE,
        "supports": re.compile(r"支撑\s*："),
        "confidence": re.compile(r"置信度\s*："),
        "timing basis": re.compile(r"时间依据\s*："),
        "synthesis": re.compile(r"精确合成时间\s*："),
        "implication": re.compile(r"研究设计含义\s*（"),
        "prior": re.compile(r"先验地图证据\s*："),
    },
    "README.en.md": {
        "state": DIRECTION_STATE_LABEL_RE,
        "supports": re.compile(r"\bSupports\s*:", re.I),
        "confidence": re.compile(r"\bconfidence\s*:", re.I),
        "timing basis": re.compile(r"\btiming basis\s*:", re.I),
        "synthesis": re.compile(r"\bExact synthesis time\s*:", re.I),
        "implication": re.compile(r"\bResearch-design implication\s*\(", re.I),
        "prior": re.compile(r"\bprior map evidence\s*:", re.I),
    },
}
VISIBLE_DIRECTION_VALUES = {
    "README.md": {
        "state": DIRECTION_STATE_VALUE_RE,
        "supports": re.compile(r"支撑\s*：\s*(?P<value>[^\n；]*?)；"),
        "confidence": re.compile(r"置信度\s*：\s*(?P<value>[a-z]+)"),
        "timing basis": re.compile(
            r"时间依据\s*：\s*(?P<value>[a-z0-9._-]+)", re.I
        ),
        "synthesis": re.compile(
            r"精确合成时间\s*：\s*(?P<value>[^\s（\n]+)\s*（UTC）"
        ),
        "implication": re.compile(
            r"研究设计含义\s*（(?P<value>[^）\n]+)）\s*："
        ),
        "prior": re.compile(r"先验地图证据\s*：\s*(?P<value>[^\n。；]+)[。；]"),
    },
    "README.en.md": {
        "state": DIRECTION_STATE_VALUE_RE,
        "supports": re.compile(r"\bSupports\s*:\s*(?P<value>[^\n;]*?);", re.I),
        "confidence": re.compile(r"\bconfidence\s*:\s*(?P<value>[a-z]+)", re.I),
        "timing basis": re.compile(
            r"\btiming basis\s*:\s*(?P<value>[a-z0-9._-]+)", re.I
        ),
        "synthesis": re.compile(
            r"\bExact synthesis time\s*:\s*(?P<value>[^\s(\n]+)\s*\(UTC\)",
            re.I,
        ),
        "implication": re.compile(
            r"\bResearch-design implication\s*\((?P<value>[^)\n]+)\)\s*:",
            re.I,
        ),
        "prior": re.compile(
            r"\bprior map evidence\s*:\s*(?P<value>[^\n.;]+)[.;]", re.I
        ),
    },
}
LOW_SUPPORT_DURABLE_CLAIM_RE = re.compile(
    r"(?<![a-z])(?:reinforc(?:e|es|ed|ing)|trend|durable|established)(?![a-z])|"
    r"趋势|强化|巩固|已确立|持久(?:方向|趋势)",
    re.I,
)
STRICT_UTC_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
RELEASED_RE = re.compile(r"^\d{4}-\d{2}(?:-\d{2})?$")
STABLE_TOKEN_RE = re.compile(r"^[a-z0-9][a-z0-9._-]*$")
FAMILY_ROUTES = {
    "Agent Memory": "https://github.com/H20Zhang/Agent-Memory-Radar#field-map",
    "Agentic RAG": "https://github.com/H20Zhang/Agentic-RAG-Radar#field-map",
    "Data Agent": "https://github.com/H20Zhang/Data-Agent-Radar#field-map",
}
BENCHMARK_ALIASES = (
    "frontier",
    "changes",
    "evolution",
    "benchmark-memory",
    "benchmark-rag",
    "benchmark-data",
)
V2_FIELDS = (
    "published_at",
    "first_seen_at",
    "radar_published_at",
    "time_provenance",
    "map_delta",
)
MAP_DELTAS = frozenset(
    ("none", "early_signal", "reinforces", "revises", "splits", "retires")
)
LEGACY_TIMELINE_COMPATIBILITY_IDS = (
    "dsagentbench",
    "vakra",
    "dataspace",
    "locomo-plus",
    "mem2actbench",
    "agenticdatabench",
    "sgr-bench",
    "realmem",
)
BENCHMARK_AREAS = ("agent-memory", "rag", "data-agent")
DIRECTION_ATTRIBUTES = (
    "key",
    "state",
    "supports",
    "confidence",
    "implication",
    "timing",
    "synthesized",
    "prior",
)
DIRECTION_STATES = frozenset(
    (
        "new_signal",
        "reinforced",
        "revised",
        "splits",
        "retires",
        "no_material_change",
    )
)
CONFIDENCE_VALUES = frozenset(("low", "medium", "high"))
SYNTHESIS_TIMESTAMP = "2026-08-21T00:48:57Z"
SYNTHESIS_DATE = date(2026, 8, 21)
EXPECTED_PERIOD_WINDOWS = {
    "last-7-days": (date(2026, 8, 15), SYNTHESIS_DATE),
    "last-30-days": (date(2026, 7, 23), SYNTHESIS_DATE),
}


def _anchor_matches(text: str, anchor: str) -> list[re.Match[str]]:
    return list(
        re.finditer(rf'<a\s+id=["\']{re.escape(anchor)}["\']\s*></a>', text, re.I)
    )


def validate_benchmark_aliases(zh: str, en: str) -> list[str]:
    """Return Benchmark-only compatibility alias/cardinality violations."""

    errors: list[str] = []
    for language, raw_text in (("README.md", zh), ("README.en.md", en)):
        text = strip_html_comments(raw_text)
        positions: dict[str, int] = {}
        for alias in BENCHMARK_ALIASES:
            matches = _anchor_matches(text, alias)
            if not matches:
                errors.append(f"{language}: missing Benchmark compatibility alias {alias}")
            else:
                positions[alias] = matches[0].start()
                if len(matches) > 1:
                    errors.append(
                        f"{language}: duplicate Benchmark compatibility alias {alias}"
                    )

        order = (
            "timeline",
            "frontier",
            "periods",
            "changes",
            "evolution",
            "field-map",
            "benchmark-memory",
            "benchmark-rag",
            "benchmark-data",
            "reading-paths",
        )
        order_positions: list[int] = []
        for anchor in order:
            if anchor in positions:
                order_positions.append(positions[anchor])
                continue
            matches = _anchor_matches(text, anchor)
            if matches:
                order_positions.append(matches[0].start())
        if len(order_positions) == len(order) and order_positions != sorted(order_positions):
            errors.append(f"{language}: Benchmark compatibility alias order drift")
    return errors


def validate_family_routes(zh: str, en: str) -> list[str]:
    errors: list[str] = []
    for language, text in (("README.md", zh), ("README.en.md", en)):
        visible_text = strip_html_comments(text)
        targets = {raw.strip().strip("<>") for raw in LINK_RE.findall(visible_text)}
        for label, target in FAMILY_ROUTES.items():
            if target not in targets:
                errors.append(
                    f"{language}: missing canonical {label} sibling route to #field-map"
                )
    return errors


def _complete_library_block(
    language: str,
    text: str,
    label: str,
    errors: list[str],
) -> list[tuple[str, str]]:
    """Return identity/row pairs from one bounded complete-library table."""

    start = f"<!-- {label}:START -->"
    end = f"<!-- {label}:END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        errors.append(f"{language}: expected exactly one {label} block")
        return []
    start_at = text.index(start) + len(start)
    end_at = text.index(end, start_at)
    if end_at <= start_at:
        errors.append(f"{language}: malformed {label} block")
        return []

    entries: list[tuple[str, str]] = []
    for line in text[start_at:end_at].splitlines():
        identities = BENCHMARK_ID_RE.findall(line)
        if len(identities) > 1:
            errors.append(
                f"{language}: duplicate benchmark identity marker in {label} row"
            )
        entries.extend((identity, line) for identity in identities)
    return entries


def _validate_library_rows(
    language: str,
    label: str,
    entries: list[tuple[str, str]],
    records: dict[str, dict[str, object]],
    release_column: int,
    errors: list[str],
) -> None:
    """Require hidden identities to be bound to visible canonical Markdown rows."""

    for identity, line in entries:
        location = f"{language}: {label} identity {identity}"
        record = records.get(identity)
        if record is None:
            errors.append(f"{location} has no canonical record")
            continue
        visible = strip_html_comments(line).strip()
        cells = [cell.strip() for cell in visible.split("|")[1:-1]]
        artifacts = record.get("artifacts")
        primary = None
        if isinstance(artifacts, dict):
            primary = next(
                (
                    artifacts.get(key)
                    for key in ("paper", "project", "code", "data")
                    if isinstance(artifacts.get(key), str)
                ),
                None,
            )
        expected_link = f"[{record.get('name')}]({primary})"
        if (
            not visible.startswith("|")
            or len(cells) <= release_column
            or cells[release_column] != record.get("released")
            or not isinstance(primary, str)
            or expected_link not in visible
        ):
            errors.append(
                f"{location} lacks a visible canonical row with exact release, title, "
                "and primary link"
            )


def validate_benchmark_library(
    zh: str,
    en: str,
    records: list[dict[str, object]],
) -> list[str]:
    """Validate the complete non-temporal registry projection in both libraries."""

    errors: list[str] = []
    record_by_id = {str(record.get("id")): record for record in records}
    by_name = sorted(
        records,
        key=lambda record: (str(record.get("name", "")).casefold(), str(record.get("id"))),
    )
    expected_timeline = [
        str(record.get("id"))
        for record in sorted(
            by_name, key=lambda record: str(record.get("released", "")), reverse=True
        )
    ]
    expected_by_area = {
        area: [
            str(record.get("id"))
            for record in sorted(
                (record for record in records if record.get("area") == area),
                key=lambda record: (
                    str(record.get("released", "")),
                    str(record.get("name", "")).casefold(),
                    str(record.get("id")),
                ),
            )
        ]
        for area in BENCHMARK_AREAS
    }

    observed: dict[str, dict[str, list[str]]] = {}
    for language, text in (("library/README.md", zh), ("library/README.en.md", en)):
        language_observed: dict[str, list[str]] = {}
        timeline_entries = _complete_library_block(
            language, text, "COMPLETE-TIMELINE", errors
        )
        timeline_ids = [identity for identity, _ in timeline_entries]
        language_observed["COMPLETE-TIMELINE"] = timeline_ids
        if len(timeline_ids) != len(set(timeline_ids)):
            errors.append(f"{language}: duplicate identity in complete Timeline")
        if timeline_ids != expected_timeline:
            errors.append(
                f"{language}: complete Timeline is incomplete or outside canonical release order"
            )
        _validate_library_rows(
            language,
            "complete Timeline",
            timeline_entries,
            record_by_id,
            0,
            errors,
        )

        for area in BENCHMARK_AREAS:
            label = f"COMPLETE-MAP:{area}"
            entries = _complete_library_block(language, text, label, errors)
            identities = [identity for identity, _ in entries]
            language_observed[label] = identities
            if len(identities) != len(set(identities)):
                errors.append(f"{language}: duplicate identity in {area} map")
            if identities != expected_by_area[area]:
                errors.append(
                    f"{language}: {area} map is incomplete, misassigned, or outside "
                    "canonical release order"
                )
            _validate_library_rows(
                language, f"{area} map", entries, record_by_id, 2, errors
            )
        observed[language] = language_observed

    if observed.get("library/README.md") != observed.get("library/README.en.md"):
        errors.append("Chinese/English complete Benchmark Library identity/order drift")
    return errors


def _strict_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or STRICT_UTC_RE.fullmatch(value) is None:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(
            tzinfo=timezone.utc
        )
    except ValueError:
        return None


def _honest_released_value(value: object) -> bool:
    if not isinstance(value, str) or RELEASED_RE.fullmatch(value) is None:
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d" if len(value) == 10 else "%Y-%m")
    except ValueError:
        return False
    return True


def _canonical_direction_keys(value: object) -> tuple[str, ...] | None:
    if not isinstance(value, list) or not value:
        return None
    if any(
        not isinstance(key, str) or STABLE_TOKEN_RE.fullmatch(key) is None
        for key in value
    ):
        return None
    keys = tuple(value)
    if len(keys) != len(set(keys)):
        return None
    return keys


def validate_record_time_contract(record: dict[str, object]) -> list[str]:
    """Validate one implicit-legacy, explicit-legacy, or native-v2 record."""

    errors: list[str] = []
    identity = str(record.get("id", "<missing-id>"))
    direction_keys_present = "direction_keys" in record
    if direction_keys_present and _canonical_direction_keys(
        record.get("direction_keys")
    ) is None:
        errors.append(
            f"canonical record {identity}: direction_keys must be a non-empty list "
            "of unique lowercase stable tokens"
        )
    present = {field for field in V2_FIELDS if field in record}
    if not present:
        if direction_keys_present:
            errors.append(
                f"canonical record {identity}: direction_keys requires the complete "
                "native_v2 time contract"
            )
        return errors

    missing = [field for field in V2_FIELDS if field not in record]
    if missing:
        for field in missing:
            errors.append(
                f"canonical record {identity}: any v2 field requires complete field {field}"
            )
        return errors

    map_delta = record.get("map_delta")
    if map_delta not in MAP_DELTAS:
        errors.append(
            f"canonical record {identity}: map_delta must be one of "
            f"{', '.join(sorted(MAP_DELTAS))}"
        )

    provenance = record.get("time_provenance")
    if provenance == "legacy_unknown":
        if direction_keys_present:
            errors.append(
                f"canonical record {identity}: direction_keys is native-v2 support "
                "metadata and is forbidden on explicit legacy records"
            )
        released = record.get("released")
        published_at = record.get("published_at")
        if not _honest_released_value(released):
            errors.append(
                f"canonical record {identity}: explicit legacy released must retain honest "
                "YYYY-MM or YYYY-MM-DD precision"
            )
        if published_at != released:
            errors.append(
                f"canonical record {identity}: explicit legacy published_at must equal "
                "released precision exactly"
            )
        if record.get("first_seen_at") is not None:
            errors.append(
                f"canonical record {identity}: legacy_unknown requires first_seen_at=null; "
                "do not fabricate discovery time"
            )
        if record.get("radar_published_at") is not None:
            errors.append(
                f"canonical record {identity}: legacy_unknown requires radar_published_at=null; "
                "do not fabricate Radar acceptance time"
            )
        return errors

    if provenance != "native_v2":
        errors.append(
            f"canonical record {identity}: complete v2 time fields require "
            "time_provenance=native_v2 or legacy_unknown"
        )
        return errors

    parsed_times: list[datetime] = []
    for field in ("published_at", "first_seen_at", "radar_published_at"):
        parsed = _strict_utc(record.get(field))
        if parsed is None:
            errors.append(
                f"canonical record {identity}: native_v2 {field} must be a strict UTC "
                "timestamp YYYY-MM-DDTHH:MM:SSZ"
            )
        else:
            parsed_times.append(parsed)
    if len(parsed_times) == 3 and not (
        parsed_times[0] <= parsed_times[1] <= parsed_times[2]
    ):
        errors.append(
            f"canonical record {identity}: native_v2 requires "
            "published_at <= first_seen_at <= radar_published_at"
        )
    return errors


def validate_benchmark_registry(records: list[dict[str, object]]) -> list[str]:
    """Validate registry-wide time semantics and the bounded legacy migration."""

    errors: list[str] = []
    record_by_id: dict[str, dict[str, object]] = {}
    for record in records:
        identity = str(record.get("id", "<missing-id>"))
        if identity in record_by_id:
            errors.append(f"canonical registry contains duplicate id {identity}")
        record_by_id[identity] = record
        errors.extend(validate_record_time_contract(record))

    compatibility = set(LEGACY_TIMELINE_COMPATIBILITY_IDS)
    for identity in LEGACY_TIMELINE_COMPATIBILITY_IDS:
        record = record_by_id.get(identity)
        if record is None:
            errors.append(
                f"canonical registry is missing explicit legacy compatibility id {identity}"
            )
            continue
        if record.get("time_provenance") != "legacy_unknown":
            errors.append(
                f"canonical record {identity}: Timeline compatibility migration requires "
                "time_provenance=legacy_unknown"
            )
        if record.get("map_delta") != "early_signal":
            errors.append(
                f"canonical record {identity}: Timeline compatibility migration requires "
                "map_delta=early_signal"
            )

    for identity, record in record_by_id.items():
        if (
            identity not in compatibility
            and record.get("time_provenance") == "legacy_unknown"
        ):
            errors.append(
                f"canonical record {identity}: explicit legacy migration is outside the "
                "fixed Timeline compatibility set"
            )
    return errors


def validate_no_public_run_files(paths: tuple[Path, ...]) -> list[str]:
    """Reject every file or symlink below a configured public run path."""

    errors: list[str] = []
    for root in paths:
        if not root.exists() and not root.is_symlink():
            continue
        candidates = (root,) if root.is_file() or root.is_symlink() else root.rglob("*")
        for path in sorted(candidates):
            if path.is_file() or path.is_symlink():
                errors.append(
                    "public operational run file is forbidden; preserve accepted provenance "
                    f"in canonical projections and git, and private state in .radar-private/: {path}"
                )
    return errors


def _section(text: str, anchor: str, next_anchor: str) -> str | None:
    start_marker = f'<a id="{anchor}"></a>'
    end_marker = f'<a id="{next_anchor}"></a>'
    start = text.find(start_marker)
    end = text.find(end_marker, start + len(start_marker)) if start >= 0 else -1
    if start < 0 or end <= start:
        return None
    return text[start:end]


def _period_window(section: str) -> tuple[date, date] | None:
    matches = list(PERIOD_RANGE_RE.finditer(strip_html_comments(section)))
    if len(matches) != 1:
        return None
    match = matches[0]
    try:
        return date.fromisoformat(match.group("start")), date.fromisoformat(
            match.group("end")
        )
    except ValueError:
        return None


def _timeline_chunks(text: str) -> tuple[list[str], dict[str, str]]:
    section = _section(text, "timeline", "periods")
    if section is None:
        return [], {}
    matches = list(ENTRY_ANCHOR_RE.finditer(section))
    identities = [match.group(1) for match in matches]
    chunks: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(section)
        chunks.setdefault(match.group(1), section[match.end() : end])
    return identities, chunks


def _expected_timeline_ids(
    records: list[dict[str, object]],
    window: tuple[date, date],
    synthesis_cutoff: datetime,
) -> list[str]:
    start, end = window
    native: list[tuple[datetime, str]] = []
    for record in records:
        if record.get("time_provenance") != "native_v2":
            continue
        radar_time = _strict_utc(record.get("radar_published_at"))
        if (
            radar_time is not None
            and start <= radar_time.date() <= end
            and radar_time <= synthesis_cutoff
        ):
            native.append((radar_time, str(record.get("id"))))
    native.sort(key=lambda item: (-item[0].timestamp(), item[1]))
    return [identity for _, identity in native] + list(
        LEGACY_TIMELINE_COMPATIBILITY_IDS
    )


def _entry_link_targets(chunk: str) -> list[str]:
    visible_chunk = strip_html_comments(chunk)
    return [raw.strip().strip("<>") for raw in LINK_RE.findall(visible_chunk)]


def _validate_timeline_language(
    language: str,
    text: str,
    records: list[dict[str, object]],
    expected: list[str],
    synthesis_cutoff: datetime,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    record_by_id = {str(record.get("id")): record for record in records}
    identities, chunks = _timeline_chunks(text)

    seen: set[str] = set()
    for identity in identities:
        if identity in seen:
            errors.append(f"{language}: duplicate Timeline identity {identity}")
        seen.add(identity)
    for identity in expected:
        if identity not in identities:
            errors.append(f"{language}: canonical identity {identity} is missing from Timeline")
    for identity in identities:
        if identity not in expected:
            record = record_by_id.get(identity)
            radar_time = (
                _strict_utc(record.get("radar_published_at"))
                if record is not None and record.get("time_provenance") == "native_v2"
                else None
            )
            if radar_time is not None and radar_time > synthesis_cutoff:
                errors.append(
                    f"{language}: Timeline identity {identity} is after public synthesis "
                    f"cutoff {synthesis_cutoff.strftime('%Y-%m-%dT%H:%M:%SZ')}"
                )
            else:
                errors.append(f"{language}: unexpected Timeline identity {identity}")
    if identities != expected:
        errors.append(
            f"{language}: Timeline violates full Radar timestamp order or fixed legacy order"
        )

    for identity in identities:
        record = record_by_id.get(identity)
        if record is None:
            continue
        chunk = chunks.get(identity, "")
        visible_chunk = strip_html_comments(chunk)
        summary = SUMMARY_IDENTITY_RE.search(visible_chunk)
        if summary is None:
            errors.append(f"{language}: Timeline identity {identity} has no parseable summary")
        else:
            visible_title = summary.group("title").strip()
            if visible_title != record.get("name"):
                errors.append(
                    f"{language}: Timeline identity {identity} visible title does not match "
                    "canonical title"
                )
            if record.get("time_provenance") == "native_v2":
                radar_time = _strict_utc(record.get("radar_published_at"))
                expected_date = radar_time.date().isoformat() if radar_time else None
            else:
                expected_date = record.get("published_at")
            if summary.group("date") != expected_date:
                errors.append(
                    f"{language}: Timeline identity {identity} displayed date does not match "
                    "its canonical time basis"
                )

        map_match = VISIBLE_MAP_RE.search(visible_chunk)
        visible_map = map_match.group(1).lower() if map_match else None
        if visible_map != record.get("map_delta"):
            errors.append(
                f"{language}: Timeline identity {identity} visible map token does not match "
                "canonical map_delta"
            )

        targets = _entry_link_targets(visible_chunk)
        artifacts = record.get("artifacts")
        primary = artifacts.get("paper") if isinstance(artifacts, dict) else None
        if not isinstance(primary, str) or primary not in targets:
            errors.append(
                f"{language}: Timeline identity {identity} does not link its canonical primary artifact"
            )

        suffix = ".en.md" if language == "README.en.md" else ".md"
        local = ROOT / "benchmarks" / f"{identity}{suffix}"
        if local.exists():
            expected_target = f"benchmarks/{identity}{suffix}"
            if expected_target not in targets:
                errors.append(
                    f"{language}: Timeline identity {identity} local note link does not match "
                    "its canonical identity and language"
                )
    return identities, errors


def _stable_token_is_visible(token: str, visible: str) -> bool:
    phrase = re.sub(r"[-_.]+", " ", token.lower()).strip()
    normalized = re.sub(r"\s+", " ", visible.lower())
    if not phrase:
        return False
    pattern = r"(?<![a-z0-9])" + r"\s+".join(
        re.escape(part) for part in phrase.split()
    ) + r"(?![a-z0-9])"
    return re.search(pattern, normalized) is not None


def _normalized_stable_phrase(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"[-_.]+", " ", value.lower())).strip()


@dataclass(frozen=True)
class _RenderedLink:
    start: int
    end: int
    target: str
    is_image: bool


@dataclass(frozen=True)
class _RenderedVisibleText:
    text: str
    links: tuple[_RenderedLink, ...]


def _strip_html_tags(value: str) -> str:
    """Remove raw HTML tags while retaining their rendered child text."""

    rendered: list[str] = []
    index = 0
    while index < len(value):
        if value[index] != "<":
            rendered.append(value[index])
            index += 1
            continue
        tag_start = index + 1
        if tag_start < len(value) and value[tag_start] == "/":
            tag_start += 1
        if tag_start >= len(value) or not value[tag_start].isalpha():
            rendered.append(value[index])
            index += 1
            continue
        quote: str | None = None
        escaped = False
        tag_end: int | None = None
        for cursor in range(tag_start + 1, len(value)):
            character = value[cursor]
            if escaped:
                escaped = False
                continue
            if character == "\\":
                escaped = True
                continue
            if quote is not None:
                if character == quote:
                    quote = None
                continue
            if character in {'"', "'"}:
                quote = character
                continue
            if character == ">":
                tag_end = cursor
                break
        if tag_end is None:
            rendered.append(value[index])
            index += 1
        else:
            index = tag_end + 1
    return "".join(rendered)


def _normalize_rendered_fragment(value: str) -> str:
    """Normalize harmless Markdown syntax without erasing rendered words."""

    value = html.unescape(value)
    value = re.sub(r"https?://[^\s<>)]+", "", value, flags=re.I)
    value = re.sub(r"`+", "", value)
    value = value.replace("**", "").replace("__", "").replace("~~", "")
    value = value.replace("*", "")
    value = re.sub(r"(?<!\w)_(?=\S)|(?<=\S)_(?!\w)", "", value)
    return value


def _closing_markdown_delimiter(
    value: str,
    start: int,
    opening: str,
    closing: str,
    *,
    quoted: bool = False,
) -> int | None:
    """Return a balanced Markdown delimiter, respecting escapes and link titles."""

    depth = 0
    quote: str | None = None
    escaped = False
    title_position = False
    for index in range(start, len(value)):
        character = value[index]
        if escaped:
            escaped = False
            continue
        if character == "\\":
            escaped = True
            title_position = False
            continue
        if quote is not None:
            if character == quote:
                quote = None
            continue
        if quoted and depth == 1:
            if character.isspace():
                title_position = True
                continue
            if title_position and character in {'"', "'"}:
                quote = character
                title_position = False
                continue
            title_position = False
        if character == opening:
            depth += 1
        elif character == closing:
            depth -= 1
            if depth == 0:
                return index
    return None


def _markdown_destination_target(value: str) -> str:
    """Return only a Markdown destination, excluding its optional title."""

    value = value.strip()
    if not value:
        return ""
    if value.startswith("<"):
        escaped = False
        for index, character in enumerate(value[1:], start=1):
            if escaped:
                escaped = False
                continue
            if character == "\\":
                escaped = True
                continue
            if character == ">":
                return html.unescape(value[1:index])
        return ""

    depth = 0
    escaped = False
    destination: list[str] = []
    for character in value:
        if escaped:
            destination.append(character)
            escaped = False
            continue
        if character == "\\":
            escaped = True
            continue
        if character == "(":
            depth += 1
        elif character == ")" and depth:
            depth -= 1
        elif character.isspace() and depth == 0:
            break
        destination.append(character)
    return html.unescape("".join(destination))


def _rendered_visible_text(value: str) -> _RenderedVisibleText:
    """Render the visible Markdown text once and retain scoped link locations."""

    value = _strip_html_tags(strip_html_comments(value))
    rendered: list[str] = []
    links: list[_RenderedLink] = []
    rendered_length = 0

    def append_fragment(fragment: str) -> None:
        nonlocal rendered_length
        normalized = _normalize_rendered_fragment(fragment)
        rendered.append(normalized)
        rendered_length += len(normalized)

    cursor = 0
    index = 0
    while index < len(value):
        token_start = index
        if value.startswith("![", index):
            label_start = index + 2
            is_image = True
        elif value[index] == "[":
            label_start = index + 1
            is_image = False
        else:
            index += 1
            continue

        label_end = _closing_markdown_delimiter(value, label_start - 1, "[", "]")
        if label_end is None:
            index += 1
            continue
        destination_start = label_end + 1
        if destination_start >= len(value) or value[destination_start] != "(":
            index = label_end + 1
            continue
        destination_end = _closing_markdown_delimiter(
            value,
            destination_start,
            "(",
            ")",
            quoted=True,
        )
        if destination_end is None:
            index = label_end + 1
            continue

        append_fragment(value[cursor:token_start])
        label = _rendered_visible_text(value[label_start:label_end])
        label_start_rendered = rendered_length
        rendered.append(label.text)
        rendered_length += len(label.text)
        links.extend(
            _RenderedLink(
                start=label_start_rendered + nested.start,
                end=label_start_rendered + nested.end,
                target=nested.target,
                is_image=nested.is_image,
            )
            for nested in label.links
        )
        links.append(
            _RenderedLink(
                start=label_start_rendered,
                end=rendered_length,
                target=_markdown_destination_target(
                    value[destination_start + 1 : destination_end]
                ),
                is_image=is_image,
            )
        )
        cursor = destination_end + 1
        index = cursor
    append_fragment(value[cursor:])
    return _RenderedVisibleText("".join(rendered), tuple(links))


def _direction_item_blocks(section: str) -> list[tuple[int, str, int, int]]:
    """Return visible direction blocks bounded by the next direction item."""

    lines = section.splitlines(keepends=True)
    starts: list[int] = []
    for index, line in enumerate(lines):
        visible_line = _rendered_visible_text(line).text
        if DIRECTION_HEADING_RE.search(visible_line) is not None:
            starts.append(index)
    offsets: list[int] = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    blocks: list[tuple[int, str, int, int]] = []
    for index, start in enumerate(starts):
        end = starts[index + 1] if index + 1 < len(starts) else len(lines)
        blocks.append(
            (start + 1, "".join(lines[start:end]), offsets[start], offsets[end])
        )
    return blocks


def _parse_direction_items(
    language: str,
    anchor: str,
    section: str,
    window: tuple[date, date],
    records: list[dict[str, object]],
    errors: list[str],
) -> list[tuple[str, str, tuple[str, ...], str, str, str, str, str]]:
    record_by_id = {str(record.get("id")): record for record in records}
    items: list[tuple[str, str, tuple[str, ...], str, str, str, str, str]] = []
    seen_keys: set[str] = set()
    label_patterns = VISIBLE_DIRECTION_LABELS[language]
    value_patterns = VISIBLE_DIRECTION_VALUES[language]
    blocks = _direction_item_blocks(section)
    for metadata in DIRECTION_COMMENT_RE.finditer(section):
        owners = [
            block for block in blocks if block[2] <= metadata.start() < block[3]
        ]
        if len(owners) != 1:
            errors.append(
                f"{language}: {anchor} has orphan direction metadata not owned by "
                "exactly one visible direction block"
            )

    for line_number, raw_block, _start, _end in blocks:
        location = f"{language}: {anchor} direction at line {line_number}"
        rendered_block = _rendered_visible_text(raw_block)
        visible_block = rendered_block.text
        claim_visible_block = visible_block
        label_matches = {
            name: list(pattern.finditer(visible_block))
            for name, pattern in label_patterns.items()
        }
        visible_values: dict[str, str] = {}
        visible_value_spans: dict[str, tuple[int, int]] = {}
        for name, matches in label_matches.items():
            if len(matches) != 1:
                errors.append(f"{location} requires exactly one visible {name} field")
                continue
            value_match = value_patterns[name].match(visible_block, matches[0].start())
            if value_match is None or not value_match.group("value").strip():
                errors.append(
                    f"{location} requires exactly one visible {name} field with valid structure"
                )
                continue
            visible_values[name] = value_match.group("value").strip()
            visible_value_spans[name] = value_match.span("value")

        comments = list(DIRECTION_COMMENT_RE.finditer(raw_block))
        if len(comments) != 1:
            errors.append(f"{location} requires exactly one stable direction metadata block")
            continue

        attributes: dict[str, list[str]] = {name: [] for name in DIRECTION_ATTRIBUTES}
        for match in DIRECTION_ATTRIBUTE_RE.finditer(comments[0].group("attributes")):
            name = match.group("name").lower()
            if name in attributes:
                attributes[name].append(match.group("value"))
        complete = True
        for name, values in attributes.items():
            if len(values) != 1 or not values[0]:
                errors.append(f"{location} requires exactly one non-empty {name} value")
                complete = False
        if not complete:
            continue

        values = {name: found[0] for name, found in attributes.items()}
        key = values["key"]
        state = values["state"]
        timing = values["timing"]
        synthesized = values["synthesized"]
        synthesized_time = _strict_utc(synthesized)
        prior = values["prior"]
        for name in ("key", "confidence", "implication", "prior"):
            if STABLE_TOKEN_RE.fullmatch(values[name]) is None:
                errors.append(
                    f"{location} {name} must be a lowercase stable token, not free-form prose"
                )
        support_value = values["supports"]
        supports = (
            ()
            if support_value == "none"
            else tuple(part.strip() for part in support_value.split(",") if part.strip())
        )
        if state not in DIRECTION_STATES:
            errors.append(f"{location} has invalid direction state {state}")
        visible_state = visible_values.get("state")
        if visible_state is None or visible_state.lower() != state:
            errors.append(f"{location} visible state and stable direction state drift")
        visible_heading = DIRECTION_HEADING_RE.search(visible_block)
        if (
            visible_heading is None
            or visible_heading.group("state").lower() != state
            or not _stable_token_is_visible(key, visible_heading.group("heading"))
        ):
            errors.append(f"{location} direction key lacks a bounded heading witness")
        if values["confidence"] not in CONFIDENCE_VALUES:
            errors.append(f"{location} confidence must be low, medium, or high")
        visible_confidence = visible_values.get("confidence")
        if visible_confidence is None or visible_confidence.lower() != values["confidence"]:
            errors.append(f"{location} visible confidence and stable metadata drift")
        if timing != "radar_published_at":
            errors.append(f"{location} timing basis must be radar_published_at")
        visible_timing = visible_values.get("timing basis")
        if visible_timing != timing:
            errors.append(f"{location} visible timing basis and stable metadata drift")
        if synthesized_time is None or synthesized != SYNTHESIS_TIMESTAMP:
            errors.append(
                f"{location} synthesized must be the exact UTC synthesis timestamp "
                f"{SYNTHESIS_TIMESTAMP}"
            )
        visible_synthesis = visible_values.get("synthesis")
        if visible_synthesis != synthesized:
            errors.append(f"{location} exact visible synthesis timestamp drift")
        visible_implication = visible_values.get("implication")
        if (
            visible_implication is None
            or _normalized_stable_phrase(visible_implication)
            != _normalized_stable_phrase(values["implication"])
        ):
            errors.append(f"{location} implication lacks its labeled visible witness")
        if len(supports) != len(set(supports)):
            errors.append(f"{location} contains duplicate support identities")
        visible_support_field = visible_values.get("supports")
        support_span = visible_value_spans.get("supports")
        support_links = (
            sorted(
                (
                    link
                    for link in rendered_block.links
                    if support_span is not None
                    and support_span[0] <= link.start
                    and link.end <= support_span[1]
                ),
                key=lambda link: (link.start, link.end),
            )
            if support_span is not None
            else []
        )
        visible_supports: list[str] = []
        for link in support_links:
            target = PERIOD_SUPPORT_TARGET_RE.fullmatch(link.target)
            if link.is_image or target is None:
                errors.append(
                    f"{location} visible support field contains a non-canonical support link"
                )
                visible_supports.append(f"<invalid:{link.target}>")
                continue
            identity = target.group("identity")
            if identity not in record_by_id:
                errors.append(
                    f"{location} visible support anchor {identity} has no canonical record"
                )
                visible_supports.append(f"<unknown:{identity}>")
                continue
            visible_supports.append(identity)
        if tuple(visible_supports) != supports:
            errors.append(f"{location} visible support order and stable metadata drift")
        if not supports and visible_support_field != "none":
            errors.append(f"{location} zero support must be exactly **none**")
        if supports and visible_support_field is not None and support_span is not None:
            support_surface = visible_block[support_span[0] : support_span[1]]
            remainder = list(support_surface)
            for link in support_links:
                start = link.start - support_span[0]
                end = link.end - support_span[0]
                remainder[start:end] = " " * max(end - start, 0)
            if re.sub(r"[\s·]+", "", "".join(remainder)):
                errors.append(
                    f"{location} visible support field must contain only canonical support links"
                )
        if key in seen_keys:
            errors.append(f"{location} repeats stable direction key {key}")
        seen_keys.add(key)

        for identity in supports:
            record = record_by_id.get(identity)
            if record is None:
                errors.append(f"{location} support identity {identity} has no canonical record")
                continue
            if record.get("time_provenance") != "native_v2":
                errors.append(
                    f"{location} support identity {identity} must be a native_v2 Radar acceptance; "
                    "legacy context is not support"
                )
                continue
            direction_keys = _canonical_direction_keys(record.get("direction_keys"))
            if direction_keys is None or key not in direction_keys:
                errors.append(
                    f"{location} support identity {identity} direction_keys must include "
                    f"{key}"
                )
            radar_time = _strict_utc(record.get("radar_published_at"))
            if radar_time is None:
                errors.append(
                    f"{location} support identity {identity} has no valid radar_published_at"
                )
            elif not window[0] <= radar_time.date() <= window[1]:
                errors.append(
                    f"{location} support identity {identity} falls outside "
                    f"{window[0].isoformat()}—{window[1].isoformat()} by radar_published_at"
                )
            if (
                synthesized_time is not None
                and radar_time is not None
                and radar_time > synthesized_time
            ):
                errors.append(
                    f"{location} support identity {identity} is accepted after direction "
                    f"synthesized={synthesized}"
                )

        if (
            len(set(supports)) < 2
            and LOW_SUPPORT_DURABLE_CLAIM_RE.search(claim_visible_block) is not None
        ):
            errors.append(
                f"{location} fewer than two distinct supports cannot make a trend/趋势 "
                "claim or reinforced/durable/established claim"
            )

        if state == "no_material_change":
            if supports:
                errors.append(f"{location} no_material_change requires zero canonical support")
            if prior != "none":
                errors.append(f"{location} no_material_change requires prior=none")
        if state == "new_signal":
            if len(set(supports)) != 1:
                errors.append(f"{location} labeled new_signal requires exactly one support identity")
            elif record_by_id.get(supports[0], {}).get("map_delta") != "early_signal":
                errors.append(
                    f"{location} labeled new_signal requires its one record to have "
                    "map_delta=early_signal"
                )
            if prior != "none":
                errors.append(f"{location} new_signal requires prior=none")
        if state == "reinforced" and len(set(supports)) < 2:
            errors.append(
                f"{location} labeled reinforced requires at least two distinct support identities"
            )
        if state in {"revised", "splits", "retires"} and not supports:
            errors.append(f"{location} labeled {state} requires canonical support")

        visible_prior = visible_values.get("prior")
        prior_span = visible_value_spans.get("prior")
        prior_links = (
            sorted(
                (
                    link
                    for link in rendered_block.links
                    if prior_span is not None
                    and prior_span[0] <= link.start
                    and link.end <= prior_span[1]
                ),
                key=lambda link: (link.start, link.end),
            )
            if prior_span is not None
            else []
        )
        if visible_prior == "none" and not prior_links:
            visible_prior_token = "none"
        else:
            visible_prior_token = None
            if prior_span is not None and len(prior_links) == 1:
                prior_link = prior_links[0]
                prior_surface = visible_block[prior_span[0] : prior_span[1]]
                remainder = list(prior_surface)
                start = prior_link.start - prior_span[0]
                end = prior_link.end - prior_span[0]
                remainder[start:end] = " " * max(end - start, 0)
                if (
                    not prior_link.is_image
                    and prior_link.target == "#field-map"
                    and not "".join(remainder).strip()
                ):
                    visible_prior_token = "field-map"
        if visible_prior_token != prior:
            errors.append(f"{location} visible prior-map evidence and metadata drift")
        if state in {"reinforced", "revised", "splits", "retires"}:
            if prior != "field-map" or visible_prior_token != "field-map":
                errors.append(
                    f"{location} durable direction requires independent prior Field Map "
                    "evidence via prior=field-map and a visible #field-map link"
                )

        items.append(
            (
                key,
                state,
                supports,
                values["confidence"],
                values["implication"],
                timing,
                synthesized,
                prior,
            )
        )
    if not items:
        errors.append(f"{language}: {anchor} has no parseable direction metadata")
    return items


def validate_benchmark_projection(
    zh: str,
    en: str,
    records: list[dict[str, object]],
) -> list[str]:
    """Validate Benchmark-only canonical Timeline and rolling-period projections."""

    errors: list[str] = []
    observed_windows: dict[str, dict[str, tuple[date, date]]] = {}
    directions: dict[
        str,
        dict[
            str,
            list[tuple[str, str, tuple[str, ...], str, str, str, str, str]],
        ],
    ] = {}

    for language, text in (("README.md", zh), ("README.en.md", en)):
        language_windows: dict[str, tuple[date, date]] = {}
        language_directions: dict[
            str,
            list[tuple[str, str, tuple[str, ...], str, str, str, str, str]],
        ] = {}
        for anchor, next_anchor in (
            ("last-7-days", "last-30-days"),
            ("last-30-days", "evolution"),
        ):
            section = _section(text, anchor, next_anchor)
            if section is None:
                errors.append(f"{language}: cannot locate {anchor} period section")
                continue
            window = _period_window(section)
            if window is None:
                errors.append(
                    f"{language}: {anchor} must contain exactly one visible date range "
                    "with valid inclusive dates"
                )
            else:
                language_windows[anchor] = window
                expected_window = EXPECTED_PERIOD_WINDOWS[anchor]
                if window != expected_window:
                    errors.append(
                        f"{language}: {anchor} must use current expected window "
                        f"{expected_window[0].isoformat()}—{expected_window[1].isoformat()}"
                    )
            language_directions[anchor] = _parse_direction_items(
                language,
                anchor,
                section,
                EXPECTED_PERIOD_WINDOWS[anchor],
                records,
                errors,
            )
        observed_windows[language] = language_windows
        directions[language] = language_directions

    for anchor in ("last-7-days", "last-30-days"):
        zh_window = observed_windows.get("README.md", {}).get(anchor)
        en_window = observed_windows.get("README.en.md", {}).get(anchor)
        if zh_window is not None and en_window is not None and zh_window != en_window:
            errors.append(f"Chinese/English {anchor} window drift")

    synthesis_cutoff = _strict_utc(SYNTHESIS_TIMESTAMP)
    if synthesis_cutoff is None:
        errors.append("Benchmark projection has an invalid public synthesis cutoff")
        return errors
    expected = _expected_timeline_ids(
        records, EXPECTED_PERIOD_WINDOWS["last-30-days"], synthesis_cutoff
    )
    actual: dict[str, list[str]] = {}
    for language, text in (("README.md", zh), ("README.en.md", en)):
        identities, language_errors = _validate_timeline_language(
            language, text, records, expected, synthesis_cutoff
        )
        actual[language] = identities
        errors.extend(language_errors)
    if actual.get("README.md") != actual.get("README.en.md"):
        errors.append("Chinese/English Timeline identity or order drift")

    for anchor in ("last-7-days", "last-30-days"):
        if directions.get("README.md", {}).get(anchor) != directions.get(
            "README.en.md", {}
        ).get(anchor):
            errors.append(f"Chinese/English {anchor} direction parity drift")
    return errors


def check_links(path: Path, errors: list[str]) -> None:
    text = strip_html_comments(path.read_text(encoding="utf-8"))
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>")
        if not target:
            errors.append(f"{path.relative_to(ROOT)}: empty link target")
            continue
        parsed = urlsplit(target)
        if target.startswith("#") or parsed.scheme or parsed.netloc:
            continue
        rel = unquote(parsed.path)
        if not rel:
            continue
        resolved = (path.parent / rel).resolve()
        try:
            resolved.relative_to(ROOT.resolve())
        except ValueError:
            errors.append(f"{path.relative_to(ROOT)}: link escapes repo: {target}")
            continue
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: broken local link: {target}")



def validate_public_readme(
    zh: str,
    en: str,
    records: list[dict[str, object]],
) -> list[str]:
    """Validate the compact v3 reader projection without the retired deep/period layers."""

    errors: list[str] = []
    record_ids = {str(record.get("id")) for record in records}
    cases = (
        ("README.md", zh, "**主干：**"),
        ("README.en.md", en, "**Defining chain:**"),
    )
    banned = (
        "## 最新条目深读",
        "## 7 天 / 30 天：评价对象发生了什么变化",
        "## 三个方向的演化",
        "## 7 days / 30 days: What Changed in the Evaluation Object",
        "## Three Areas",
    )

    for language, text, chain_label in cases:
        for phrase in banned:
            if phrase in text:
                errors.append(f"{language}: retired reader surface returned: {phrase}")

        onboarding_start = text.find("<!-- ONBOARDING:START -->")
        onboarding_end = text.find("<!-- ONBOARDING:END -->")
        recipe_start = text.find("<!-- EVALUATION-RECIPES:START -->")
        recipe_end = text.find("<!-- EVALUATION-RECIPES:END -->")
        recipe_anchor = text.find('<a id="evaluation-recipes"></a>')
        frontier = text.find('<a id="frontier-signals"></a>')
        release = text.find('<a id="release-timeline"></a>')
        field_map = text.find('<a id="field-map"></a>')
        if min(onboarding_start, onboarding_end, recipe_start, recipe_end, recipe_anchor, frontier) < 0:
            errors.append(f"{language}: missing onboarding or Evaluation Recipes surface")
        elif not (onboarding_start < onboarding_end < recipe_start <= recipe_anchor < recipe_end < frontier < release):
            errors.append(f"{language}: intent routing / recipe / frontier ordering drift")
        else:
            onboarding = text[onboarding_start:onboarding_end]
            required_routes = (
                "#benchmark-memory", "#recipe-memory", "#registry-memory",
                "#benchmark-rag", "#recipe-rag", "#registry-rag",
                "#benchmark-data", "#recipe-data", "#registry-data",
            )
            for route in required_routes:
                if route not in onboarding:
                    errors.append(f"{language}: onboarding is missing area route {route}")
            recipe_block = text[recipe_start:recipe_end]
            recipe_sections = (("recipe-memory", "recipe-rag"), ("recipe-rag", "recipe-data"), ("recipe-data", None))
            for anchor, next_anchor in recipe_sections:
                start_at = recipe_block.find(f'<a id="{anchor}"></a>')
                end_at = recipe_block.find(f'<a id="{next_anchor}"></a>', start_at + 1) if next_anchor else len(recipe_block)
                if start_at < 0 or end_at <= start_at:
                    errors.append(f"{language}: missing recipe section {anchor}")
                    continue
                section = recipe_block[start_at:end_at]
                rows = [line for line in section.splitlines() if line.startswith("| **")]
                if not 3 <= len(rows) <= 5:
                    errors.append(f"{language}: {anchor} must contain 3–5 bounded recipes")
                for row in rows:
                    if len(re.findall(r"\]\((?:https?://)[^)]+\)", row)) < 2:
                        errors.append(f"{language}: {anchor} recipe row needs Core and Complement links")
        for registry_anchor in ("registry-memory", "registry-rag", "registry-data"):
            if text.count(f'<a id="{registry_anchor}"></a>') != 1:
                errors.append(f"{language}: expected exactly one stable {registry_anchor} anchor")
        if release < 0 or field_map < 0 or release >= field_map:
            errors.append(f"{language}: release timeline must precede Benchmark Map")
        elif "<details" in text[release:field_map].lower():
            errors.append(f"{language}: per-item deep reads returned to the main README")

        for label in (
            "TABLE-FIRST:RECENT",
            "TABLE-FIRST:AREA:agent-memory",
            "TABLE-FIRST:AREA:rag",
            "TABLE-FIRST:AREA:data-agent",
        ):
            start_marker = f"<!-- {label}:START -->"
            end_marker = f"<!-- {label}:END -->"
            if text.count(start_marker) != 1 or text.count(end_marker) != 1:
                errors.append(f"{language}: expected exactly one {label} block")
                continue
            block = text.split(start_marker, 1)[1].split(end_marker, 1)[0]
            expected_columns = 4 if label == "TABLE-FIRST:RECENT" else 5
            for line in block.splitlines():
                visible = strip_html_comments(line).strip()
                if visible.startswith("|") and visible.endswith("|"):
                    cells = visible.split("|")[1:-1]
                    if len(cells) != expected_columns:
                        errors.append(
                            f"{language}: {label} must have exactly {expected_columns} visible columns"
                        )
                        break
            for forbidden in ("相较以往", "带来的变化", "What changed", "Why it changed the question"):
                if forbidden in block:
                    errors.append(f"{language}: {label} still exposes parallel change column {forbidden}")

        sections = (
            ("benchmark-memory", "benchmark-rag"),
            ("benchmark-rag", "benchmark-data"),
            ("benchmark-data", "all-benchmarks"),
        )
        for anchor, next_anchor in sections:
            start = text.find(f'<a id="{anchor}"></a>')
            end = text.find(f'<a id="{next_anchor}"></a>', start + 1)
            if start < 0 or end < 0:
                errors.append(f"{language}: missing Benchmark Map section {anchor}")
                continue
            if text[start:end].count(chain_label) != 1:
                errors.append(f"{language}: {anchor} needs exactly one defining chain")

        for label in ("TABLE-FIRST:AREA:agent-memory", "TABLE-FIRST:AREA:rag", "TABLE-FIRST:AREA:data-agent"):
            block = text.split(f"<!-- {label}:START -->", 1)[1].split(f"<!-- {label}:END -->", 1)[0]
            for identity in BENCHMARK_ID_RE.findall(block):
                if identity not in record_ids:
                    errors.append(f"{language}: unknown benchmark identity {identity} in {label}")

    def _recipe_external_links(value: str) -> list[str]:
        try:
            block = value.split("<!-- EVALUATION-RECIPES:START -->", 1)[1].split(
                "<!-- EVALUATION-RECIPES:END -->", 1
            )[0]
        except IndexError:
            return []
        return re.findall(r"\]\((https?://[^)]+)\)", block)

    if _recipe_external_links(zh) != _recipe_external_links(en):
        errors.append("Chinese/English Evaluation Recipes benchmark-link drift")

    try:
        zh_recent = BENCHMARK_ID_RE.findall(zh.split("<!-- TABLE-FIRST:RECENT:START -->", 1)[1].split("<!-- TABLE-FIRST:RECENT:END -->", 1)[0])
        en_recent = BENCHMARK_ID_RE.findall(en.split("<!-- TABLE-FIRST:RECENT:START -->", 1)[1].split("<!-- TABLE-FIRST:RECENT:END -->", 1)[0])
        if zh_recent != en_recent:
            errors.append("Chinese/English recent release table identity or order drift")
    except IndexError:
        pass

    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = [ZH, EN, LIB_ZH, LIB_EN, REGISTRY, ROOT / "docs" / "RADAR_FAMILY.md", ROOT / "docs" / "RADAR_AGENT_PROTOCOL.md", ROOT / "docs" / "EDITORIAL_STANDARD.md", ROOT / "docs" / "DAILY_WORKFLOW.md"]
    for p in required:
        if not p.exists(): errors.append(f"missing contract: {p.relative_to(ROOT)}")
    if errors:
        for e in errors: print("ERROR", e)
        return 1

    records = json.loads(REGISTRY.read_text(encoding="utf-8"))
    zh = ZH.read_text(encoding="utf-8")
    en = EN.read_text(encoding="utf-8")
    errors.extend(validate_benchmark_registry(records))
    errors.extend(validate_public_readme(zh, en, records))
    errors.extend(
        validate_benchmark_library(
            LIB_ZH.read_text(encoding="utf-8"),
            LIB_EN.read_text(encoding="utf-8"),
            records,
        )
    )
    errors.extend(validate_no_public_run_files(PUBLIC_OPERATIONAL_RUN_PATHS))
    if "README.en.md" not in zh or "README.md" not in en:
        errors.append("README language switch is incomplete")
    errors.extend(validate_family_routes(zh, en))
    errors.extend(validate_benchmark_aliases(zh, en))

    evaluation_frontier_anchor = '<a id="evaluation-frontiers"></a>'
    if evaluation_frontier_anchor not in zh or evaluation_frontier_anchor not in en:
        errors.append("evaluation-frontiers guardrail is missing from the entry surface")

    for pat in [r"真正重要的是", r"关键不在于.*而在于", r"值得注意的是", r"this matters because", r"the important thing is not"]:
        n = len(re.findall(pat, zh + "\n" + en, flags=re.IGNORECASE))
        if n >= 3: warnings.append(f"repeated editorial skeleton {pat!r}: {n} occurrences")

    for p in [ZH, EN, LIB_ZH, LIB_EN]: check_links(p, errors)

    for w in warnings: print("WARN", w)
    if errors:
        for e in errors: print("ERROR", e)
        return 1
    print("Validated Chinese-first Benchmark Radar entry and family routing.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
