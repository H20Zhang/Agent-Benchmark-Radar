"""Pure validator for the bilingual, time-first Radar README contract."""

import re
from dataclasses import dataclass
from datetime import datetime


ANCHORS = (
    "timeline",
    "latest",
    "periods",
    "last-7-days",
    "last-30-days",
    "field-map",
    "reading-paths",
    "library",
)
ORDERED_ANCHORS = ("timeline", "periods", "field-map", "reading-paths", "library")
MAP_TOKENS = ("none", "early_signal", "reinforces", "revises", "splits", "retires")
# These comparison/contract-role words cannot make a visible witness distinctive;
# a valid witness must retain at least two other, distinct lexical terms.
GENERIC_WITNESS_TERMS = frozenset(
    {
        "a",
        "an",
        "and",
        "baseline",
        "baselines",
        "caveat",
        "change",
        "changes",
        "comparison",
        "comparisons",
        "control",
        "controls",
        "data",
        "effect",
        "effects",
        "evidence",
        "finding",
        "findings",
        "gain",
        "gains",
        "general",
        "generic",
        "improved",
        "improvement",
        "limitation",
        "limitations",
        "matched",
        "matching",
        "metric",
        "metrics",
        "number",
        "numbers",
        "or",
        "outcome",
        "outcomes",
        "output",
        "outputs",
        "performance",
        "result",
        "results",
        "same",
        "score",
        "scores",
        "strong",
        "strongest",
        "the",
        "value",
        "values",
        "visible",
        "weak",
        "weaker",
    }
)
ENTRY_ANCHOR_RE = re.compile(r'<a\s+id=["\']entry-([^"\']+)["\']\s*></a>', re.I)
DETAILS_RE = re.compile(
    r"^\s*<details>\s*<summary>(?P<summary>.*?)</summary>"
    r"(?P<body>.*?)</details>\s*$",
    re.I | re.S,
)
FIELD_LABEL_RE = re.compile(
    r"\*\*(?P<label>Question|问题|Evidence|证据|Caveat|限制|Map|地图|Links|链接)"
    r"(?:[.。:：])?\*\*",
    re.I,
)
CONTRACT_RE = re.compile(
    r"<!--\s*timefirst:(?P<name>area|delta|question|evidence|caveat)="
    r"(?P<value>[a-z0-9][a-z0-9._~-]*)\s*-->",
    re.I,
)
SUMMARY_RE = re.compile(
    r"^(?P<date>\d{4}-\d{2}(?:-\d{2})?)\s*·\s*"
    r"(?P<identity>[^·\n]+?)\s*·\s*"
    r"(?P<area>[^—\n]+?)\s*—\s*(?P<delta>\S.*)$"
)
MARKDOWN_LINK_RE = re.compile(r"\[(?P<label>[^\]\r\n]+)\]\((?P<target>[^)\r\n]*)\)")
RANGE_RE = re.compile(
    r"(?P<start>\d{4}-\d{2}-\d{2})\s*[—–]\s*"
    r"(?P<end>\d{4}-\d{2}-\d{2})"
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)


@dataclass(frozen=True)
class Entry:
    identity: str
    title: str
    displayed_date: str
    date_value: datetime
    area_contract: str
    delta_contract: str
    question_contract: str
    evidence_contract: str
    caveat_contract: str
    map_token: str
    link_targets: tuple[str, ...]


def _anchor_re(anchor: str) -> re.Pattern[str]:
    return re.compile(rf'<a\s+id=["\']{re.escape(anchor)}["\']\s*></a>', re.I)


def _anchor_positions(text: str, language: str, errors: list[str]) -> dict[str, int]:
    positions: dict[str, int] = {}
    anchor_surface = _mask_html_comments(text)
    for anchor in ANCHORS:
        matches = list(_anchor_re(anchor).finditer(anchor_surface))
        if not matches:
            errors.append(f"{language}: missing stable anchor {anchor}")
        else:
            positions[anchor] = matches[0].start()
            if len(matches) > 1:
                errors.append(f"{language}: duplicate stable anchor {anchor}")

    if all(anchor in positions for anchor in ORDERED_ANCHORS):
        ordered = [positions[anchor] for anchor in ORDERED_ANCHORS]
        if ordered != sorted(ordered):
            errors.append(
                f"{language}: section order must be timeline < periods < field-map "
                "< reading-paths < library"
            )
    return positions


