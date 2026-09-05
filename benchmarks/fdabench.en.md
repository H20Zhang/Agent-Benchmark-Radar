# FDABench: analytical data agents over heterogeneous evidence

[中文](fdabench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Project](https://fdabench.github.io/)

## What it actually measures

FDABench evaluates data agents that answer analytical questions over **heterogeneous evidence**: structured databases, documents, web content, images, video, and audio. Tasks can require planning, tool use, reflection, and multi-agent workflows rather than one SQL/code call.

## What changed relative to prior evaluation

Text-to-SQL and notebook benchmarks usually start from one dominant data modality. FDABench makes source selection and cross-modal evidence composition part of the analytical workflow, then evaluates both outcomes and reasoning traces.

## Decisive evidence

The benchmark contains 2,007 tasks across 50+ domains, three task types, and multiple heterogeneous data sources. Its evaluation includes choice correctness, rubric-scored reports, DAG-based trace metrics, latency, and token cost, making resource use and workflow structure visible alongside answer quality.

## What the score supports

FDABench supports an end-to-end claim about multi-source analytical agents under a given scaffold. Its breadth does not isolate whether gains come from planning, retrieval, multimodal perception, tool execution, or the backbone model.

## Fair comparison contract

Fix accessible data sources, model, toolset, agent scaffold, latency/token budget, and evaluator. Separate deterministic choice tasks from rubric-scored report tasks and report trace/cost metrics; otherwise an expensive scaffold can dominate via more exploration.

## What remains unmeasured

Task-local data avoids longitudinal enterprise changes, permissions, writes, collaborative operations, and evolving semantic definitions. LLM-judged reports also introduce evaluator dependence.

## Next discriminating validation

Construct matched single-source and heterogeneous versions of the same analytical question and intervene on source routing. This would quantify the marginal difficulty created by cross-source integration rather than generic reasoning complexity.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use FDABench for analytical workflows across structured, document, and multimodal sources. Combining discovery, tools, and reporting improves breadth, but an aggregate across heterogeneous tasks can hide failure location. Preserve correctness, report quality, and resource-cost readouts.

### What a concrete task looks like

Illustrative task: an analysis needs tables, documents, and media, requiring an access plan and a synthesized conclusion. Missing a source type can produce a one-sided report, while a complete-looking report can still contain unsupported calculations or claims.

### Most discriminating experiment

Fix tools and backbone, slice by source combination and task type, and supply correct source sets to diagnose discovery. Keep choice, report, and trajectory scores separate and charge multimodal parsing costs so expensive preprocessing does not create an opaque advantage.

### Pair with

[dataspace](dataspace.en.md) · [kramabench](kramabench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`single-source analytics → heterogeneous evidence workflows → multi-source data-agent orchestration`

FDABench broadens the measurement object from query execution to evidence orchestration.