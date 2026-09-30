# DataSciBench: component checks and overall success in multi-step data science

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-02 · paper v1<br>
> **GPT-4o-2024-05-13 — Table 2 overall Score: 64.51**; **GPT-4o-2024-05-13 — Collected-prompts success: 19.82%**<br>
> Best overall Score in Table 2 and best success on collected prompts in Table 5; the latter is not whole-mixture accuracy. [Original source](https://arxiv.org/html/2502.13897v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](datascibench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read the complete 40-page main text and Appendices A.1–A.13 and B, including code and examples; checked Tables 2, 5 and 6.

[arXiv 2502.13897v1 · 2025-02-19](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DataSciBench decomposes requirements into task–function–check (TFC) units and uses reference solutions to build executable checks. It has 222 prompts: 167 from BigCodeBench and 55 otherwise collected prompts, producing 519 checks. A DataInterpreter-style planning/execution framework evaluates 23 models on output completion, requirement adherence and visualization quality.

[Source](https://arxiv.org/html/2502.13897v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: DS-1000 tests snippets in supplied context; DataSciBench extends the endpoint to multi-step data-science requests with task-specific checks. This is finer than a single string/execution pass rate, but component, visual and overall metrics have different scales rather than one universal correctness meaning.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Ten runs per prompt estimate SR as single-sample pass@1 for satisfying all TFC checks, not best-of-ten success. CR assigns 0 to missing/failed outputs, 1 to completed but noncompliant outputs and 2 to compliant outputs. The composite weights CR at 65% and SR, visual quality and five function scores at 5% each. GPT-4o-mini supplies visual grades on a raw 0–5 scale; that scale should not silently be converted to percentages. Temperature, tool steps, token and wall-clock limits are incompletely reported.

[Source](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected results across 222 prompts, Table 2

All 222 prompts and 519 TFC checks; ten runs per prompt; SR estimates pass@1 and CR has two points per check; DataInterpreter-style harness with GPT-4o-mini visual judging; other budgets incompletely reported.

| Model | SR (%) | CR (%) | Composite Score |
| --- | --- | --- | --- |
| GPT-4o-2024-05-13 | 66.31 | 68.44 | 64.51 |
| Deepseek-Coder-33B-Instruct | 55.86 | 61.23 | 56.76 |
| o1-mini | 29.77 | 45.26 | 38.78 |

Source location: §3.2–3.3,§4.2 Eqs2–4; Table 2 PDFp6 · [Source](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Source slices for the same GPT-4o, Tables5–6

Same GPT-4o-2024-05-13; source groups have denominators 55 and 167, with ten runs per prompt; not difficulty-matched paired interventions.

| Model / source | Prompts | SR (%) |
| --- | --- | --- |
| GPT-4o-2024-05-13 / Other collected prompts | 55 | 19.82 |
| GPT-4o-2024-05-13 / BigCodeBench source | 167 | 81.62 |

Source location: §3.2; §5.2; AppendixA.8 Tables5/6, PDFp15 · [Source](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The same GPT-4o has SR 81.62% on the 167 BigCodeBench-derived prompts but 19.82% on the remaining 55. Source and difficulty composition strongly affect totals, and the 64.51 composite score is not end-to-end accuracy.

Visual and other check scales differ; preserve the paper’s formula and metric units. Source slices are not difficulty-matched experiments.

Fix the harness and budget, report all-check success, partial completion and visual-judge disagreement by source and difficulty, and vary requirements over the same underlying data to separate execution from adherence.

[Source](https://arxiv.org/html/2502.13897v1)
<!-- EVIDENCE:limitations:END -->
