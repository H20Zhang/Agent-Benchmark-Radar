#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "README.md"
EN = ROOT / "README.en.md"
LIB_ZH = ROOT / "library" / "README.md"
LIB_EN = ROOT / "library" / "README.en.md"
REGISTRY = ROOT / "data" / "benchmarks.json"
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def check_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for raw in LINK_RE.findall(text):
        target = raw.strip().strip("<>")
        parsed = urlsplit(target)
        if not target or target.startswith("#") or parsed.scheme or parsed.netloc:
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


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    required = [ZH, EN, LIB_ZH, LIB_EN, REGISTRY, ROOT / "docs" / "RADAR_FAMILY.md", ROOT / "docs" / "EDITORIAL_STANDARD.md", ROOT / "docs" / "DAILY_WORKFLOW.md"]
    for p in required:
        if not p.exists(): errors.append(f"missing contract: {p.relative_to(ROOT)}")
    if errors:
        for e in errors: print("ERROR", e)
        return 1

    json.loads(REGISTRY.read_text(encoding="utf-8"))
    zh = ZH.read_text(encoding="utf-8")
    en = EN.read_text(encoding="utf-8")
    if "README.en.md" not in zh or "README.md" not in en:
        errors.append("README language switch is incomplete")

    zh_order = ["frontier", "evolution", "reading-paths", "library"]
    en_order = zh_order
    for name, text, order in [("README.md", zh, zh_order), ("README.en.md", en, en_order)]:
        pos = []
        for anchor in order:
            needle = f'<a id="{anchor}"></a>'
            if needle not in text: errors.append(f"{name}: missing stable anchor {anchor}")
            pos.append(text.find(needle))
        if any(p < 0 for p in pos) or pos != sorted(pos): errors.append(f"{name}: section-order drift")

    for required_phrase in ["Agent Memory", "Agentic RAG", "Data Agent"]:
        if required_phrase not in zh or required_phrase not in en:
            errors.append(f"README pair missing sibling-radar route: {required_phrase}")

    if "目前仍然测不好的重要问题" not in zh or "What Is Still Poorly Measured" not in en:
        errors.append("poorly-measured guardrail is missing from the entry surface")

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
