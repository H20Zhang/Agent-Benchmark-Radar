# Benchmark Radar Time-First v2 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn Agent Benchmark Radar into the family-level, time-first evaluation radar and establish the reusable README validation contract for all four repositories.

**Architecture:** Keep the canonical benchmark registry and deep notes intact. Re-project the current reader surface as compact inline-expandable Timeline entries, explicit 7-day/30-day synthesis, then stable evaluation maps. Put the autonomous multi-agent workflow in repository-owned protocol files and validate the public contract with a pure Python parser.

**Tech Stack:** Markdown, Python 3.12 standard library, GitHub Actions, JSON registry.

**Spec:** `docs/superpowers/specs/2026-08-20-agent-maintained-time-first-radar-v2-design.md`

## Global Constraints

- The Daily Scheduled Agent is the only writer; delegated research agents never mutate repository or GitHub state.
- Public order is `Latest Timeline → 7-day / 30-day synthesis → Field Map → Reading Paths → Library`.
- Latest has no fixed item-count cap; every accepted record in the current window remains visible as one compact `<details>` summary.
- Closed summaries expose date, identity, area/problem, and one-sentence delta; open bodies expose Question, Evidence, Caveat, Map status, and Links.
- `published_at`, `first_seen_at`, and `radar_published_at` retain distinct meanings; unknown legacy times are never fabricated.
- A single work may be `early_signal` but may not silently rewrite a durable field-map claim.
- Chinese and English identities, displayed dates/order, evidence scope, map status, and primary links remain paired.
- Full-text-blocked, deferred, rejected, or abstract-only candidates never appear on public surfaces.
- Preserve Benchmark Radar as family entry/evaluation layer and route methods/systems to the three domain radars.

---

### Task 1: Implement the family protocol and Benchmark time-first surface

**Files:**
- Create: `docs/RADAR_AGENT_PROTOCOL.md`
- Modify: `docs/DAILY_WORKFLOW.md`
- Modify: `CURATION.md`
- Modify: `SCHEMA.md`
- Modify: `README.md`
- Modify: `README.en.md`
- Modify: `digests/README.md`
- Create: `scripts/timefirst_contract.py`
- Create: `tests/test_timefirst_contract.py`
- Modify: `scripts/validate_reading.py`
- Modify: `.github/workflows/validate.yml`

**Interfaces:**
- Produces: `timefirst_contract.validate_pair(zh: str, en: str) -> list[str]` for reuse verbatim by the three domain repositories.
- Produces stable anchors: `timeline`, `latest`, `frontier`, `periods`, `last-7-days`, `last-30-days`, `evolution`, `field-map`, `reading-paths`, `library`.
- Produces entry anchors `entry-<canonical-id>` paired across Chinese and English.

- [ ] **Step 1: Write the failing behavior tests**

Create `tests/test_timefirst_contract.py` with `unittest`. Build complete in-memory Chinese/English fixtures and assert observable reader behavior:

```python
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from timefirst_contract import validate_pair


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

    def test_language_identity_or_date_order_drift_is_rejected(self):
        zh, en = make_pair(2)
        en = en.replace('entry-work-1', 'entry-wrong-work', 1)
        self.assertTrue(any('identity' in error.lower() for error in validate_pair(zh, en)))

    def test_missing_evidence_or_caveat_is_rejected(self):
        zh, en = make_pair(1)
        zh = zh.replace('**证据。** controlled result', '')
        self.assertTrue(any('evidence' in error.lower() for error in validate_pair(zh, en)))

    def test_period_window_drift_is_rejected(self):
        zh, en = make_pair(1)
        en = en.replace('2026-08-14—2026-08-20', '2026-08-13—2026-08-20', 1)
        self.assertTrue(any('window' in error.lower() for error in validate_pair(zh, en)))
```

`make_pair(count)` must emit the full anchor order, paired `entry-work-N` anchors, descending `2026-08-DD` summaries, all five semantic labels, both period ranges, and no production helper reuse for expected values.

- [ ] **Step 2: Run the focused test and verify RED**

Run: `python -m unittest tests.test_timefirst_contract -v`

Expected: import failure because `scripts/timefirst_contract.py` does not exist, or repository-surface failure because the current README lacks `timeline`/`periods` and compact entry details.

- [ ] **Step 3: Implement the pure time-first validator**

Create `scripts/timefirst_contract.py` using only `re`, `dataclasses`, and `datetime`. Implement:

```python
def validate_pair(zh: str, en: str) -> list[str]:
    """Return deterministic public-contract violations; an empty list is valid."""
```

It must:

