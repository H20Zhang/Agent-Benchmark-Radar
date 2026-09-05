# AI4AI-Bench: learning-algorithm design behind a source-patch boundary

[中文](ai4ai-bench.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.20318) · [Code and tasks](https://github.com/Einsia/AI4AI-Bench) · [Released trajectories](https://lab.einsia.ai/ai4ai/trajectories/)

Agents explore a cheap proxy for four hours, submit only a source patch, and then face a fresh formal training run whose frozen evaluator was unavailable during exploration.

## What it follows

MLAgentBench measures iterative ML experimentation; MLE-bench and MLE-Dojo broaden end-to-end ML engineering. AI4AI-Bench makes a narrower critique: an unrestricted final score does not show whether an agent improved the learning algorithm or only tuned run-side settings and infrastructure. It freezes ten real training repositories and makes the source patch the boundary between exploration and evaluation.

## How it is evaluated

**Question:** Can an agent diagnose and improve a learning algorithm rather than merely optimize the way an existing implementation is run?

**Measurement object:** repository diagnosis, experimental iteration, source-level algorithm modification, clean-start training performance, and the submitted patch's run-side versus learning-side classification.

**Scale and protocol:** ten repositories span ten algorithm families. Each agent explores for four hours on one B300 with a cheap proxy; only its source patch enters a fresh formal environment for up to twelve hours. The shipped baseline is rerun with the same hardware, budget, evaluator, and assets. Heterogeneous task metrics are normalized so 0 is uninformative, 0.1 is the shipped baseline, and 1 is a stated optimum. All 290 evaluated trajectories are public.

## What a score can support

Across 290 cells, the mean normalized score is 0.166, the best system averages 0.250, and 124 cells fall below the shipped baseline. Among 263 changed submissions, learning-side patches average 0.226 versus 0.126 for run-side-only patches. These are system-level and selected-group differences: they show that the protocol exposes substantial room beyond run configuration, not that a learning-side edit causally adds 0.100.

## Strongest confounder

Learning-side submissions are observationally selected: stronger systems reach that layer more often, and the paper explicitly disclaims a causal interpretation. A separate LLM classifies patch families without reported reliability. Systems bundle model, harness, and reasoning effort; proxy and final stages are separated by access and time but are not always sample-disjoint.

## Remaining Gap: What remains uncovered

Ten B300-scale tasks are expensive, there is no human baseline, and the common score encodes heterogeneous task utility. The repository supports self-hosted final evaluation but currently operates no blind service, so third parties cannot reproduce the official hidden-boundary enforcement.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use AI4AI-Bench for learning-algorithm modification rather than unrestricted score optimization. Source patches and clean-start formal training help isolate durable changes, while independence between proxy feedback and formal evaluation still needs scrutiny. A small expensive task set limits statistical confidence.

### What a concrete task looks like

Illustrative task: an agent diagnoses training and edits code in a proxy environment, then hands off only source patches for fresh formal training. Temporary files and trained state cannot substitute for code changes without changing the evaluation object.

### Most discriminating experiment

Match proxy and formal-training budgets, pin baseline reruns and patch boundaries, and verify multiple seeds. Treat patch categories as descriptive rather than causal. Algorithmic mechanism claims still require targeted ablations and transfer to independent tasks.

### Pair with

[deltaml-bench](deltaml-bench.en.md) · [mle-bench](mle-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy consequence

`map_delta=early_signal`, bound to `data-agent-research-integrity`. It isolates learning-algorithm design more tightly than broad ML-agent suites, but one record does not change the durable defining chain.
