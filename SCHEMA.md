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
- `artifacts`: verified first-party paper/code/data/leaderboard links only
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
