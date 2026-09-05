# DSAEval: cumulative, multimodal data-science projects

[中文](dsaeval.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2601.13591) · [Project](https://dsaeval.github.io/DSAEval/)

## What it actually measures

DSAEval evaluates agents on **real-world data-science projects** with multimodal environment perception, cumulative multi-query interaction, and separate assessment of reasoning, code, and results. It includes 641 problems grounded in 285 structured and unstructured datasets.

## What changed relative to prior evaluation

One-shot coding tasks reset state between queries. DSAEval makes later requests depend on earlier analysis and expands observations beyond tables into image/text data, closer to an iterative data-science session.

## Decisive evidence

Eleven advanced agentic LLMs are evaluated. The paper reports Claude-Sonnet-4.5 strongest overall, GPT-5.2 most efficient, and MiMo-V2-Flash most cost-effective; multimodal perception improves vision-related tasks by 2.04–11.30%. Structured/routine analysis is substantially easier than unstructured workloads.

## What the score supports

The benchmark supports cumulative project competence and exposes quality–efficiency–cost trade-offs. The model/scaffold is still a combined system, and multi-dimensional grading can contain evaluator assumptions beyond deterministic code execution.

## Fair comparison contract

Fix dataset, query order, accumulated workspace state, tool environment, model, budget, and evaluator. Preserve prior-query outputs exactly; resetting or summarizing history differently changes the cumulative task.

## What remains unmeasured

Long projects can span weeks, involve stakeholder feedback, data updates, version control, and production deployment. DSAEval's cumulative interactions are still bounded benchmark episodes.

## Next discriminating validation

Inject controlled mistakes early in a project and measure downstream recovery versus error propagation. This would test whether agents maintain trustworthy analytical state, not merely accumulate conversation context.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use DSAEval for multimodal data science in cumulative multi-query projects rather than independent questions. Earlier state affects later answers. Falling scores may reflect propagated errors rather than intrinsic difficulty of later queries.

### What a concrete task looks like

Illustrative task: an agent explores tabular, image, or text data and then models and interprets it over successive requests. An early cleaning or interpretation error can persist through the notebook and surface only in the final report.

### Most discriminating experiment

Compare cumulative autonomous execution with supplied-correct-prior-state controls each round, scoring reasoning, code, and results. Pin GPU, notebook environment, and evaluator; slice by modality and query position to isolate cross-turn state management.

### Pair with

[dsagentbench](dsagentbench.en.md) · [agenticdatabench](agenticdatabench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`one-shot data analysis → cumulative multimodal project → persistent analytical state`

DSAEval makes state continuity across analytical requests an explicit capability.