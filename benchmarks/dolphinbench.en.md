# DolphinBench: testing history-dependent actions under frozen memory

[中文](dolphinbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.24971) · [Code](https://github.com/mem0ai/dolphinbench) · [Project](https://dolphinbench.ai)

## What it measures

DolphinBench evaluates three simulated knowledge-work personas, each with roughly 500K tokens of user messages and 200 tasks, for 600 tests overall. The target is a correct action in a work application, not merely a verbal recollection. Its applications are simulated; action-grounded evaluation should not be described as evidence from a production deployment. [Official overview](https://github.com/mem0ai/dolphinbench/blob/main/README.md)

## Compared with what

Compared with LoCoMo, historical information must support task completion. Compared with evaluations of continued learning across episodes, the standard test freezes the ingested memory so that one test cannot teach the next. This isolates utility of the existing history, not improvement over the 200-test sequence.

## Evaluation protocol

Messages are ingested chronologically through the tested agent's normal memory interface. Processing must complete before a checkpoint is recorded. Each test starts a fresh conversation and fresh application state while memory remains frozen; trajectories, actions, and grader evidence are retained. Certification requires two successes with relevant history and two failures without it for the specified certification agent. That is a conditional selection test, not proof that every possible model needs the history. [Canonical protocol](https://github.com/mem0ai/dolphinbench/blob/main/docs/CANONICAL_EVALUATION.md)

## Decisive evidence and score boundary

The decisive evidence reviewed here is the public, executable state-isolation and grading protocol. This Radar has not independently rerun the 600 tasks. Differences between ingestion agents, providers, and answer models do not isolate a retriever effect. Official materials include older single-persona reference results alongside newer configuration summaries: interpret a score with its exact model, coverage, checkpoint, and recovery records rather than merging those releases into one ranking.

## Confounders and remaining coverage gaps

The strongest confounders are the ingestion model, asynchronous provider processing, and certification agent. Dates spanning years inside messages are not years of real provider operation and do not validate real-time decay. Separate ingestion, maintenance, and query costs, specify amortization, and keep missing costs distinct from zero. Three simulated users leave cross-user transfer, permission changes, and long-running online learning unmeasured.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it to test whether long-term user context improves stateful workflows and whether that benefit survives lifecycle cost accounting.

### What a concrete task looks like

Illustrative task: prior messages identify a project contact and standing constraint; a new request requires updating the project in an application rather than merely repeating the remembered constraint.

### Most discriminating experiment

Hold the writer, executor, interfaces, and graders fixed; compare no memory, budget-matched retrieval, and supplied relevant history. Report action success, evidence access, and total cost separately. Treat test-time memory updates as a different protocol rather than pooling them with frozen-memory scores.

### Pair with

[locomo-conv](locomo-conv.en.md) · [memoryarena](memoryarena.en.md) · [mem2actbench](mem2actbench.en.md)

<!-- RESEARCH-DECISION:END -->

---

Evidence checked: 2026-09-23. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.
