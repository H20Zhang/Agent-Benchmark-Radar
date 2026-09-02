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
