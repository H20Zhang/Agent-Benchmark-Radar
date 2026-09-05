# RAGCap-Bench: intermediate capabilities inside agentic RAG

[中文](ragcap-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2510.13910)

## What it actually measures

RAGCap-Bench evaluates **intermediate tasks and capabilities** that recur inside agentic RAG workflows rather than scoring only the final answer. The benchmark taxonomy is derived from observed system outputs, recurring tasks, and typical failure patterns.

## What changed relative to prior evaluation

End-to-end RAG scores turn planning, retrieval, reasoning, and intermediate decision errors into one black box. RAGCap-Bench makes those latent abilities explicit so a failure can be associated with a capability class rather than inferred from the final answer alone.

## Decisive evidence

The paper reports that slow-thinking models with stronger RAGCap performance also achieve better end-to-end agentic-RAG outcomes. This correlation is evidence that the chosen intermediate tasks capture useful competencies rather than arbitrary micro-benchmarks.

## What the score supports

Capability scores can diagnose likely weaknesses and compare models under standardized micro-tasks. They do not prove that improving one capability will causally improve a deployed RAG system; interface, tools, and orchestration determine whether the capability is realized.

## Fair comparison contract

Fix prompt/harness, backbone version, tool descriptions, and per-task budget. When relating RAGCap to end-to-end performance, use matched systems and resource budgets; otherwise a larger agent scaffold can create both higher micro-scores and higher final scores.

## What remains unmeasured

Capability decomposition may miss emergent coordination effects, and benchmark micro-tasks can become easier than the messy state in real trajectories. Cost, stopping, and error recovery remain system-level properties.

## Next discriminating validation

Intervene on one weak capability while holding the rest of the agent fixed, then test whether predicted end-to-end failures decrease. That is the needed step from correlation to causal diagnostic value.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use RAGCap-Bench to isolate intermediate capabilities in agentic RAG. Their practical value depends on predicting behavior in real workflows. Higher scores on decomposed tasks should not be presented as better end-to-end search without a transfer check.

### What a concrete task looks like

Illustrative task: a system solves a local retrieval-planning, intermediate-reasoning, or evidence-assessment problem rather than an entire user request. Such tasks improve diagnosis but may remove error accumulation and state dependence present in the full workflow.

### Most discriminating experiment

Hold a complete system fixed and replace only a component improved on one local capability. Test whether local and end-to-end scores move together. Evaluate on system-generated intermediate states as well as reference states to expose sensitivity to upstream errors.

### Pair with

[agenticragtracer](agenticragtracer.en.md) · [browsecomp-plus](browsecomp-plus.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`final RAG score → capability decomposition → intervention-based agent diagnosis`

RAGCap-Bench is useful insofar as its intermediate coordinates predict what to fix.