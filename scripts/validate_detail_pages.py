#!/usr/bin/env python3

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "benchmarks.json"
NOTES = ROOT / "benchmarks"
GATE_ACTIVATION = datetime.fromisoformat("2026-09-02T13:31:45+00:00")
MIN_NOTE_CHARS = 450
DECISION_MARKER = "<!-- RESEARCH-DECISION:START -->"


def parse_time(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


def note_pair(record_id: str) -> tuple[Path, Path]:
    return NOTES / f"{record_id}.md", NOTES / f"{record_id}.en.md"


def main() -> int:
    records = json.loads(REGISTRY.read_text(encoding="utf-8"))
    errors: list[str] = []
    backlog: list[str] = []

    required_text = ("summary", "measurement_strength", "scale", "coverage_gap")
    required_lists = ("environment", "protocol", "confounders")

    for item in records:
        record_id = item.get("id", "<missing-id>")
        for field in required_text:
            value = item.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{record_id}: missing non-empty {field}")

        for field in required_lists:
            value = item.get(field)
            if not isinstance(value, list) or not any(str(v).strip() for v in value):
                errors.append(f"{record_id}: missing non-empty {field}")

        artifacts = item.get("artifacts") or {}
        if not isinstance(artifacts, dict) or not any(
            isinstance(url, str) and url.startswith("https://") for url in artifacts.values()
        ):
            errors.append(f"{record_id}: missing primary artifact URL")

        zh_note, en_note = note_pair(record_id)
        has_zh, has_en = zh_note.exists(), en_note.exists()
        if has_zh != has_en:
            errors.append(f"{record_id}: benchmark note must be paired in zh/en")
        elif has_zh:
            for path in (zh_note, en_note):
                text = path.read_text(encoding="utf-8").strip()
                if len(text) < MIN_NOTE_CHARS:
                    errors.append(
                        f"{record_id}: {path.name} is too thin ({len(text)} chars; minimum {MIN_NOTE_CHARS})"
                    )
        else:
            backlog.append(record_id)

        accepted_at = parse_time(item.get("radar_published_at"))
        if accepted_at and accepted_at >= GATE_ACTIVATION and not (has_zh and has_en):
            errors.append(
                f"{record_id}: post-activation accepted record lacks paired benchmark notes"
            )

    if backlog:
        print(f"detail-note backlog: {len(backlog)} record(s)")
        print("  " + ", ".join(backlog[:40]))
        if len(backlog) > 40:
            print(f"  ... and {len(backlog) - 40} more")
    else:
        print("detail-note backlog: 0")

    if errors:
        print("detail-page validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"detail-page validation passed for {len(records)} canonical record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