def _display_date(value: str) -> datetime | None:
    date_format = "%Y-%m-%d" if len(value) == 10 else "%Y-%m"
    try:
        return datetime.strptime(value, date_format)
    except ValueError:
        return None


def strip_html_comments(value: str) -> str:
    """Return the human-visible Markdown surface without machine comments."""

    return HTML_COMMENT_RE.sub("", value)


def _mask_html_comments(value: str) -> str:
    """Mask comments without changing offsets used to slice the raw Markdown."""

    def mask(match: re.Match[str]) -> str:
        return "".join(
            character if character in "\r\n" else " "
            for character in match.group(0)
        )

    return HTML_COMMENT_RE.sub(mask, value)


def _visible_text(value: str) -> str:
    value = strip_html_comments(value)
    value = re.sub(r"<[^>]+>", "", value)
    return value.strip()


def _contract_value(
    value: str,
    contract_name: str,
    language: str,
    identity: str,
    errors: list[str],
    require_witness: bool = False,
) -> str:
    matches = [
        match.group("value").lower()
        for match in CONTRACT_RE.finditer(value)
        if match.group("name").lower() == contract_name
    ]
    if len(matches) != 1:
        errors.append(
            f"{language}: entry identity {identity} needs exactly one "
            f"{contract_name} semantic contract"
        )
        return ""
    contract = matches[0]
    if require_witness:
        parts = contract.split("~")
        if len(parts) != 2 or not all(parts):
            errors.append(
                f"{language}: entry identity {identity} {contract_name} semantic "
                "contract needs one visible-text witness"
            )
            return contract
        witness = parts[1]
        witness_parts = witness.split("-")
        lexical_parts = [part for part in witness_parts if re.search(r"[a-z]", part)]
        specific_parts = {
            part for part in lexical_parts if part not in GENERIC_WITNESS_TERMS
        }
        if len(witness_parts) < 3 or len(specific_parts) < 2:
            errors.append(
                f"{language}: entry identity {identity} {contract_name} semantic "
                "contract needs a distinctive visible-text witness with at least "
                "three terms and two specific content terms"
            )
            return contract
        visible = re.sub(r"[^a-z0-9.]+", "-", _visible_text(value).lower()).strip("-")
        if re.search(rf"(?:^|-){re.escape(witness)}(?:-|$)", visible) is None:
            errors.append(
                f"{language}: entry identity {identity} visible {contract_name} "
                f"does not carry contract witness {witness}"
            )
    return contract


def _body_fields(
    body: str,
    language: str,
    identity: str,
    errors: list[str],
) -> dict[str, str]:
    canonical = {
        "question": "question",
        "问题": "question",
        "evidence": "evidence",
        "证据": "evidence",
        "caveat": "caveat",
        "限制": "caveat",
        "map": "map",
        "地图": "map",
        "links": "links",
        "链接": "links",
    }
    matches = list(FIELD_LABEL_RE.finditer(_mask_html_comments(body)))
    fields: dict[str, str] = {}
    for index, match in enumerate(matches):
        name = canonical[match.group("label").lower()]
        end = matches[index + 1].start() if index + 1 < len(matches) else len(body)
        if name in fields:
            errors.append(f"{language}: entry identity {identity} repeats {name}")
            continue
        fields[name] = body[match.end() : end]

    for name in ("question", "evidence", "caveat", "map", "links"):
        if name not in fields:
            errors.append(f"{language}: entry identity {identity} is missing {name}")
        elif not _visible_text(fields[name]):
            errors.append(f"{language}: entry identity {identity} has empty {name}")
    return fields


def _link_identity(target: str) -> str:
    normalized = target.strip().strip("<>")
    return re.sub(r"\.en\.md(?=(?:#.*)?$)", ".md", normalized, flags=re.I)