- check ordered anchors `timeline < periods < field-map < reading-paths < library` in both languages;
- accept `YYYY-MM-DD` and honest legacy `YYYY-MM` display precision;
- extract every `entry-*` anchor followed by exactly one top-level `<details>` block;
- require closed-summary date, non-empty identity/title, area/problem text, and delta text after an em dash;
- require `Question/Evidence/Caveat/Map/Links` or `问题/证据/限制/地图/链接` in every open body;
- require map token `none|early_signal|reinforces|revises|splits|retires` and at least one Markdown link;
- reject public `BLOCKED`, `DEFERRED`, or `ABSTRACT_ONLY` tokens inside Timeline;
- check descending displayed date order without enforcing a count maximum;
- check Chinese/English entry identities, displayed dates, order, map tokens, and period date windows match;
- require explicit ranges under `last-7-days` and `last-30-days`.

- [ ] **Step 4: Re-project both Benchmark READMEs**

Use this top navigation and section order in natural Chinese/English:

```text
Latest Timeline · 7 days / 30 days · Field Map · Reading Paths · Library
```

Co-locate aliases `<a id="timeline"></a><a id="latest"></a><a id="frontier"></a>` before the Timeline H2. Replace the eight-row frontier table and separated explainers with eight compact `<details>` entries in current registry order. Each entry uses `entry-<registry-id>`, displays the honest legacy release month where only month precision exists, contains the five semantic labels, uses `early_signal` as the per-record map status unless the registry provides stronger independent support, and links to the primary source plus local benchmark note when present.

Add `<a id="periods"></a><a id="changes"></a>` after Timeline. Add:

- `last-7-days` with exact window `2026-08-14—2026-08-20`;
- `last-30-days` with exact window `2026-07-22—2026-08-20`.

Synthesize changes from the existing canonical records and notes, not from a count of releases. Preserve the existing evolution table, three area maps, measurement gaps, paths, and Library after the period section. Add `field-map` before the three area maps and explicit `benchmark-memory`, `benchmark-rag`, and `benchmark-data` aliases before their H3 headings. Route each Benchmark area directly to the sibling repository's `#field-map` anchor.

Add one section-level migration notice: legacy records without reconstructable Radar acceptance timestamps are temporarily ordered by original release date/month; all post-cutover records use `radar_published_at`.

- [ ] **Step 5: Install the autonomous workflow contract**

Create `docs/RADAR_AGENT_PROTOCOL.md` as the operational form of the spec. It must include the role hierarchy, single-writer rule, internal state machine, three timestamps, Timeline/period/map gates, retry/atomicity rules, bilingual projection, boundary cadence, and compact role prompt contracts. It must state that candidates remain private and that no human approval gate is part of the normal Daily Agent transaction.

Rewrite `docs/DAILY_WORKFLOW.md` as the Benchmark adapter: source lanes, measurement-object acceptance test, protocol/confounder audit, canonical locations, note/genealogy rules, evaluation-specific `map_delta`, current validation commands, and run-log policy. Update `CURATION.md` and `SCHEMA.md` to reference v2 and permit the three future time fields plus `map_delta` without fabricating legacy data. Update `digests/README.md` with rolling-root versus closed-period semantics and weekly/monthly boundary rules.

- [ ] **Step 6: Wire validation and verify GREEN**

Make `scripts/validate_reading.py` call `validate_pair` and report every returned error while retaining its existing registry/link/family-route checks. Update `.github/workflows/validate.yml` to run:

```yaml
- name: Test time-first contract
  run: python -m unittest discover -s tests -v
- name: Validate bilingual entry and registry
  run: python scripts/validate_reading.py
```

Run:

```bash
python -m unittest discover -s tests -v
python scripts/validate_reading.py
```

Expected: all tests pass; validator exits 0 with no warnings/errors.

- [ ] **Step 7: Self-review and commit**

Verify there is no fixed `6–8`/`8–10` Timeline bound, no empty digest link, no public candidate state, no fabricated day precision, no missing local link, and no sibling route that loses `#field-map` intent.

Commit:

```bash
git add docs/superpowers/specs/2026-08-20-agent-maintained-time-first-radar-v2-design.md docs/superpowers/plans/2026-08-20-time-first-radar-v2-benchmark.md docs/RADAR_AGENT_PROTOCOL.md docs/DAILY_WORKFLOW.md CURATION.md SCHEMA.md README.md README.en.md digests/README.md scripts/timefirst_contract.py tests/test_timefirst_contract.py scripts/validate_reading.py .github/workflows/validate.yml
git commit -m "Add agent-maintained time-first benchmark radar"
```
