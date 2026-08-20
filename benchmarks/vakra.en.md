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

## Genealogy consequence

`document retrieval / API use in isolation → multi-hop agent trajectories → cross-source executable coherence under policy`

VAKRA pushes RAG evaluation from finding relevant evidence toward maintaining coherent executable information state across heterogeneous tools.
