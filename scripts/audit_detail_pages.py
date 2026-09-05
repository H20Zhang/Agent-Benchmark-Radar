#!/usr/bin/env python3

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data" / "benchmarks.json"
NOTES = ROOT / "benchmarks"

WITNESSES = {
    "measurement": (
        r"测什么|到底测什么|测量对象|measurement|what it (?:actually )?measures|measurement object|measurement target|evaluation object",
        2,
    ),
    "delta": (
        r"相比|前身|前驱|compared|relative to|what changed|genealogy|谱系|演化",
        1,
    ),
    "protocol": (
        r"评测|协议|protocol|evaluation setup|how .*evaluat|实际怎样评测|公平比较|fair comparison|comparison contract",
        2,
    ),
    "evidence": (
        r"证据|结果|分数|evidence|result|score|leaderboard",
        2,
    ),
    "validity": (
        r"边界|混杂|混淆|限制|不能|局限|结论上限|confound|limitation|cannot|does not establish|score boundary|score ceiling|what (?:this|the) score supports",
        2,
    ),
    "gap": (
        r"还没有|没有覆盖|还没有测什么|未覆盖|下一步|缺口|next|unmeasured|coverage gap|remaining gap",
        2,
    ),
}

ROLE_TARGETS = {
    "precursor": 6,
    "foundation": 7,
    "transition": 8,
    "frontier": 9,
}


def score_note(text: str) -> tuple[int, list[str]]:
    score = 0
    missing: list[str] = []
    lowered = text.lower()
    for label, (pattern, weight) in WITNESSES.items():
        if re.search(pattern, lowered, flags=re.IGNORECASE):
            score += weight
        else:
            missing.append(label)
    # Reward source traceability and concrete comparison controls without making length the target.
    if re.search(r"https://", text):
        score += 1
    if len(text) >= 1800:
        score += 1
    return score, missing


def grade(score: int, target: int) -> str:
    if score >= target + 2:
        return "A"
    if score >= target:
        return "B"
    if score >= max(5, target - 2):
        return "C"
    return "D"


def main() -> int:
    records = json.loads(REGISTRY.read_text(encoding="utf-8"))
    counts = Counter()
    area_grades: dict[str, Counter] = defaultdict(Counter)
    priority: list[tuple[int, str, str, str, list[str], int]] = []
    parity_issues: list[str] = []

    for item in records:
        record_id = item["id"]
        zh_path = NOTES / f"{record_id}.md"
        en_path = NOTES / f"{record_id}.en.md"
        if not (zh_path.exists() and en_path.exists()):
            parity_issues.append(f"{record_id}: missing bilingual note pair")
            continue

        zh_text = zh_path.read_text(encoding="utf-8")
        en_text = en_path.read_text(encoding="utf-8")
        zh_score, zh_missing = score_note(zh_text)
        en_score, en_missing = score_note(en_text)
        role = item.get("evolution_role", "transition")
        target = ROLE_TARGETS.get(role, 8)
        pair_score = min(zh_score, en_score)
        pair_grade = grade(pair_score, target)
        counts[pair_grade] += 1
        area_grades[item["area"]][pair_grade] += 1

        missing = sorted(set(zh_missing) | set(en_missing))
        if set(zh_missing) != set(en_missing):
            parity_issues.append(
                f"{record_id}: semantic coverage differs zh={zh_missing or ['complete']} en={en_missing or ['complete']}"
            )

        # Higher importance, newer roles, and lower semantic depth rise first.
        urgency = (5 - min(item.get("importance", 3), 5)) * -1
        role_weight = {"frontier": 3, "transition": 2, "foundation": 1, "precursor": 0}.get(role, 1)
        priority_score = (target - pair_score) * 10 + role_weight * 3 + item.get("importance", 3) + urgency
        priority.append((priority_score, record_id, item["area"], pair_grade, missing, pair_score))

    print(f"detail-depth audit: {len(records)} canonical benchmark(s)")
    print("grades: " + ", ".join(f"{key}={counts[key]}" for key in "ABCD"))
    for area in ("agent-memory", "rag", "data-agent"):
        stats = area_grades[area]
        print(f"  {area}: " + ", ".join(f"{key}={stats[key]}" for key in "ABCD"))

    print("highest-priority content debt:")
    for _, record_id, area, pair_grade, missing, pair_score in sorted(priority, reverse=True)[:30]:
        suffix = f" missing={','.join(missing)}" if missing else ""
        print(f"  {record_id:<32} area={area:<12} grade={pair_grade} score={pair_score}{suffix}")

    if parity_issues:
        print(f"semantic-parity warnings: {len(parity_issues)}")
        for issue in parity_issues[:30]:
            print(f"  {issue}")
        if len(parity_issues) > 30:
            print(f"  ... and {len(parity_issues) - 30} more")
    else:
        print("semantic-parity warnings: 0")

    # This is an audit, not a prose-shape linter. CI fails only on missing pairs;
    # depth grades are used to prioritize editorial backfill without forcing every
    # benchmark into identical headings or artificial length.
    if any("missing bilingual note pair" in issue for issue in parity_issues):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
