# Research Radar Reading Architecture v1

Date: 2026-08-20

## Problem statement

Agent Benchmark Radar already has a strong conceptual spine: new benchmarks reveal what the field has started to care about, while historical benchmarks explain how today’s evaluation target emerged. The main remaining problem is navigation depth. New & Notable scans well, but long per-area tables will keep growing; benchmark genealogy, current frontier, measurement gaps, and protocol caveats compete for the same README space. The repository also lacks a stable note/editorial standard comparable to the paper radars.

This design turns the repository into a layered benchmark reading system that supports fast frontier scanning, field learning, genealogy, protocol audit, and historical lookup without requiring a standalone website.

Scope: root README, benchmark-note contract, benchmark genealogy/library navigation, compactions, editorial standard, validation, and the recurring workflow that derives public surfaces.

Non-goals: GitHub Pages/frontend work; maximizing benchmark count; replacing official benchmark documentation; treating leaderboard rank as component evidence; forcing every benchmark into an equally detailed note.

## Design principles

1. **Scan the frontier; expand the reason.** New benchmarks should be easy to scan, while important ones expose a 60–90 second explanation of what newly became measurable.
2. **Genealogy is causal, not chronological decoration.** Historical benchmarks remain only when they explain a durable shift in capability, environment, protocol, validity, or cost.
3. **One record, several views.** README, benchmark notes, research library, and compactions provide different projections of the same canonical benchmark record.
4. **Measurement claims need confounders.** Every important benchmark interpretation names what a score supports and what the harness/protocol prevents us from attributing.
5. **Structure is stable; prose is not templated.** Use a consistent reasoning contract without repetitive AI sentence skeletons.

## External writing basis

The design follows Google Technical Writing guidance on key points first, audience fit, progressive disclosure, and organizing large information collections into navigable views; Microsoft’s “scanning first, reading second” principle; and NeurIPS checklist/reviewer guidance that claims, scope, assumptions, evidence, reproducibility, and limitations should align.

Third-party plain-writing and research-writing skills are design references only. The repository-local editor and validator are authoritative so the daily workflow does not depend on an external skill being installed.

## Reading architecture

```text
canonical benchmark registry
  ├─ 30 sec: README New & Notable row
  ├─ 60–90 sec: README fold for high-value benchmark changes
  ├─ 5–10 min: benchmark note / protocol audit
  ├─ topic view: Benchmark Library + genealogy
  └─ time view: weekly → monthly → yearly evaluation compaction
```

## README contract

Use this top-level order:

```text
New & Notable
What Benchmark Evolution Says About the Field
Field Maps: Memory / RAG / Data Agents
Reading Paths
Benchmark Library / Browse All
What Is Still Poorly Measured
Research Compactions
About / Contributing
```

Expose depth navigation near the title:

`30 sec: Frontier · 5 min: Field Evolution · 15 min: Reading Paths · Browse All`

Keep the current core idea: a useful new benchmark is often an implicit critique of what the previous generation failed to measure. Keep the comparison rule that higher leaderboard score is system-level evidence unless model, accessible state, tools, prompts/hints, retries, stopping rule, evaluator, and relevant budgets are sufficiently matched.

### New & Notable

Keep roughly 6–10 recent benchmark changes that materially alter the evaluation object. Include benchmark releases, major protocol/evaluator revisions, contamination/saturation findings, and newly recovered historical foundations when they change current interpretation.

Each row answers:

- what is newly measurable;
- what previous limitation it exposes;
- what field signal follows.

Importance >= 4/5, or a benchmark/protocol change that alters a current genealogy, receives an inline `<details>` explainer. The fold should cover these information points naturally in 3–5 short paragraphs:

- previous benchmark/control it implicitly criticizes;
- capability × environment × protocol delta;
- what a score does and does not support;
- strongest validity/confounder issue;
- why this changes the field map.

Do not repeat a future benchmark note verbatim.

### Field evolution

Keep one compact area-level evolution arrow for Agent Memory, RAG / Agentic Retrieval, and Data Agents. The arrow should tell a causal story: what target became too narrow or easy, and which new coordinate replaced it.

### Area field maps

Do not render the full historical registry as one permanently expanded table. Each area defaults to:

- one-line evolution chain;
- 4–6 defining benchmarks covering precursor/foundation/transition/frontier;
- current frontier signal;
- biggest current measurement gap.

Place the full genealogy in `<details>` or link to the Benchmark Library. This keeps foundations visible without making the first read exhaustive.

### Reading Paths

Use three or four paths maximum, framed as questions such as `How did long-term memory move from recall to action?`, `How did retrieval evaluation become a stateful control problem?`, or `How did data-agent evaluation move from SQL/code to real workspaces?`.

## Benchmark Explainer Standard

High-visibility benchmark notes follow this reasoning contract:

