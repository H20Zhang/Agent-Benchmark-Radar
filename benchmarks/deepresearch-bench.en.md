# DeepResearch Bench: moving from finding an answer to producing a citable research artifact

[中文](deepresearch-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2506.11763) · [Code](https://github.com/Ayanami0730/deep_research_bench)

## What it measures

DeepResearch Bench uses 100 PhD-level research tasks across 22 fields to evaluate multi-step web research, evidence collection, citation accuracy/effectiveness, and long-form report quality. The evaluation object is an analyst-like research artifact rather than a short answer.

## Compared with what

BrowseComp stresses search persistence but does not require a complete research deliverable. DeepResearch Bench connects retrieval, citation, and synthesis, making “plausible answer with unsupported citations” a separately observable failure.

## Decisive evidence and score boundary

The evaluator itself continues to evolve. The official repository switched to GPT-5.5 in May 2026 and maintained separate leaderboards during migration; GPT-5.5 evaluator overall alignment is reported around 71.82 versus a human IAA reference around 68.78. That makes evaluator generation a load-bearing protocol variable. Radar should not merge agent scores from old and new judges into one current ranking.

## Fair comparison conditions

Align task set, search provider, report budget, citation extraction, judge generation, and scoring rubric. Every evaluator version needs its own dated protocol track.

## Next evaluation coordinate

One hundred expensive tasks measure systems well but make causal attribution hard. Stronger evaluation needs replayable evidence snapshots and component interventions that separate search, source selection, writing, and citation verification.
