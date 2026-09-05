# MemBench: expanding memory evaluation beyond answer accuracy

[中文](membench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2506.21605) · [Code](https://github.com/import-myself/Membench)

## What it measures

MemBench covers factual and reflective memory, separates participation from observation scenarios, and evaluates effectiveness, efficiency, and capacity rather than only task accuracy. Its question is therefore not merely whether an agent can recall information, but whether memory remains useful and affordable across different memory levels and interaction roles.

## Compared with what

LoCoMo and LongMemEval made long-history QA harder and more diagnostic. MemBench adds orthogonal axes for memory level, interaction scenario, and resource behavior. A method should therefore not be called a better memory system solely because it tops one QA dataset while spending substantially more memory or behaving differently under observation versus participation.

## Decisive evidence and score boundary

The important contribution is the evaluation decomposition itself: the same memory system is inspected across factual/reflective memory, participation/observation, and effectiveness/efficiency/capacity. The primary sources do not provide a stable public leaderboard that can defensibly be treated as a single current SOTA ranking, so the Radar does not manufacture an Overall track. System results are comparable only under matched backbone, harness, and metric aggregation.

## Fair comparison conditions

Align the backbone, agent harness, memory budget, interaction scenario, and aggregation rule. If one system obtains higher effectiveness by consuming more tokens or capacity, accuracy alone does not support an architecture-level claim.

## Next evaluation coordinate

MemBench broadens what gets measured but still does not isolate which write, organization, retrieval, or update mechanism caused the outcome. Matched component interventions and long-term maintenance cost are the next useful coordinates.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use MemBench to profile a memory system across effectiveness, capacity, and cost. Breadth does not itself identify a component contribution. Treat task slices and resource curves as primary results rather than comparing only bundled-system totals.

### What a concrete task looks like

Illustrative task: a system remembers interactions it participated in, uses information it only observed, and derives a higher-level conclusion from repeated experiences. The same storage budget may favor factual retention over reflective information, so these should be inspected separately.

### Most discriminating experiment

With one answerer, sweep memory capacity and report quality, write cost, and retrieval latency separately for factual and reflective tasks. An advantage that appears only with more capacity is not evidence of better organization; add capacity- and query-budget-matched controls.

### Pair with

[memoryagentbench](memoryagentbench.en.md) · [evomembench](evomembench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
