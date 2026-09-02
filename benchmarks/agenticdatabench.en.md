# AgenticDataBench: fine-grained skills behind realistic data-science tasks

[中文](agenticdatabench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2607.01647) · [Project](https://agenticdatabench.github.io/) · [Code](https://github.com/AgenticDataBench/AgenticDataBench)

## What it actually measures

AgenticDataBench evaluates realistic data-science tasks while attaching **fine-grained skill labels** to the required work. It covers 344 tasks across 15 domains, 97 real-world datasets totaling 27.3 GB / 123.1M rows, and 433 ground-truth skill labels.

## What changed relative to prior evaluation

End-to-end data-science benchmarks reveal whether a task succeeded but often provide weak coverage accounting. AgenticDataBench adds a skill taxonomy so benchmark composition and agent weakness can be analyzed at finer granularity.

## Decisive evidence

The benchmark supports both a DevSet for standardized result submission and a TestSet where agent code is sandbox-executed and traces are captured. Human performance is reported around 84–90%, preserving substantial but not unreachable headroom.

## What the score supports

Skill-level results can show coverage and recurring weak competencies. They do not prove that a skill label is an independent causal module: one task can require interacting skills, and agent scaffolding determines how those skills appear in trajectories.

## Fair comparison contract

Fix dataset version, sandbox, tool availability, agent harness, model, and execution budget. Compare skill distributions as well as aggregate accuracy, and preserve the hidden TestSet when making tuning decisions.

## What remains unmeasured

Skill labels are an ontology chosen by benchmark designers; production business semantics, longitudinal data change, collaboration, and data governance are only partially represented.

## Next discriminating validation

Use the skill labels to construct matched task pairs differing in exactly one required competency, then test whether targeted agent interventions improve only the predicted slice. That would validate the taxonomy as a diagnostic instrument.

## Genealogy

`end-to-end data tasks → skill-labeled coverage → capability-targeted data-agent improvement`

AgenticDataBench makes “what kinds of data work are actually covered?” measurable.