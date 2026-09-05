# DA-Code: grounded executable code for real data-analysis tasks

[中文](da-code.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2410.07331) · [Project](https://da-code-bench.github.io/)

## What it actually measures

DA-Code evaluates generation of **grounded executable data-science code** over real and diverse data, covering difficult wrangling, exploratory analysis, and machine-learning operations in a controlled execution environment.

## What changed relative to prior evaluation

DS-1000 uses realistic library-level coding problems. DA-Code raises the unit of work toward agentic data analysis: tasks require grounding in supplied datasets, planning several operations, and producing the required answer through complex data-science programs rather than filling a local code hole.

## Decisive evidence

The benchmark's evaluation suite is manually designed for robust executable checking. Even using the strongest contemporary LLMs in the authors' experiments, accuracy reaches only 30.5%, showing a large gap despite the tasks being objectively executable.

## What the score supports

DA-Code supports grounded program synthesis for bounded analysis tasks. It still does not measure the full data-agent loop of discovering the question, inspecting intermediate outputs over many turns, maintaining project state, and delivering a user-facing artifact.

## Fair comparison contract

Fix data files, runtime/library versions, allowed languages/tools, execution budget, retry policy, and answer evaluator. Distinguish one-shot generation from iterative agent repair; execution feedback can materially change the task.

## What remains unmeasured

Repository-scale engineering, heterogeneous documentation, business semantics, long-lived state, and open-ended insight discovery sit outside the core benchmark.

## Next discriminating validation

Construct paired tasks where the same target requires either one monolithic program or a multi-step inspect-and-repair workflow. This isolates the value of agentic iteration beyond stronger code generation.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DA-Code for grounded planning and executable code over real data rather than linguistic form. Wrangling, exploration, and modeling produce different outputs. Overall accuracy alone does not show whether gains arise from data understanding, generation, or recovery.

### What a concrete task looks like

Illustrative task: an agent builds a pipeline grounded in task data, correcting types or missing values before analysis or training. Executable code can silently discard important rows and produce a semantically wrong result.

### Most discriminating experiment

Pin data and runtime, report wrangling, exploration, and ML slices, and add supplied-correct-data-summary controls. Match debugging attempts and distinguish executable runs from correct outputs so execution rate is not mistaken for analysis quality.

### Pair with

[ds-1000](ds-1000.en.md) · [datascibench](datascibench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`library-level code → grounded multi-operation analysis code → iterative data-analysis agent`

DA-Code is a bridge between executable coding benchmarks and full data-agent workflows.