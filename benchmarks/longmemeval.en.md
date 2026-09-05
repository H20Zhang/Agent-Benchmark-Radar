# LongMemEval: separating long-term memory into five capabilities

[中文](longmemeval.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2410.10813) · [Code](https://github.com/xiaowu0162/LongMemEval)

## What it measures

LongMemEval uses 500 high-quality questions embedded in scalable, timestamped user-assistant histories to test information extraction, multi-session reasoning, knowledge updates, temporal reasoning, and abstention. Rather than presenting one static long document, the protocol models history as interactions that arrive over time and must be absorbed before later questions are asked.

## Compared with what

LoCoMo established that very long multi-session dialogue is difficult. LongMemEval goes further by separating update and abstention from generic recall and by using attribute-controlled history construction that can scale context length. A high factual-recall score therefore no longer implies that a system can replace stale knowledge or know when evidence is absent.

## Decisive evidence and score boundary

The official repository later cleaned history sessions to reduce interference with answer correctness, which is itself evidence that benchmark version is a load-bearing variable. The Radar does not collapse third-party LongMemEval numbers into an official leaderboard because answerers, retrieval top-k, judges, and dataset revisions often differ. Under a matched protocol, a score supports how much useful long-term evidence the system supplies; it does not isolate the causal effect of memory writing or retrieval.

## Fair comparison conditions

Lock the dataset/history version, reader or answerer, retrieval budget, and grader. Full-history, retrieval-only, and external-memory systems are different contracts. If the reader or top-k also changes, end-to-end accuracy is packaged-system evidence rather than a memory-component comparison.

## Next evaluation coordinate

LongMemEval still terminates in QA over history. LongMemEval-V2 later moves to agent-environment trajectories, workflow knowledge, and latency; the next stronger target is whether remembered experience improves future actions directly.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LongMemEval for persistent-assistant failures such as recalling a fact but using its superseded version. Its value lies in separating updates, temporal reasoning, and abstention. Category-level reporting is more diagnostic than treating one overall accuracy as a complete account of memory.

### What a concrete task looks like

Illustrative task: a user states a preference, explicitly revises it several sessions later, and then asks which arrangement now applies. The system must resolve the revision rather than pick between similar passages, and avoid guessing when the history provides insufficient evidence.

### Most discriminating experiment

Place both old and new facts in retrieved context and compare against a condition containing only the operative fact. Persistent failure with both facts available points beyond recall to conflict resolution or temporal interpretation. Report unanswerable questions separately so always-answer policies cannot hide their cost.

### Pair with

[statemembench](statemembench.en.md) · [scale-qa](scale-qa.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
