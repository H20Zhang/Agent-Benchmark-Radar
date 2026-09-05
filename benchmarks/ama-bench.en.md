# AMA-Bench: memory over agent-environment trajectories

[中文](ama-bench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.22769) · [Project](https://ama-bench.github.io/) · [Code](https://github.com/AMA-Bench/AMA-Bench)

## What it actually measures

AMA-Bench evaluates memory over **agent-environment trajectories** rather than human-agent conversation alone. Questions require recall, causal inference, state updating, and state abstraction over histories containing actions, observations, and changing environment state.

## What changed relative to prior evaluation

LoCoMo and LongMemEval establish long conversational memory but their histories are primarily communication artifacts. AMA-Bench changes the source of memory to machine-generated experience: what the agent did, what the environment returned, and how state changed. This makes causality and objective state more central than conversational phrasing.

## Decisive evidence

The project reports 206 trajectory samples, 2,471 QA pairs, six domains, and four target capabilities: Recall, Causal Inference, State Updating, and State Abstraction. Its AMA-Agent reaches 57.22% average accuracy, 11.16 percentage points above the strongest reported baseline, using a causality graph plus tool-augmented retrieval.

## What the score supports

The benchmark supports memory reasoning over stored trajectories and suggests that causal structure plus active retrieval can help. The method gain remains system-level evidence: graph construction, retrieval tools, backbone, and answerer all change together. Moreover, the endpoint is still QA about experience rather than success on a future environment task.

## Fair comparison contract

Fix trajectory set, backbone, retrieval/tool budget, evidence visibility, and QA evaluator. Report per-capability results because a system strong on raw recall may still fail state abstraction or causal inference. Tool-augmented systems should disclose extra search calls and latency.

## What remains unmeasured

The benchmark only indirectly tests whether remembering a trajectory improves later acting. Long-running error accumulation, experience deletion, policy learning, and transfer to unseen environments remain separate questions.

## Next discriminating validation

Take the same trajectories and evaluate a paired future task whose optimal action depends on the remembered causal/state information. This would connect trajectory QA to the more consequential criterion: behavior improvement.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use AMA-Bench for memory of agent execution trajectories rather than only personal facts in dialogue. Causal relations among tool outputs and environment states matter. Answering questions about a stored trajectory still does not establish better action on a new task.

### What a concrete task looks like

Illustrative task: an agent invokes a tool, observes a state change, and adjusts its next action; a later question asks why the state arose. The memory must connect action, feedback, and consequence rather than retrieve only the final state description.

### Most discriminating experiment

Compare full trajectories, observations alone, and preserved action–feedback pairs on the same questions. Then use the memory in related executable tasks and report action gains separately. This separates trajectory understanding from experience transfer.

### Pair with

[longmemeval-v2](longmemeval-v2.en.md) · [memoryarena](memoryarena.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`conversation history → agent trajectory → causal/state memory of experience`

AMA-Bench is a bridge from conversational memory benchmarks toward memory for acting agents.