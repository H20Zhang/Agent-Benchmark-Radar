# Curation Policy

## Inclusion test

Include a work only when the benchmark/evaluation suite is itself a reusable research contribution. It should define a task, environment, dataset, protocol, or diagnostic that other systems can meaningfully run against.

A paper is **not** included merely because it reports experiments on Agent Memory, RAG, or Data Agents.

## Daily discovery

Search broadly enough to catch naming drift: `agent memory`, `long-term memory`, `experience memory`, `RAG benchmark`, `agentic retrieval`, `search agent`, `deep research`, `data agent`, `analytics agent`, `data science agent`, `database agent`, `semantic data analysis`, plus benchmark/evaluation/dataset/challenge/leaderboard terms.

Prefer primary sources: paper, official benchmark repository, official dataset/leaderboard, and conference/challenge pages. Product/vendor claims are useful only as leads or protocol evidence, not as the sole source for benchmark metadata.

## Review gate

For each candidate answer five questions before acceptance:

1. **What new thing becomes measurable?** If the answer is only “the same task with more examples,” importance should be low unless scale fixes a known validity problem.
2. **Compared to what?** Identify the nearest existing benchmark and the actual delta in capability, environment, or protocol.
3. **What does a score causally support?** Separate system-level performance from claims about memory, retrieval policy, planning, or data tooling.
4. **What is the strongest confounder?** Model version, tool interface, hints, retries, LLM judge, synthetic data artifacts, contamination, or lifecycle cost are common examples.
5. **What is still not measured?** Every accepted benchmark should have one explicit coverage gap.

## Change types worth publishing

Treat these as first-class updates, not only brand-new benchmark papers:

- material dataset/version releases;
- corrected labels or contamination findings;
- evaluator/judge changes that shift conclusions;
- new executable environments or public data;
- leaderboard protocol changes;
- independent evidence that a benchmark is saturated, brittle, or harness-sensitive.

## Research synthesis

Weekly/monthly/yearly compactions should synthesize changes in the **evaluation landscape**, not concatenate benchmark summaries. Useful theses include: which capabilities are now well measured, where evaluation is becoming more realistic, where benchmarks disagree because they measure different objects, and what missing benchmark would be most decision-relevant next.
