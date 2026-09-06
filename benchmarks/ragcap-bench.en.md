# RAGCap-Bench: intermediate capabilities inside agentic RAG

[中文](ragcap-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2510.13910)

## What it actually measures

RAGCap-Bench evaluates intermediate tasks inside agentic RAG rather than only the final answer: planning, evidence extraction, grounded reasoning, and noise robustness. Its multiple-choice questions come from system trajectories and recurring failure patterns, making an end-to-end failure easier to diagnose.

## What changed relative to prior evaluation

End-to-end RAG scores turn planning, retrieval, reasoning, and intermediate decision errors into one black box. RAGCap-Bench makes those latent abilities explicit so a failure can be associated with a capability class rather than inferred from the final answer alone.

## Decisive evidence

Under the paper v2 informative-prompt protocol (Table 3), DeepSeek-R1 records the highest Overall F1 in the reported comparison, 81.05%. Strict exact match tells a different story: evidence extraction reaches 42.02% with Gemini-3.1-Pro, while grounded reasoning reaches 57.23% with Qwen3-235B-A22B. Aggregate F1 above 80% therefore does not mean that a model completes intermediate steps without errors.

The reported correlation with end-to-end agentic RAG supports diagnostic relevance, not a causal guarantee that improving one micro-task improves the deployed system. [Versioned source: Table 3](https://arxiv.org/html/2510.13910v2#S4.T3).

## What the score supports

Capability scores can diagnose likely weaknesses and compare models under standardized micro-tasks. They do not prove that improving one capability will causally improve a deployed RAG system; interface, tools, and orchestration determine whether the capability is realized.

## Fair comparison contract

Fix prompts, evaluation version, and run count. Paper v2 Table 3 uses informative prompts and averages three runs; bare prompts are a different setting. When relating these capabilities to end-to-end performance, also align the agent framework, tools, and resource budget. A larger scaffold can otherwise improve both scores without establishing component-level causality.

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