def _link_targets(
    field: str,
    language: str,
    identity: str,
    errors: list[str],
) -> tuple[str, ...]:
    links = list(MARKDOWN_LINK_RE.finditer(strip_html_comments(field)))
    valid: list[str] = []
    for link in links:
        if not link.group("label").strip() or not link.group("target").strip():
            errors.append(
                f"{language}: entry identity {identity} has an empty Markdown link target or label"
            )
            continue
        valid.append(_link_identity(link.group("target")))
    if not valid:
        errors.append(f"{language}: entry identity {identity} needs a non-empty Markdown link")
    return tuple(valid)


def _extract_map_token(field: str) -> str | None:
    token_match = re.search(
        rf"(?<![A-Za-z_])({'|'.join(MAP_TOKENS)})(?![A-Za-z_])",
        strip_html_comments(field),
        flags=re.I,
    )
    return token_match.group(1).lower() if token_match else None


def _parse_entry(
    identity: str,
    chunk: str,
    language: str,
    errors: list[str],
) -> Entry | None:
    structural_chunk = _mask_html_comments(chunk)
    if len(re.findall(r"<details(?:\s|>)", structural_chunk, flags=re.I)) != 1:
        errors.append(
            f"{language}: entry identity {identity} must have exactly one top-level details block"
        )
        return None

    details = DETAILS_RE.match(structural_chunk)
    if details is None:
        errors.append(
            f"{language}: entry identity {identity} must be followed by one complete details block"
        )
        return None

    summary_start, summary_end = details.span("summary")
    raw_summary = chunk[summary_start:summary_end]
    summary = _visible_text(raw_summary)
    parsed_summary = SUMMARY_RE.match(summary)
    if parsed_summary is None:
        errors.append(
            f"{language}: entry identity {identity} summary needs date, title, area/problem, and delta"
        )
        return None

    displayed_date = parsed_summary.group("date")
    date_value = _display_date(displayed_date)
    if date_value is None:
        errors.append(f"{language}: entry identity {identity} has invalid displayed date")

    title = parsed_summary.group("identity").strip()
    if not title:
        errors.append(f"{language}: entry identity {identity} has an empty title")
    if not parsed_summary.group("area").strip():
        errors.append(f"{language}: entry identity {identity} has no area/problem text")
    if not parsed_summary.group("delta").strip():
        errors.append(f"{language}: entry identity {identity} has no research delta")

    area_contract = _contract_value(
        raw_summary, "area", language, identity, errors
    )
    delta_contract = _contract_value(
        raw_summary, "delta", language, identity, errors
    )
    body_start, body_end = details.span("body")
    body = chunk[body_start:body_end]
    fields = _body_fields(body, language, identity, errors)
    question_contract = _contract_value(
        fields.get("question", ""), "question", language, identity, errors
    )
    evidence_contract = _contract_value(
        fields.get("evidence", ""),
        "evidence",
        language,
        identity,
        errors,
        require_witness=True,
    )
    caveat_contract = _contract_value(
        fields.get("caveat", ""),
        "caveat",
        language,
        identity,
        errors,
        require_witness=True,
    )

    map_token = _extract_map_token(fields.get("map", ""))
    if map_token is None:
        errors.append(
            f"{language}: entry identity {identity} needs a valid map token: "
            + "|".join(MAP_TOKENS)
        )
    link_targets = _link_targets(fields.get("links", ""), language, identity, errors)

    if date_value is None or map_token is None:
        return None
    return Entry(
        identity,
        title,
        displayed_date,
        date_value,
        area_contract,
        delta_contract,
        question_contract,
        evidence_contract,
        caveat_contract,
        map_token,
        link_targets,
    )


def _timeline_entries(
    text: str,
    positions: dict[str, int],
    language: str,
    errors: list[str],
) -> list[Entry]:
    if "timeline" not in positions or "periods" not in positions:
        return []
    timeline = text[positions["timeline"] : positions["periods"]]
    if re.search(r"\b(?:BLOCKED|DEFERRED|ABSTRACT_ONLY)\b", timeline):
        errors.append(f"{language}: Timeline exposes a private candidate state")

    anchors = list(ENTRY_ANCHOR_RE.finditer(timeline))
    if not anchors:
        errors.append(f"{language}: Timeline has no entry identities")
        return []

    entries: list[Entry] = []
    for index, anchor in enumerate(anchors):
        chunk_end = anchors[index + 1].start() if index + 1 < len(anchors) else len(timeline)
        chunk = timeline[anchor.end() : chunk_end]
        entry = _parse_entry(anchor.group(1), chunk, language, errors)
        if entry is not None:
            entries.append(entry)

    dates = [entry.date_value for entry in entries]
    if any(earlier < later for earlier, later in zip(dates, dates[1:])):
        errors.append(f"{language}: Timeline displayed date order is not descending")
    return entries


