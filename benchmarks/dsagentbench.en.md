# DSAgentBench: End-to-End Data Science in Real Computer Environments

[中文](dsagentbench.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.10366) · **Area: Data Agent**

> **Measurement delta.** DSAgentBench moves data-agent evaluation from isolated SQL/code/analysis stages to complete data-science workflows inside real computer environments, with multi-tool execution grounded in intermediate outputs.

## Predecessor / implicit critique

Earlier benchmarks commonly isolate Text-to-SQL, code generation, analysis answers, or individual tool operations. That misses OS grounding, tool orchestration, long-horizon dependency, and artifact-level verification.

## What it actually measures

The benchmark contains **275 tasks** spanning wrangling, exploration, modeling, visualization, and validation. Agents interact with real computing tools such as notebooks, IDEs, terminals, browsers, and databases. Deterministic evaluators verify analytical correctness, visual outputs, and model performance rather than code execution alone.

## What a score supports

The paper reports **56.70% task success** for the strongest evaluated agent, while open-source agents remain below 1%. This is primarily **end-to-end system-level evidence**: model capability, tool reliability, OS grounding, planning, recovery, and harness all contribute.

It does not isolate a planning or routing component.

## Strongest confounder

Harness and computer-use stack are tightly coupled with model capability. Cross-agent leaderboard gaps can therefore reflect scaffolding and recovery policy as much as reasoning. Real-computer realism also introduces environment/tool-version drift.

## What remains unmeasured

Persistent multi-session project state, enterprise business semantics, clarification/approval, deployment monitoring, authority/permissions, irreversible actions, and full lifecycle cost remain outside the core protocol.

## Genealogy consequence

`executable code → workflow-oriented data-agent evaluation → real-computer end-to-end execution`

DSAgentBench is best read as a frontier environment/protocol shift, not as a clean component-performance coordinate.
