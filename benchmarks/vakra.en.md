# VAKRA: Cross-Source Executable Agent Evaluation

[中文](vakra.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.12282) · [Code](https://github.com/IBM/VAKRA) · **Area: RAG / Agentic Retrieval**

> **Measurement delta.** VAKRA combines API interaction, multi-hop reasoning, document retrieval, and natural-language tool-use policy inside one **executable trajectory**, testing whether agents maintain identity, grounding, and policy consistency across access modes.

## Predecessor / implicit critique

API, RAG, and tool-policy benchmarks often evaluate primitives separately. That does not establish that an agent can compose them reliably inside an enterprise-like workflow.

## What it actually measures

VAKRA exposes **8,000+ locally hosted executable APIs across 62 domains** and covers diverse API interaction styles, 1–3-hop structured API reasoning, and multi-turn API + RAG tasks with policy constraints. Predicted tool calls are re-executed, allowing multiple valid paths.

## What a score supports

A fixed ReAct harness reduces some architecture confounding. The best model reports **70.4%** on single-hop endpoint-style tasks, roughly **50–51%** on compositional APIs, and as low as **2.4%** in some policy-constrained unanswerable settings.

Trace analysis points to entity disambiguation and cross-source grounding rather than tool invocation mechanics alone. Still, scores remain model + fixed-harness system evidence, not direct evidence for a retrieval or planner component.

## Strongest confounder

Fixing the ReAct harness makes model comparison cleaner but also binds conclusions to one interface/controller contract. API schema, policy wording, and document collections affect difficulty as well.

## What remains unmeasured

Component attribution, persistent long-horizon state, live API drift/permissions, tool latency/cost, irreversible external actions, and recovery remain open.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use VAKRA for composition of executable APIs, document evidence, and natural-language tool policies. A fixed ReAct harness controls system variation but primarily supports comparisons within that harness. New agent architectures need separately matched interface and budget experiments.

### What a concrete task looks like

Illustrative task: an enterprise-style request requires retrieving a policy document, calling an API for state, and composing the result while respecting call constraints. A correct answer with an invalid call, or a successful call grounded to the wrong entity, should not be conflated with success.

### Most discriminating experiment

Remove document evidence, API results, or tool policy separately to verify task dependence, then swap models within the same harness. For tool-retrieval research, fix the visible tool inventory so a smaller candidate set is not mistaken for large-scale tool-selection competence.

### Pair with

[crag](crag.en.md) · [data-agent-benchmark](data-agent-benchmark.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy consequence

`document retrieval / API use in isolation → multi-hop agent trajectories → cross-source executable coherence under policy`

VAKRA pushes RAG evaluation from finding relevant evidence toward maintaining coherent executable information state across heterogeneous tools.
