# Curation Policy

This policy is the Benchmark-specific acceptance layer for [Radar Agent Protocol v2](docs/RADAR_AGENT_PROTOCOL.md) and [the Daily Benchmark adapter](docs/DAILY_WORKFLOW.md). Candidates remain private until the protocol's evidence and skeptical-audit gates are complete; normal Daily Agent publication does not wait for a human approval step.

## What this Radar is for

This repository has two jobs at once:

1. **Frontier radar** — surface new benchmarks and material protocol changes quickly enough that a researcher can see what the field is starting to care about.
2. **Benchmark genealogy** — preserve the precursor, foundation, and transition benchmarks needed to understand *why* the frontier now measures those things.

The public registry is comprehensive within these three areas. Once a work defines a verifiable, reusable benchmark, it remains reachable even when its contribution is incremental or overlaps an existing coordinate. Importance and evolution role express how much it changed the field; they do not decide whether an accepted benchmark disappears. Papers that merely run experiments on existing benchmarks remain out of scope.

## Inclusion test

Include a work when the benchmark/evaluation suite is itself a reusable research contribution. It should define a task, environment, dataset, protocol, diagnostic, challenge, or evaluator target that other systems can meaningfully run against.

A paper is **not** included merely because it reports experiments on Agent Memory, RAG, or Data Agents.

For recent releases, reusability and scope are the inclusion gate. Novelty controls importance, genealogy, and depth of explanation, not acceptance. Historical backfill prioritizes landmarks and missing links while retaining every verified benchmark already accepted into the canonical registry.

## Evolution role

Every accepted benchmark receives one role from `SCHEMA.md`: `precursor`, `foundation`, `transition`, or `frontier`.

When reviewing a benchmark, ask explicitly:

1. **What previous benchmark is this implicitly criticizing?** What was too easy, narrow, static, synthetic, opaque, or weakly diagnosed?
2. **What changed in capability × environment × protocol?** More examples alone are not a new evaluation object.
3. **Did the field actually inherit the change?** A benchmark can be useful without being a landmark; record the distinction through role and importance rather than omission.
4. **What does the new benchmark still fail to measure?** Every generation should make the next missing coordinate visible.

Roles are not prestige labels. `frontier` is time-relative: as an idea becomes durable it may later become a `foundation` or `transition` anchor.

## Daily discovery

Search broadly enough to catch naming drift: `agent memory`, `long-term memory`, `experience memory`, `multimodal memory`, `RAG benchmark`, `agentic retrieval`, `search agent`, `deep research`, `data agent`, `analytics agent`, `data science agent`, `database agent`, `semantic data analysis`, plus benchmark/evaluation/dataset/challenge/leaderboard terms.

Use two discovery windows:

- **Recent window:** new benchmark papers, releases, challenges, protocol revisions, evaluator changes, contamination findings, and independent validity evidence.
- **Historical backfill:** landmark benchmarks repeatedly cited as predecessors or exposed as missing links in an evolution chain.

Prefer primary sources: paper, official benchmark repository, official dataset/leaderboard, and conference/challenge pages. Product/vendor claims are useful only as leads or protocol evidence, not as the sole source for benchmark metadata.

## Review gate

For each candidate answer five questions before acceptance:

1. **What new thing becomes measurable?** If the answer is only “the same task with more examples,” importance should be low unless scale fixes a known validity problem.
2. **Compared to what?** Identify the nearest existing benchmark and the actual delta in capability, environment, or protocol.
3. **What does a score causally support?** Separate system-level performance from claims about memory, retrieval policy, planning, or data tooling.
4. **What is the strongest confounder?** Model version, tool interface, hints, retries, LLM judge, synthetic data artifacts, contamination, environment drift, or lifecycle cost are common examples.
5. **What is still not measured?** Every accepted benchmark should have one explicit coverage gap.

## Change types worth publishing

Treat these as first-class updates, not only brand-new benchmark papers:

- material dataset/version releases;
- corrected labels or contamination findings;
- evaluator/judge changes that shift conclusions;
- new executable environments or public data;
- leaderboard protocol changes;
- independent evidence that a benchmark is saturated, brittle, or harness-sensitive;
- a newly identified historical anchor that changes how the current frontier should be interpreted.

## README contract

README starts with a compact **onboarding layer** that routes readers by research area, followed by a small **Evaluation Recipes** decision-support layer, then the **signal-first, table-first research surface**. Onboarding and recipes are navigation/selection aids rather than research-trend synthesis. “Time-first” means that the newest research is easiest to scan; it does **not** mean that Radar-maintenance timestamps replace the research chronology or that one card is rendered per paper. Keep onboarding stable and short: title, one-sentence value proposition, language switch, lightweight status badges, and three area routes to each area’s map, recipes, and complete registry.

The main README must preserve three high-bandwidth scan surfaces:

- **Evaluation recipes:** maintain a compact decision table for each area that maps common research claims to one Core benchmark, complementary coverage, and one explicit remaining inference gap. Keep 3–5 recipes per area. Recipes are curated starting points, not rankings, exhaustive experimental suites, or substitutes for reading protocol/confounder metadata.
- **Recent release timeline:** every verified in-scope benchmark in the rolling six-month release window, ordered by source `released` date/month in reverse chronology. Preserve honest month precision, retain the whole boundary month when necessary, impose no fixed item cap, and do not editorially sample the table.
- **Complete area tables:** all accepted Agent Memory, RAG / Agentic Retrieval, and Data Agent benchmarks remain directly visible in README, with role, release time, and one concise measurement-object description. Do not add a parallel research-delta column. Table length is never a reason to move these rows only to the Library.
- **Evolution / reading routes:** compact synthesis may sit around the tables, but it must route through the same canonical records rather than replace them.

`radar_published_at` remains first-class **publication provenance** for the autonomous maintainer: it records when the Radar accepted a native-v2 record and can support acceptance-window audits, period synthesis, and map-delta reasoning. It is not the reader-facing publication date and must never reorder the primary release timeline. Never infer it from `released`, `last_verified`, a scheduler run, or a later integration commit.

Do not publish per-item `<details>` deep reads in the main README. Question, Evidence, Caveat, Map, predecessor, and genealogy detail belongs in canonical notes, the Benchmark Library, and closed-period digests. The Library remains the canonical complete backstop and alternate browse surface, not a dumping ground used to thin the README.

Each accepted event also receives the `map_delta` status defined in `SCHEMA.md`. One work may be an `early_signal`; it cannot by itself establish a durable trend or silently rewrite a Field Map node.

## Research synthesis

Weekly/monthly/yearly compactions should synthesize changes in the **evaluation landscape**, not concatenate benchmark summaries. Useful theses include: which capabilities are now well measured, where evaluation is becoming more realistic, which old assumptions are being rejected, where benchmarks disagree because they measure different objects, and what missing benchmark would be most decision-relevant next.
