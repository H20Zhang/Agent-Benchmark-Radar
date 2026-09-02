# SGR-Bench: search where the correct website is not enough

[中文](sgr-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.22219) · [Dataset](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)

## What it actually measures

SGR-Bench evaluates **state-gated retrieval**: answer-bearing evidence becomes available only after an agent reaches the right specialized site and configures the correct filters, hierarchy, scope, or view. The task therefore includes retrieval-state control, not just source discovery.

## What changed relative to prior evaluation

Web benchmarks often count reaching a relevant source as substantial progress. SGR-Bench shows that specialized data portals behave more like interactive query interfaces: the same site can expose the wrong slice of data unless the agent establishes the correct state.

## Decisive evidence

The benchmark has 100 expert-curated tasks across six source families and 12 public data ecosystems, with paired constraint-guided and goal-oriented formulations. The strongest evaluated system reaches 66.18% item-level F1 while row-level F1 remains much lower. In 156 analyzable failed CLI trajectories, retrieval-scope drift accounts for 37.2% and criterion mismatch 27.6%; final answer composition is only 10.3%.

## What the score supports

This is strong evidence that source discovery and retrieval-state control are distinct capabilities. The result remains browser/harness dependent because interacting with site controls is part of the measured system.

## Fair comparison contract

Fix site snapshot/time, browser/tool interface, agent model, action budget, and task formulation. Report item-level and row-level F1 and preserve constraint-guided versus goal-oriented variants; explicit filters in the prompt materially change the planning burden.

## What remains unmeasured

The setting is narrower than general deep research and is sensitive to public-site UI drift. Authentication, private enterprise tools, write operations, and arbitrary document retrieval are outside the core protocol.

## Next discriminating validation

Expose a canonical structured API for the same data and compare it with browser interaction. The gap would quantify how much failure comes from semantic query planning versus GUI/interface grounding.

## Genealogy

`find the source → configure retrieval state → execute semantic data query`

SGR-Bench links search-agent evaluation directly to semantic query processing.