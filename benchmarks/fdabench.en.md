# FDABench: analytical workflows and tool-call evaluation over heterogeneous evidence

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-09<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2509.02473)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](fdabench.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read all 12 pages of v3 including Appendices A–D, plus the complete five-page official technical report; checked Tables 6 and 10.

[arXiv 2509.02473v3 · 2026-08-15](https://arxiv.org/pdf/2509.02473v3)
[Official technical report · 2026-09-30](https://github.com/fdabench/FDAbench/blob/main/technical_report.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

FDABench v3 contains 2,007 tasks over 139 databases and frozen document, web, image, video and audio evidence: 579 single-choice, 760 multiple-choice and 668 report tasks. Authors compare planning, reflection, direct tool use and other workflows. Some prior systems are reimplementations, not original releases. Systems lacking native multimodality receive text fallbacks, creating an input-interface confound.

[Source](https://arxiv.org/pdf/2509.02473v3)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: compared with DA-Code’s interactive artifact tasks, FDABench organizes analytical workflows over heterogeneous evidence and evaluates tool selection/calls. Tool-call success complements final-artifact evaluation but is not interchangeable with end-to-end analytical task success.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

EX scores choices, RS grades report dimensions, and TOS measures tool/reference-structure agreement. SR means successful tool execution, not end-to-end task success. The technical report specifies Gemini-3-Flash-preview judging at temperature 0 with at most 500 output tokens. A complete common agent step/token cap is not given; construction-model limits must not be substituted for evaluation budgets.

[Source](https://arxiv.org/pdf/2509.02473v3)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected workflows with GPT-5 fixed, v3 Table 6

V3 with GPT-5 fixed; EX covers 1,339 choice tasks, RS covers 668 reports, and TOS is a tool/structure score; token budgets are not equalized; Cost is a reported resource outcome.

| Model / workflow | RS (0–1) | EX (0–1) | TOS (0–1) | Cost (tokens, reported) |
| --- | --- | --- | --- | --- |
| GPT-5 / Reflection | 0.418 | 0.628 | 0.331 | 12331 |
| GPT-5 / Planning | 0.409 | 0.610 | 0.412 | 4430 |
| GPT-5 / Tool-use | 0.450 | 0.536 | 0.392 | 2587 |

Source location: Main§4.3,§5.1,§5.3/Table 6 PDFp8; technical report§1,§6,§9 · [Source](https://arxiv.org/pdf/2509.02473v3)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Report-grading agreement sample, v3 Table 10

200 sampled tasks across types and three independent experts; report-subset size unspecified; agreement coefficients are not task accuracy.

| Comparison | Krippendorff alpha | ICC(A,1) | Kendall tau-b |
| --- | --- | --- | --- |
| Report: Human vs Human | 0.81 | 0.84 | 0.95 |
| Report: Human vs LLM | 0.76 | 0.79 | 0.92 |

Source location: Main§5.5, Table 10 PDFp9; technical report§5 gives per-dimension detail · [Source](https://arxiv.org/pdf/2509.02473v3)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

With GPT-5 fixed, workflows trade quality against cost. Judge agreement is validated on 200 sampled tasks across types, with the report-only count unspecified; it does not guarantee all report grades. Reference tool graphs may omit valid alternative paths.

This note uses v3 dated August 15, 2026, not the initial 2025 release results. The official technical report supplements the reading; scorer settings should be pinned with code revisions.

Fix model, budget and modality inputs, ablate planning and reflection separately, blind-review alternative tool paths and jointly report answers, reports, tool selection and runtime failures.

[Source](https://arxiv.org/pdf/2509.02473v3)
<!-- EVIDENCE:limitations:END -->
