# Curation Policy

## What this Radar is for

This repository has two jobs at once:

1. **Frontier radar** — surface new benchmarks and material protocol changes quickly enough that a researcher can see what the field is starting to care about.
2. **Benchmark genealogy** — preserve the precursor, foundation, and transition benchmarks needed to understand *why* the frontier now measures those things.

The public map is comprehensive within these three areas. Once a work provides a verifiable, reusable benchmark, it stays visible even when its contribution is incremental or overlaps an existing evaluation coordinate. Importance and evolution roles express how much it changed the field; they do not decide whether an in-scope benchmark disappears from the list. Papers that merely run experiments on existing benchmarks are still outside the repository.

## Inclusion test

Include a work when the benchmark/evaluation suite is itself a reusable research contribution. It should define a task, environment, dataset, protocol, diagnostic, challenge, or evaluator target that other systems can meaningfully run against.

A paper is **not** included merely because it reports experiments on Agent Memory, RAG, or Data Agents.

For recent releases, reusability and scope are the inclusion gate. Novelty affects the importance score, genealogy, and whether the work receives a deeper explanation, but not whether it appears in the rolling timeline. Historical backfill gives priority to landmarks and missing links while retaining every verified benchmark already accepted into the registry.

## Evolution role

Every accepted benchmark receives one role from `SCHEMA.md`: `precursor`, `foundation`, `transition`, or `frontier`.

When reviewing a benchmark, ask explicitly:

1. **What previous benchmark is this implicitly criticizing?** What was too easy, narrow, static, synthetic, opaque, or weakly diagnosed?
2. **What changed in capability × environment × protocol?** More examples alone are not a new evaluation object.
3. **Did the field actually inherit the change?** A benchmark can be useful without being a landmark; record that distinction through role and importance rather than omission.
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

README is the public reading surface and should support two reading directions:

- **Latest → field signal:** every accepted benchmark in a rolling six-month window, in reverse chronological order, and what new concern it reveals.
- **Foundation → frontier:** per-area evolution chains showing how the problem definition changed.

The recent timeline is not editorially sampled: derive it from the registry's latest `last_verified` date, move six months back, and retain the full boundary month when release precision is only monthly. A recent benchmark must not be deferred merely because a nearby benchmark measures something similar. Do not let recency push durable foundations out of the repository. Once a benchmark is accepted into the canonical registry, keep it visible in the complete chronological and area tables; table length is not a reason to hide it.

## Research synthesis

Weekly/monthly/yearly compactions should synthesize changes in the **evaluation landscape**, not concatenate benchmark summaries. Useful theses include: which capabilities are now well measured, where evaluation is becoming more realistic, which old assumptions are being rejected, where benchmarks disagree because they measure different objects, and what missing benchmark would be most decision-relevant next.