def _period_windows(
    text: str,
    positions: dict[str, int],
    language: str,
    errors: list[str],
) -> dict[str, tuple[str, str]]:
    windows: dict[str, tuple[str, str]] = {}
    boundaries = {
        "last-7-days": "last-30-days",
        "last-30-days": "field-map",
    }
    for anchor, next_anchor in boundaries.items():
        if anchor not in positions or next_anchor not in positions:
            continue
        section = text[positions[anchor] : positions[next_anchor]]
        matches = list(RANGE_RE.finditer(strip_html_comments(section)))
        if len(matches) != 1:
            errors.append(
                f"{language}: {anchor} must contain exactly one visible date range"
            )
            continue
        match = matches[0]
        start = match.group("start")
        end = match.group("end")
        start_value = _display_date(start)
        end_value = _display_date(end)
        if start_value is None or end_value is None:
            errors.append(f"{language}: {anchor} has an invalid date window")
            continue
        windows[anchor] = (start, end)
        expected_days = 7 if anchor == "last-7-days" else 30
        if (end_value - start_value).days + 1 != expected_days:
            errors.append(
                f"{language}: {anchor} window must span exactly "
                f"{expected_days} inclusive days"
            )
    if (
        "last-7-days" in windows
        and "last-30-days" in windows
        and windows["last-7-days"][1] != windows["last-30-days"][1]
    ):
        errors.append(
            f"{language}: 7-day and 30-day windows must share the same synthesis endpoint"
        )
    return windows


def validate_pair(zh: str, en: str) -> list[str]:
    """Return deterministic public-contract violations; an empty list is valid."""

    errors: list[str] = []
    zh_positions = _anchor_positions(zh, "Chinese", errors)
    en_positions = _anchor_positions(en, "English", errors)
    zh_entries = _timeline_entries(zh, zh_positions, "Chinese", errors)
    en_entries = _timeline_entries(en, en_positions, "English", errors)

    zh_identities = [entry.identity for entry in zh_entries]
    en_identities = [entry.identity for entry in en_entries]
    if zh_identities != en_identities:
        errors.append("Chinese/English Timeline identity or order drift")

    zh_dates = [entry.displayed_date for entry in zh_entries]
    en_dates = [entry.displayed_date for entry in en_entries]
    if zh_dates != en_dates:
        errors.append("Chinese/English Timeline displayed date or order drift")

    paired_fields = (
        ("title", "title"),
        ("area_contract", "area/problem semantic contract"),
        ("delta_contract", "delta semantic contract"),
        ("question_contract", "question scope"),
        ("evidence_contract", "evidence scope"),
        ("caveat_contract", "caveat scope"),
        ("link_targets", "primary/local link"),
    )
    for attribute, description in paired_fields:
        zh_values = [getattr(entry, attribute) for entry in zh_entries]
        en_values = [getattr(entry, attribute) for entry in en_entries]
        if zh_values != en_values:
            errors.append(f"Chinese/English Timeline {description} drift")

    zh_maps = [entry.map_token for entry in zh_entries]
    en_maps = [entry.map_token for entry in en_entries]
    if zh_maps != en_maps:
        errors.append("Chinese/English Timeline map token or order drift")

    zh_windows = _period_windows(zh, zh_positions, "Chinese", errors)
    en_windows = _period_windows(en, en_positions, "English", errors)
    for anchor in ("last-7-days", "last-30-days"):
        if (
            anchor in zh_windows
            and anchor in en_windows
            and zh_windows[anchor] != en_windows[anchor]
        ):
            errors.append(f"Chinese/English {anchor} window drift")

    return errors
