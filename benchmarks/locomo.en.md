# LoCoMo: making very-long-term conversational memory measurable

[中文](locomo.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://aclanthology.org/2024.acl-long.747/) · [Code](https://github.com/snap-research/locomo)

## What it measures

LoCoMo moves memory evaluation from short dialogue context to genuinely multi-session histories: conversations average roughly 600 turns and 16K tokens and can span 32 sessions. It evaluates QA, event summarization, and multimodal dialogue generation, so the target includes long-range temporal and causal reasoning rather than only retrieving one remembered sentence.

## Compared with what

Many earlier long-context tests were closer to needle retrieval or single-document understanding. LoCoMo instead accumulates information through coherent interaction and asks models to use that history across multiple downstream tasks. It therefore became a foundation for later benchmarks such as LongMemEval and MemoryAgentBench. The benchmark establishes long-term history as a separate evaluation coordinate; it does not validate one particular memory architecture.

## Decisive evidence and score boundary

The ACL paper reports that long-context LLMs and RAG improve performance, yet models still substantially trail humans on lengthy conversations and long-range temporal/causal dynamics. This supports the measurement claim that simply enlarging a context window does not solve long-term memory. It does not identify whether a gain came from writing, indexing, retrieval, the answerer, or the judge. The Radar therefore keeps third-party LoCoMo scores with incompatible question sets or judges out of one artificial leaderboard.

## Fair comparison conditions

Comparisons must align the LoCoMo question/version, answerer or reader, retrieval budget, visible history, and the evaluator used for QA or summarization. LLM-as-judge choices and filtering can materially shift absolute numbers, so one Overall score is not sufficient evidence for a memory-component claim.

## Next evaluation coordinate

LoCoMo mostly asks what happened in the past. The next step is to test whether remembered experience changes future actions and planning, while separating update, forgetting, conflict handling, and maintenance cost from end-to-end QA accuracy.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LoCoMo as an entry point for long-term conversational memory, not as sole evidence that an agent improves through experience. Separate accessibility of historical information from its effect on future behavior; this benchmark primarily informs the former.

### What a concrete task looks like

Illustrative task: an early conversation describes a move, a later session updates work plans, and the current question asks how the events relate in time. The system must retain the person, chronology, and event links; retrieving a sentence with matching keywords may still be insufficient.

### Most discriminating experiment

Hold the answerer and question set fixed; compare full history, budget-matched retrieved snippets, and supplied supporting evidence. Report both evidence recall and answer quality. A retrieval-to-supplied-evidence gap motivates work on memory access; failure in both conditions instead directs attention to reading and temporal reasoning.

### Pair with

[longmemeval](longmemeval.en.md) · [memoryarena](memoryarena.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
