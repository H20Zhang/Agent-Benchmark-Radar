# Agent Memory Bench: causal memory reuse in coding agents

[中文](agent-memory-bench-coding.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Code, tasks, preregistration, and pilot](https://github.com/GiulioDER/agent-memory-bench)

## What it actually measures

Agent Memory Bench measures whether **experience from earlier repository tasks causally improves later coding action**. Instead of loosely comparing an agent configured with memory against one without it, the protocol inserts a pluggable memory layer under a neutral, verbatim session feed and hidden executable grading, while checking whether the memory integration is valid and whether memory is actually available and used in later sessions.

## What changed relative to predecessors

PAST-Bench and related work already move memory evaluation from QA toward future action. Agent Memory Bench adds **treatment validity** as an explicit protocol concern. A common hidden failure in memory experiments is that “memory enabled” in system configuration does not mean the agent actually saw, retrieved, or used the memory during the task. Integration hashes and proof-of-treatment gates attempt to verify treatment receipt separately from downstream success.

## Decisive evidence

The public corpus contains **24 real-repository tasks, 24 precursor transcripts, and 99 distractors**. Arms share the same baseline and verbatim session feed; before hidden executable oracles score the result, integration hashes and proof-of-treatment gates verify that memory is actually available and used. Ingestion/session cost and negative transfer are recorded explicitly. The current preregistered pilot leaves only **13 surviving cases** and estimates a gain of just **+0.014 over a CLAUDE.md baseline**, with an interval crossing zero.

## What the score supports

The current pilot supports only the statement that, for these survivors in a Claude-specific environment with the evaluated memory product, there is not yet sufficient evidence of a stable positive effect. It does **not** show that memory cannot help coding agents: the sample is far below target power, proof-of-treatment creates a survivor set, and the Recall memory product is author-built. The stronger contribution at this stage is the causal-evaluation protocol rather than a product ranking.

## Fair comparison contract

Coding agent/backbone, repository/task, session feed, tool permissions, execution budget, memory-ingestion timing, retrieval visibility, and executable grader should be fixed. Every memory method should report integration success, treatment exposure, task success, negative transfer, and total cost. If results are reported only for cases where memory integration succeeds, the survivor rate must also be reported so integration failures do not disappear from the evaluation object.

## How to use it in research

The most transferable idea is **proof-of-treatment + executable outcome + cost accounting**. A memory mechanism that claims to improve coding or data agents should first establish that memory was actually retrieved and used, then compare action utility under a matched baseline. “Memory is enabled in the configuration” is treatment assignment, not evidence that treatment was received.

## Next discriminating validation

The largest gaps are statistical power, cross-backbone/harness transfer, and independence from an author-built treatment. The highest-leverage next study would expand the number of real repository tasks, run the same neutral-feed protocol across multiple coding agents, and preregister both intention-to-treat and treatment-on-treated estimands. That would preserve integration failures while still answering whether memory helps when it is genuinely used.

## Genealogy

`map_delta=reinforces`, bound to `memory-action-utility`. It independently strengthens the causal-treatment direction represented by PAST-Bench, while the current null result does not alter the defining chain. The benchmark contract worth carrying forward is: **verify that memory was used before claiming a causal memory benefit**.
