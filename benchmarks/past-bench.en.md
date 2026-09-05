# PAST-Bench: Agent Memory / cross-episode causal attribution

[中文](past-bench.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.04003) · [Code](https://github.com/Gen-Verse/PAST-Bench)

Moves from visible-history recall to whether persistence causally improves later executable tasks.

## What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** After context clearing, does retained state actually cause better downstream task performance?

**Measurement object:** Paired persistent-state benchmark that tests whether retained cross-episode experience causally improves later executable work.

**Scale and protocol:** 26 task families and 204 executable episodes with paired persistence controls. The protocol includes persistence-on-off-pairs, matched-seeds-prompts-graders, artifact-and-trace-evidence.

## What a Score Can Support

Across 26 families and 204 episodes, persistence-on/off runs match seeds, prompts, and graders and retain artifact/trace evidence. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Generated tasks and closely related graders can create model-family template familiarity, and the study does not cover months-long deployment. The load-bearing confounders are task-generator-model-family, grader-coupling, tool-harness.

## What It Still Does Not Measure

Generated tasks and graders may favor related frontier coding-model templates, and the study remains short of months-long deployment.

## Where It Fits in the Map

`map_delta=early_signal`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use PAST-Bench for paired causal evidence that persistent state benefits later tasks. Saving files is not the target; the question is whether the same later task changes when earlier state is retained. Conclusions remain bounded by the generated task distribution.

### What a concrete task looks like

Illustrative task: an earlier episode produces reusable experience and a fresh agent session handles a related task. Prompts, seeds, and graders are matched, with access to prior state as the key difference, enabling measurement of the net persistence effect.

### Most discriminating experiment

Retain paired persistence-on/off runs and add length-matched irrelevant state and raw trajectories. Report paired differences, task-family slices, and full-cycle cost. Benefits that survive controls for extra text and computation support a contribution from experience content itself.

### Pair with

[memoryarena](memoryarena.en.md) · [agent-memory-bench-coding](agent-memory-bench-coding.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
