# Benchmark Schema

`data/benchmarks.json` is the canonical machine-readable registry. Each record describes a benchmark as a **measurement instrument**, not merely as a paper citation.

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
