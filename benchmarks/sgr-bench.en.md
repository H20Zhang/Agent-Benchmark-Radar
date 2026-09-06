# SGR-Bench: search where the correct website is not enough

[中文](sgr-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.22219) · [Dataset](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)

## What it actually measures

SGR-Bench evaluates **state-gated retrieval**: answer-bearing evidence becomes available only after an agent reaches the right specialized site and configures the correct filters, hierarchy, scope, or view. The task therefore includes retrieval-state control, not just source discovery.

## What changed relative to prior evaluation

Web benchmarks often count reaching a relevant source as substantial progress. SGR-Bench shows that specialized data portals behave more like interactive query interfaces: the same site can expose the wrong slice of data unless the agent establishes the correct state.

## Decisive evidence

The benchmark has 100 expert-curated tasks across six source families and 12 public data ecosystems, with paired constraint-guided and goal-oriented formulations. In the reported CLI evaluation, GPT-5.5 obtains 66.18% Item-F1 but only 43.37% Row-F1: recovering individual fields is not the same as preserving complete, correctly scoped rows. The evaluated commercial systems use their own product interfaces, not the same CLI harness.

Among 156 analyzable failed CLI trajectories, retrieval-scope drift accounts for 37.2%, criterion mismatch for 27.6%, and final answer composition for 10.3%. These percentages describe the audited failure subset, not all tasks or commercial systems. [Paper v1, main results and Appendix E](https://arxiv.org/html/2605.22219v1#S4).

## What the score supports

This is strong evidence that source discovery and retrieval-state control are distinct capabilities. The result remains browser/harness dependent because interacting with site controls is part of the measured system.

## Fair comparison contract

Fix the site snapshot or collection time, task formulation, retrieval tools, model, and action budget. Report Item-F1 and Row-F1 separately and retain the constraint-guided / goal-oriented split. CLI agents and manually operated commercial products belong to different system configurations; these results are not model-only rankings.

## What remains unmeasured

The setting is narrower than general deep research and is sensitive to public-site UI drift. Authentication, private enterprise tools, write operations, and arbitrary document retrieval are outside the core protocol.

## Next discriminating validation

Expose a canonical structured API for the same data and compare it with browser interaction. The gap would quantify how much failure comes from semantic query planning versus GUI/interface grounding.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use SGR-Bench for stateful retrieval where finding the website is not enough to expose the correct view. It separates source discovery from configuring filters, hierarchy, or scope within that source. Static page recall is not a substitute for task completion.

### What a concrete task looks like

Illustrative task: an agent reaches the correct data portal but must configure time, geography, and hierarchy to expose the requested records. Data from a wrong view may be true and citable while failing the requested scope.

### Most discriminating experiment

Supply the correct site, retrieval state, and complete target evidence in separate controls. Fix browser tools and site snapshot or verification date, then report item- and row-level quality to locate gains in source discovery, state control, or extraction.

### Pair with

[gisa](gisa.en.md) · [data-exploration-benchmark](data-exploration-benchmark.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`find the source → configure retrieval state → execute semantic data query`

SGR-Bench links search-agent evaluation directly to semantic query processing.