# Agent Memory Bench: causal memory reuse in coding agents

[中文](agent-memory-bench-coding.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Code, tasks, preregistration, and pilot](https://github.com/GiulioDER/agent-memory-bench)

## Question

Does a pluggable memory layer causally help a coding agent reuse prior repository-task experience under a neutral feed and executable grading?

## Evidence

The public corpus contains 24 real-repository tasks, 24 precursor transcripts, and 99 distractors. Arms share a baseline and verbatim session feed; integration hashes and proof-of-treatment gates verify that memory was actually available and used before hidden executable oracles score the result. Ingestion and session cost and negative transfer are explicit. The current preregistered pilot leaves 13 surviving cases and estimates only +0.014 over a CLAUDE.md baseline, with an interval crossing zero.

## Caveat

The competing Recall memory product is author-built, the environment is Claude-specific, and proof-of-treatment creates a survivor set. The pilot is far below target power, so its null result is not evidence that memory cannot help coding agents.

## Map

`map_delta=reinforces`, bound to `memory-action-utility`. It independently strengthens the causal-treatment protocol introduced by PAST-Bench without rewriting the defining chain.
