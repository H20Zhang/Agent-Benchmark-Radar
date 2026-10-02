# DABstep: multi-step financial analysis and final-answer scoring

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-06-30 · paper v1<br>
> **o4-mini — Hard accuracy: 14.55%**; **GPT-4.1 — Easy accuracy: 80.56%**<br>
> Hidden test set, Table 1. Hard and Easy have different best models; these are not one model’s combined result. [Original source](https://arxiv.org/html/2506.23719v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](dabstep.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

This review read the complete extracted Sections 1–5 and Appendices A.1–A.4, Table 1 and scoring pseudocode, and checked official task files and baseline code. The ten execution-trace figures were not newly visually inspected; the earlier 2026-09-30 figure-reading record is not claimed as new visual verification.

[arXiv 2506.23719v1 · 2025-06-30](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DABstep v1 contains 450 tasks: 72 Easy and 378 Hard. Anonymized Adyen queries are expanded from 95 core questions, with the Hard instances derived from 23 core questions. Agents combine payment tables, fee and merchant JSON, category and country mappings, and a rule manual in an isolated Python environment to produce short answers. A lightweight tool wrapper normally uses ReAct prompting; o4-mini, o3-mini, o1, R1 and Gemini 2.5 Pro use a reasoning-oriented prompt. Table 1 reports a maximum of ten steps, without a common token cap, time limit or repetition budget.

[Source](https://arxiv.org/pdf/2506.23719v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: WikiSQL/Spider primarily produce queries; DABstep requires multi-step financial analysis over business data and documentation. Compared with DA-Code’s heterogeneous artifact scoring, it retains a more explicit final-answer target. Tool composition and business rules enter the task without final correctness certifying every reasoning step.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

The metric is binary final-answer accuracy on the hidden test set, reported separately for Easy and Hard. A deterministic, type-aware scorer normalizes numbers, lists and strings without an LLM judge. Its numeric tolerance differs between the prose and pseudocode, making a pinned scorer implementation important. On 75 model answers checked by two annotators, the scorer matched every final human label; this small validation study is not agent task accuracy.

[Source](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected baseline results from the release paper

Table 1 hidden test, with Hard and Easy scored separately; the released task file contains 378 Hard and 72 Easy tasks, but per-model evaluated and excluded counts were not independently verified. Binary final-answer scoring; maximum ten steps; prompt families differ; no across-seed variance reported.

| Model | Hard accuracy (%) | Easy accuracy (%) | Prompt type |
| --- | --- | --- | --- |
| o4-mini | 14.55 | 76.39 | Reasoning prompt |
| Claude 3.7 Sonnet | 13.76 | 75.00 | ReAct prompt |
| GPT 4.1 | 12.43 | 80.56 | ReAct prompt |

Source location: Table 1, PDF p. 3; sections 3.1–4.1, pp. 5–7; Appendix A.2, pp. 13–14 · [Source](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

o4-mini leads Hard while GPT 4.1 leads Easy; their best scores cannot be combined into one system result. Parameterized instances are not 450 independent workflows, so core-question-level splits would better test generalization. The appendix shows Claude 3.7 Sonnet reading the manual, repairing a JSON-structure mistake and producing a correctly formatted list, yet omitting monthly fraud statistics required to filter fees. This illustrates a difference between executable code and complete business-rule application, but is not a quantitative causal attribution.

Numeric tolerance is illustrated as 1e-4 in the prose but 1e-2 in Algorithm 1; reproduction must pin scorer code. Historical cost timestamps are also inconsistent and are not treated as current prices.

Split by core question, hold prompts and the ten-step budget fixed, and compare raw manuals, explicit structured rules and gold intermediate statistics. Separately report omitted rules, data-processing errors, formatting errors and execution cost.

[Source](https://arxiv.org/pdf/2506.23719v1)
<!-- EVIDENCE:limitations:END -->
