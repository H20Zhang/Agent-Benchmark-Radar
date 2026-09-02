# DSGym: a data-science agent benchmark that filters shortcut-solvable tasks

[中文](dsgym.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2601.16344) · [Code](https://github.com/fannie1208/DSGym)

## What it actually measures

DSGym is both a standardized **execution framework** and a curated suite for evaluating/training data-science agents across analysis, prediction, and domain-specialized tasks in self-contained environments.

## What changed relative to prior evaluation

The authors show that a substantial fraction of existing data-science benchmark tasks can be solved without using the supplied data. DSGym explicitly filters shortcut-solvable problems and standardizes environment interfaces, making data grounding and cross-benchmark comparison central.

## Decisive evidence

DSGym refines existing tasks and adds DSBio and DSPredict for bioinformatics and challenging prediction workloads. It also supports execution-verified trajectory synthesis; as a training case study, a 4B model trained on 2,000 generated examples outperforms GPT-4o on standardized analysis benchmarks.

## What the score supports

The benchmark strongly supports whether an agent can plan, implement, and validate analyses in a controlled execution environment. The training result is evidence for the framework's usefulness but not a general claim that smaller models dominate stronger models outside the standardized tasks.

## Fair comparison contract

Fix Docker/environment image, tools, datasets, metric implementation, agent scaffold, model, and execution budget. Preserve shortcut filters and report pass@k separately from average trajectory score.

## What remains unmeasured

Standardization trades away some messy production reality: enterprise semantics, permissions, evolving repositories, collaboration, and deployment are not the central focus.

## Next discriminating validation

Track performance before and after shortcut filtering for each benchmark source and publish the delta. This quantifies how much apparent data-agent progress was actually benchmark leakage or task solvability without data.

## Genealogy

`fragmented data-science benchmarks → grounded standardized gym → execution-verified agent training/evaluation`

DSGym treats benchmark validity and environment reproducibility as part of the research contribution.