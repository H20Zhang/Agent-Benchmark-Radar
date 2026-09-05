# WorldMemArena: the full memory lifecycle in evolving multimodal worlds

[中文](worldmemarena.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.29341) · [Project](https://worldmemarena-mem.github.io/)

## What it actually measures

WorldMemArena evaluates multimodal agent memory over **evolving action-world trajectories** and explicitly separates four lifecycle stages: write, maintain, retrieve, and use. Gold memory points, state updates, distractors, and evidence chains make it possible to inspect whether the agent stored the right event, kept it current, surfaced it later, and actually used it for the final decision.

## What changed relative to prior evaluation

Long-memory QA often treats a history as a static corpus and evaluates only final answers. WorldMemArena treats memory as mutable state coupled to a changing world. Its Lifelong Evolution and Agentic Execution regimes make obsolete evidence, visual observations, and state transitions first-class rather than assuming that every past fact remains equally valid.

## Decisive evidence

The benchmark contains 400 multi-session multimodal tasks and compares long-context, manually constructed retrieval/external-memory systems, and dedicated memory harnesses. The analysis finds that better writing/storage does not automatically translate into end performance, visual evidence is underused, cross-domain reliability is unstable, and real trajectories are harder than simplified alternatives. This is direct evidence that memory quality is a pipeline property, not a retrieval score.

## What the score supports

The final score supports whole-system memory performance, while stage annotations provide stronger diagnostic evidence than end QA alone. Yet causal attribution still requires matched backbones and stage-level intervention: a system can retrieve the right evidence and fail at use, or write a good memory and later overwrite it incorrectly.

## Fair comparison contract

Fix backbone, trajectory, visual observations, session segmentation, memory budget, retrieval budget, and action protocol. Report write/maintenance cost as well as read-time cost. Comparisons should preserve access to the same modalities; converting images into richer captions for only one system changes the evidence channel.

## What remains unmeasured

The benchmark remains finite and task-scoped. Policy governance, deletion rights, cross-user boundaries, months-long storage economics, and catastrophic corruption recovery are not its primary target.

## Next discriminating validation

Run oracle interventions at each lifecycle stage and measure how much final task success is recovered. The resulting error budget—write versus maintain versus retrieve versus use—would directly guide systems research investment.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use WorldMemArena to locate failures in writing, maintenance, retrieval, or use of multimodal memory. Stage metrics are more diagnostic than one aggregate score, but stages depend on one another. A local gain does not automatically establish improved end-to-end action.

### What a concrete task looks like

Illustrative task: observations and actions change world state, and checkpoint questions require the operative state plus relevant visual evidence. An old observation may be faithfully retained but obsolete, so retrieval hits and memory freshness need separate evaluation.

### Most discriminating experiment

Replace writing, maintenance, or retrieval outputs with correct intermediate artifacts one stage at a time and measure the downstream effect. Fix the visual backbone, budgets, and sample set to identify which stage actually limits the system rather than only comparing local metrics.

### Pair with

[memeye](memeye.en.md) · [memprobe](memprobe.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`static history QA → mutable multimodal state → lifecycle-diagnostic memory`

WorldMemArena is important because it makes memory lifecycle decomposition observable instead of treating “memory” as one opaque module.