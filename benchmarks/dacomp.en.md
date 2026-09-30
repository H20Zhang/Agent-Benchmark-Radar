# DAComp: separate evaluations of data engineering, analysis and workflow evolution

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-12<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2512.04324)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dacomp.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read the complete 41-page v1 main text and Appendices A–F, including metrics, harnesses, prompts, cases, errors and annotation analysis; checked Tables 3–6.

[arXiv 2512.04324v1 · 2025-12-03](https://arxiv.org/pdf/2512.04324v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DAComp divides 210 tasks into 30 architecture, 30 implementation, 50 evolution and 100 analysis tasks. Stages are evaluated independently rather than as one project lifecycle. Implementation/evolution use DuckDB checks on selected columns. Component Score (CS) evaluates components with gold upstream inputs, whereas Cascading Failure Score (CFS) propagates upstream failures. Architecture and analysis use hierarchical rubrics; analysis combines 60% rubric score with 40% GSB against five baseline reports.

[Source](https://arxiv.org/pdf/2512.04324v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: DA-Code places diverse data-science tasks in one framework; DAComp separates engineering, analysis and subsequent workflow evolution. The new coordinate is stage-specific inputs, artifacts and adaptation. Stage success rates and soft scores should not be collapsed into undifferentiated data intelligence.
<!-- EDITORIAL-METHOD:END -->
GSB means Good–Same–Bad: the judge compares the candidate analysis with five supplied baseline reports under readability, analytical-depth and visualization-related criteria. The main text defines the score as max(0, number of Good judgments minus number of Bad judgments), divided by the total Good, Same and Bad judgments. It is a nonnegative relative-comparison score, not factual accuracy. DA combines 0.6 times the normalized hierarchical-rubric score with 0.4 times GSB. The appendix comparison prompt outputs −10 to 10 for readability and analytical depth, but the exact conversion thresholds and aggregation into G/S/B are not fully specified; reproduction must pin the scorer. See Section 2.2 and Appendix A.3.2.

<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Engineering tables display weighted component/cascading scores on 0–100. SR@8 uses eight attempts, but main-text and appendix success thresholds conflict. The main table labels the framework DE-Agent while the methods also discuss OpenHands CodeAct and multi-agent implementation, leaving mappings unclear. OpenHands allows 200 rounds, 120 seconds per action and termination after three repeated actions; complex implementation allows 50 steps per SQL agent and 100 validation steps. The custom analysis agent’s global cap is unreported. Gemini-2.5-Flash is the default report judge.

[Source](https://arxiv.org/pdf/2512.04324v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected English DE results, Table 3

English track: 30 implementation and 50 evolution tasks; engineering total also includes 30 architecture tasks. CS/CFS are weighted scores; SR@8 uses eight attempts, with a conflict between strict main-text success and Appendix CFS≥80. Do not call it strict perfect-task success.

| Model | Impl CS | Impl CFS | Evol CFS | Evol SR@8 (%) | DE Score |
| --- | --- | --- | --- | --- | --- |
| GPT-5 | 61.98 | 30.79 | 38.75 | 20.00 | 43.45 |
| Qwen3-Coder | 54.21 | 23.64 | 27.12 | 12.00 | 32.80 |

Source location: Table 3 PDFp6; §2.2; AppendixA.1 pp. 16–17; B.2 pp. 22–23 · [Source](https://arxiv.org/pdf/2512.04324v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## English 100-task analysis track, Table 5

100 English analysis tasks; 0.6 normalized rubric +0.4 GSB; Gemini-2.5-Flash judge; reported variability retained; not binary task accuracy.

| Model / harness | DA Score (reported 0–100) |
| --- | --- |
| GPT-5 / OpenHands | 46.99 |
| GPT-5 / DA-Agent | 50.84±3.12 |
| Kimi-K2 / DA-Agent | 41.89±1.78 |

Source location: §2.2,§3.1; Table 5 PDFp7; AppendixA.3/B.1 · [Source](https://arxiv.org/pdf/2512.04324v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

CS exceeding CFS motivates dependency analysis, but stage scores use different measurements and cannot prove independent engineering/analysis abilities. The prose incorrectly associates 56.14 from a judge-validation table with the main results; the selected analysis score is Table 5’s 50.84±3.12.

Main-text evolution success requires every component correct, but the appendix permits CFS≥80. The SR@8 label is retained with that conflict. DuckDB checks selected columns, rounds numbers to two decimals and excludes time columns, not strict equality of every output.

Harmonize success thresholds, framework mapping and budgets, then connect implementation, change and analysis. Switch between gold and actual upstream outputs to measure propagation and repair benefits.

[Source](https://arxiv.org/pdf/2512.04324v1)
<!-- EVIDENCE:limitations:END -->
