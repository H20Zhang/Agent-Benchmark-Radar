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
