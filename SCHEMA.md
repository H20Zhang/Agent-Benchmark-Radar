# Benchmark Schema

`data/benchmarks.json` is the canonical machine-readable registry. Each record describes a benchmark as a **measurement instrument**, not merely as a paper citation.

This schema follows [Radar Agent Protocol v2](docs/RADAR_AGENT_PROTOCOL.md). The existing registry remains valid without a bulk historical rewrite; unknown legacy dates must not be fabricated.

## Required fields

- `id`, `name`, `area`, `released`, `importance`, `status`
- `evolution_role`: `precursor`, `foundation`, `transition`, or `frontier`
- `summary`: one-sentence description of the evaluated object
- `capabilities`: what competence is actually exercised
- `environment`: the state/data/tool substrate the agent interacts with
- `protocol`: how behavior is elicited and scored
- `scale`: human-readable task/data scale
- `measurement_strength`: the most important thing this benchmark makes observable
- `coverage_gap`: the most important capability or validity gap it leaves open
- `confounders`: variables that can invalidate naive leaderboard comparisons
- `artifacts`: verified first-party paper/code/data/leaderboard links only; `paper` keeps the preferred publication link while optional `preprint` may record the canonical arXiv version for identity resolution
- `last_verified`: date on which load-bearing metadata was checked

## v2 time and map fields

Untouched legacy records with none of these fields remain valid. Once any v2 field is present, the record must contain the complete explicit-legacy or native-v2 combination:

- `published_at`: earliest public version of the work or protocol event; strict UTC for native-v2, or the exact honest `released` month/day value for explicit legacy;
- `first_seen_at`: first observation of the canonical identity by this Radar; strict UTC for native-v2 and null for explicit legacy;
- `radar_published_at`: first accepted public publication in this Radar; strict UTC for native-v2 and null for explicit legacy;
- `time_provenance`: `native_v2` or `legacy_unknown`;
- `map_delta`: `none`, `early_signal`, `reinforces`, `revises`, `splits`, or `retires`.

Native-v2 timestamps use `YYYY-MM-DDTHH:MM:SSZ` and must satisfy `published_at <= first_seen_at <= radar_published_at`. The three events must not be copied from one another without evidence. Existing `released` values, including honest `YYYY-MM` precision, remain valid for untouched legacy records. Only the approved Timeline compatibility set is explicitly migrated with `published_at=released`, null discovery/Radar times, `time_provenance=legacy_unknown`, and `map_delta=early_signal`. A backfill preserves its historical publication time and uses the actual Radar acceptance time; a correction preserves original times and adds version/protocol history rather than overwriting them.

Native-v2 records used as rolling-period supports also declare `direction_keys`, a non-empty list of unique lowercase stable tokens. A support cited by a direction block with key `K` must carry `K` in `direction_keys`; two records count as same-direction reinforcement only when both carry the block's exact key. `direction_keys` by itself triggers the complete native-v2 time bundle. Native-v2 records not used as period supports may omit this adapter field. Explicit or implicit legacy records do not carry it, so this support binding does not trigger a bulk legacy rewrite.

`map_delta` is an event-level editorial judgment, not a prestige label. `early_signal` does not mutate a durable map. `reinforces` requires independent evidence beyond one work. `revises`, `splits`, and `retires` require the prior map claim, new evidence, and the smallest reversible edit.

## Citation metadata

Every registry record carries a `citations` object so the complete area tables can expose a consistent, auditable influence signal without turning citation count into a quality ranking:

- `count`: Semantic Scholar citation count, or `null` when no paper can be matched;
- `source`: currently `semantic-scholar`;
- `updated_at`: `YYYY-MM-DD` refresh date;
- `status`: `ok`, `no-paper`, or `unmatched`;
- `paper_id` and `url`: the resolved Semantic Scholar paper identity when `status=ok`.

A real zero must remain `0`; unknown is `null`. Citation count is age- and source-dependent context only. It must not determine `importance`, `evolution_role`, genealogy, or frontier status.

## Evolution role

The Radar is meant to show how a field's definition of progress changes over time.

- **precursor** — predates the current agent framing but introduced an evaluation object that later work still inherits.
- **foundation** — a durable benchmark that established the modern problem definition or comparison coordinate system.
- **transition** — materially expanded realism, capability coverage, or protocol and helped move the field toward the current frontier.
- **frontier** — represents a current evaluation direction. This label is intentionally time-relative and should be revisited as the field matures.

Do not drop a benchmark merely because it is old. A foundation should remain visible when later benchmarks are best understood as responses to its limitations.

## Area vocabulary

Use one primary area: `agent-memory`, `rag`, or `data-agent`. Cross-cutting tags belong in `capabilities` and `environment`; do not duplicate a benchmark merely because it spans areas.

## Importance

Importance is not relevance. Use a 1–5 score based on whether the benchmark materially changes the field's evaluation coordinate system.

- **5:** field anchor or major shift in evaluated object, environment, or protocol.
- **4:** strong reusable benchmark with a meaningful diagnostic or realism improvement.
- **3:** useful but mostly incremental coverage.
- **2:** narrow/redundant; retain only when it fills a concrete gap.
- **1:** generally defer rather than publish.

## Comparison rule

Never compare headline scores unless the relevant model, tool interface, accessible context, retries/trials, hints, judge, stopping rule, and cost budget are sufficiently matched. When they are not matched, describe the result as a system-level result rather than evidence for a specific component.

## Publication-event contract (2026-09)

Website chronology and generated README projections use typed events, never the
conference month as a substitute for an earlier verified public version:

- `first_public_at`: earliest verified public version, or null when not established.
- `publication_at`: formal publication event, or null.
- `data_release_at`: separately evidenced data-release event, or null.
- `release_date_evidence`: each non-null event has a source URL, original date
  precision (`day` or `month`), evidence kind, verification status and, where
  established, verification date. Old values remain in `legacy_recorded_at`.

An unclassified legacy date remains usable for browsing but is explicitly labeled
as a recorded date whose event type needs review, **not** a verified first release.
Native-v2 provenance is imported without claiming a new audit. Correcting a date
retains its original value and its separately sourced publication event.
`released` remains a compatibility projection of the selected typed date; it does
not independently establish provenance. Unknown discovery times stay unknown.
`published_at` in the existing v2 event bundle has its original event semantics;
it is not the new formal-publication field `publication_at`.

Both README and website use the discovery cutoff from `data/freshness.json`.
The six-month window subtracts six calendar months; the 30-day window contains
exactly 30 inclusive UTC dates. Month-only records use interval overlap and are
labeled as month precision. A source audit does not silently refresh discovery,
citation, or result verification timestamps.

## Explicit facet membership

`facet_assignments` maps each facet id to its option ids. Public URL values are
`facet-id:option-id`; option identity is scoped to its facet. Membership is not
recomputed from display prose. Selections combine with OR within a group and AND
between groups. Imported assignments carry `facet_assignment_status=imported-heuristic`
and remain editorial suggestions, not independently verified capability claims.
A human correction changes these explicit assignments rather than editing prose
until a substring matcher happens to produce the desired result.

## Scope-bounded result presentation

A result track is a collection of source records, not proof that all experimental
controls match. `evidence_type=baseline` labels a baseline; a single entry is a
single recorded result; multiple entries can expose only the best **among recorded
results**. Always carry the method/model, source, result date and result verification
date. `live` means a periodically curated tracking snapshot, not a real-time feed.
The benchmark comparison tool compares designs and does not rank systems using
scores from different datasets. Reference targets do not drive research-opportunity
filters or implied attainable headroom.
