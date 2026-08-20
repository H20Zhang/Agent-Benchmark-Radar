# Curation Policy

## What this Radar is for

This repository has two jobs at once:

1. **Frontier radar** — surface new benchmarks and material protocol changes quickly enough that a researcher can see what the field is starting to care about.
2. **Benchmark genealogy** — preserve the precursor, foundation, and transition benchmarks needed to understand *why* the frontier now measures those things.

The goal is therefore not maximum benchmark count. **Completeness means covering the meaningful changes in the evaluation object.** A benchmark can be old and still be essential if newer benchmarks are best understood as responses to its limitations.

## Inclusion test

Include a work when the benchmark/evaluation suite is itself a reusable research contribution. It should define a task, environment, dataset, protocol, diagnostic, challenge, or evaluator target that other systems can meaningfully run against.

A paper is **not** included merely because it reports experiments on Agent Memory, RAG, or Data Agents.

A candidate can enter through either gate:

- **Landmark value:** it established or materially redirected an evaluation coordinate system, even if it predates today's agent framing.
- **Frontier value:** it makes an important capability, environment, protocol, validity issue, or cost dimension newly observable.

## Evolution role

Every accepted benchmark receives one role from `SCHEMA.md`: `precursor`, `foundation`, `transition`, or `frontier`.

When reviewing a benchmark, ask explicitly:

1. **What previous benchmark is this implicitly criticizing?** What was too easy, narrow, static, synthetic, opaque, or weakly diagnosed?
2. **What changed in capability × environment × protocol?** More examples alone are not a new evaluation object.
3. **Did the field actually inherit the change?** A benchmark can be interesting without being a landmark.
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

- **Latest → field signal:** the newest important benchmarks and what new concern they reveal.
- **Foundation → frontier:** per-area evolution chains showing how the problem definition changed.

Do not let recency push durable foundations out of the repository. Once a benchmark is accepted into the canonical registry, keep it visible in the complete chronological and area tables; table length is not a reason to hide it. Curation still controls what enters the registry, so completeness does not mean adding every historical dataset.

## Research synthesis

Weekly/monthly/yearly compactions should synthesize changes in the **evaluation landscape**, not concatenate benchmark summaries. Useful theses include: which capabilities are now well measured, where evaluation is becoming more realistic, which old assumptions are being rejected, where benchmarks disagree because they measure different objects, and what missing benchmark would be most decision-relevant next.
