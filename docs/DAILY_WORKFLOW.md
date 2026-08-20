# Daily Benchmark-Maintenance Workflow

This is the authoritative orchestration contract for Agent Benchmark Radar. The recurring scheduler should stay short and point here.

## Role of this repository

Agent Benchmark Radar is the **default entry point** to the Radar family and the horizontal **evaluation layer** across Agent Memory, Agentic RAG, and Data Agents. It should route readers into the domain radars rather than duplicate their method surveys.

## Transaction

One run is one idempotent transaction:

`preflight → recent discovery + bounded historical backfill → independent benchmark judgment → protocol audit → canonical registry update → genealogy/library update → derive Chinese/English reader surfaces → editorial review → conditional compaction → validate → log → notify only if material`

## 1. Preflight

Read `CURATION.md`, `SCHEMA.md`, `docs/RADAR_FAMILY.md`, `docs/EDITORIAL_STANDARD.md`, the current README pair, Benchmark Library pair, `data/benchmarks.json`, digests index, and recent run logs.

Repair registry/README drift before adding new work.

## 2. Discovery

Search both:

- **Recent frontier:** new benchmark papers/releases, major protocol/evaluator revisions, contamination/saturation findings, executable environments, public artifacts, and independent validity evidence.
- **Bounded historical backfill:** missing predecessors repeatedly cited by current frontier work or necessary to explain a genealogy.

Cover naming drift around agent memory, long-term/procedural/multimodal memory, RAG/agentic retrieval/search/deep research, data agents/data science agents/analytics/database agents, plus benchmark/evaluation/dataset/challenge/leaderboard terms.

Prefer primary sources.

## 3. Independent judgment

When supported, separate roles:

- discovery optimizes recall;
- benchmark judge decides whether the evaluation object itself is reusable/important;
- protocol auditor extracts capability, environment, accessible state, tools, harness assumptions, hints, retries, stopping rule, metrics/judge, executable validation, and cost;
- genealogy analyst identifies the closest predecessor and what limitation is being criticized;
- measurement skeptic names the strongest confounder and still-unmeasured dimension;
- editor decides whether the change belongs on the public entry surface.

## 4. Inclusion and attribution

A benchmark enters when it defines a reusable task/environment/dataset/protocol/diagnostic/evaluator target and has either durable landmark value or frontier measurement value.

For every accepted candidate ask:

`what becomes measurable? → compared to what? → what does the score causally support? → strongest confounder? → what remains unmeasured?`

Leaderboard differences remain system-level evidence unless relevant conditions are sufficiently matched.

## 5. Canonical-first update

Update `data/benchmarks.json` before public prose. Preserve identity, aliases/version lineage, area, release date, importance, evolution role, capability/environment/protocol, measurement strength, coverage gap, confounders, verified artifacts, and last verification.

Then update benchmark notes/genealogy only when they add decision value.

## 6. Chinese-first bilingual publication

- `README.md` is Simplified Chinese default; `README.en.md` is the full English counterpart.
- Benchmark Library and high-value public synthesis are bilingual.
- Chinese and English derive from one semantic benchmark judgment; never curate separate inclusion or genealogy decisions by language.
- Material corrections update both languages in the same transaction.
- Keep benchmark/paper/model/metric/protocol/tool names in canonical English when useful for precision/search.

## 7. README projection

The first screen should make the family structure obvious and expose: New & Notable, area evolution, domain-radar continuations, and the fact that benchmark coverage is not the whole field.

Default reader flow:

`Frontier → Field Evolution → Area Maps → Poorly Measured → Reading Paths → Benchmark Library`

New & Notable includes only changes that materially alter the evaluation object. High-value changes may receive 60–90 second folds.

Each area map defaults to 4–6 defining benchmarks plus frontier signal and biggest measurement gap; full genealogy belongs in disclosure/library rather than a permanently expanded table.

## 8. Cross-Radar contract

- First screen links to Agent Memory, Agentic RAG, and Data Agent radars.
- Each area map ends with exactly one canonical continuation to its domain radar.
- Domain radar methods are not duplicated here.
- `What Is Still Poorly Measured` stays first-class so measurable problems are not confused with important problems.

## 9. Editorial review

Apply `docs/EDITORIAL_STANDARD.md`. Review adjacent benchmark explanations together for repeated sentence skeletons, generic praise, and machine-translated Chinese. Detect pattern density, not isolated words.

## 10. Compaction

Weekly/monthly/yearly compactions synthesize **changes in the evaluation object**, not a list of new datasets. Track which capabilities/environments/protocols become better measured, which former frontier roles become foundations/dead ends, and where validity/reproducibility tensions change.

## 11. Validation and log

Check:

- registry syntax/required fields and README synchronization;
- Chinese default + English counterpart cross-link and preserve the same benchmark identities, roles, primary links, and load-bearing facts;
- default genealogy entries have meaningful predecessor/delta logic;
- high-importance historical benchmarks remain reachable through non-temporal library routes;
- area maps route to the correct sibling radar;
- no operational/scheduler internals leak to public surfaces;
- `What Is Still Poorly Measured` remains visible;
- component claims respect harness/model/budget confounding.

Write one compact `runs/daily/YYYY/MM/DD.md` log.

## Notification gate

Notify only for an important newly accepted benchmark, a newly identified foundation that changes genealogy, a protocol/evaluator/validity correction that changes interpretation, a meaningful compaction, or an exact blocker. Otherwise finish silently.