1. **Measurement delta** — the smallest change that makes the benchmark worth knowing.
2. **Predecessor / implicit critique** — closest prior benchmark and what was missing, too easy, too static, too synthetic, or too weakly diagnosed.
3. **What it actually measures** — capability, environment, accessible state, task, and target behavior.
4. **Protocol** — tools/interfaces, model/harness assumptions, hints, retries/trials, stopping rule, metrics/judge, executable validation, and relevant cost budgets.
5. **What a score supports** — system-level claim versus any justified component-level attribution.
6. **Strongest confounder / validity risk** — contamination, saturation, judge dependence, environment drift, hidden hints, harness sensitivity, synthetic shortcuts, or lifecycle cost.
7. **What remains unmeasured** — the next missing coordinate made visible by this benchmark.
8. **Genealogy consequence** — precursor/foundation/transition/frontier role and nearest continuation.

Use a note only when it adds decision value. A large registry does not imply a large collection of prose files.

## Editorial standard

Create a repository-local Research Radar Editor contract shared in spirit with the paper radars.

Preferred prose:

- concrete nouns for capability, environment, protocol, evaluator, and artifacts;
- comparisons before adjectives;
- one research claim per paragraph;
- explicit causal boundaries (`this is a system-level result`, `the protocol does not isolate retrieval policy`);
- numbers only when they change interpretation;
- simple language for benchmark purpose before protocol detail.

Avoid:

- repetitive openers such as `the important thing is not...` or `this matters because...` across every entry;
- generic praise without comparison/evidence;
- describing benchmark scale as novelty when the evaluation object is unchanged;
- marketing language, emoji-heavy decoration, and inflated labels such as `groundbreaking` or `comprehensive` without support;
- treating `frontier` as a prestige label rather than a time-relative analytical role.

A deterministic editorial linter should warn on repeated sentence skeletons, generic judgments without nearby comparison/evidence, duplicated prose across surfaces, and structural drift. It should not ban words mechanically.

## Benchmark Library

Time-based digests are not the historical index. Maintain three discovery routes:

- **Browse by Area** — Agent Memory; RAG / Agentic Retrieval; Data Agents.
- **Browse by Genealogy** — `precursor → foundation → transition → frontier`, with nearest-predecessor relationships and the limitation each successor exposed.
- **Browse by Measurement Coordinate** — capability, environment, protocol, validity/reproducibility, cost, action/decision impact, multimodality, persistent state, and other controlled coordinates.

A compact **Browse by Year** view remains available for chronology and provenance.

Every important historical benchmark must remain reachable through at least one non-temporal route. Weekly/monthly/yearly synthesis explains changes; it does not own discoverability.

## Layer responsibilities

- `data/benchmarks.json`: canonical benchmark identity, area, evolution role, capability/environment/protocol, measurement strength, coverage gap, confounders, artifacts, verification.
- benchmark notes when present: protocol/evidence audit layer.
- Benchmark Library/genealogy: historical retrieval and evolution layer.
- `digests/*`: temporal synthesis of evaluation-object shifts.
- root README: frontier judgment/router layer.
- `runs/*`: maintenance provenance only.

Do not duplicate the same paragraph across layers.

## Maintenance workflow

Move detailed recurring behavior into a repository-owned `docs/DAILY_WORKFLOW.md`. The scheduler should become a thin entry point.

Each transaction follows:

`preflight → recent discovery + bounded historical backfill → independent benchmark judgment → protocol audit → canonical registry update → note/genealogy update when useful → derive README/library/compaction projections → editorial review → validate → log → notify only if material`

A new benchmark does not automatically become a defining benchmark in the default area view. Default genealogy changes only when the new work shifts a durable evaluation coordinate.

## Validation

Add deterministic checks for:

- README top-level section order and New & Notable bounds;
- fold eligibility and required semantic coverage;
- every README benchmark exists in the canonical registry;
- every default genealogy entry has a valid evolution role and a meaningful predecessor/delta explanation;
- every high-importance historical benchmark is reachable through the Benchmark Library;
- no maintenance/scheduler/schema internals leak to public surfaces;
- repeated house-style lead-in warnings and high-similarity paragraph warnings;
- registry/README synchronization, dates, links, role validity, measurement-strength versus coverage-gap separation, and component-attribution discipline continue to pass.

Editorial lint is advisory unless a deterministic public/canonical contract is violated.

## Migration

1. Rebuild README around progressive depth while retaining the current useful New & Notable and core comparison rule.
2. Collapse long per-area history into defining benchmarks + current frontier + measurement gap; preserve full genealogy behind disclosure/library navigation.
3. Add a Benchmark Library with area, genealogy, measurement-coordinate, and year routes.
4. Add the local Research Radar Editor standard and editorial linter.
5. Add `docs/DAILY_WORKFLOW.md` and move stable recurring behavior out of the scheduler prompt.
6. Add/upgrade benchmark notes selectively for frontier works and foundations whose protocol/genealogy is otherwise easy to misunderstand.
7. Preserve old benchmarks in canonical data; do not delete history merely to shorten README.

## Success criteria

A reader should be able to:

- identify the newest meaningful evaluation shifts within 30 seconds;
- understand why a high-value new benchmark exists in 60–90 seconds without leaving README;
- trace a current frontier benchmark back to the predecessor limitation it addresses;
- find historical benchmarks by area, genealogy, or measurement coordinate rather than publication week;
- tell what a score supports and what the protocol confounds;
- read repeated benchmark explanations without a templated AI house style.

The maintainer should be able to change reader/editorial contracts in repository files while the recurring automation prompt stays short and stable.