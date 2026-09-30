# Data Agent Benchmark (DAB): enterprise questions across heterogeneous databases

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2026-03-21 · paper v1<br>
> **Gemini-3-Pro / paper ReAct agent — Pass@1: 38%**<br>
> Best of five generic-model baselines in Table 3: 50 trials per query and a 12-dataset average. Excludes the PromptQL case study and later rescored boards. [Original source](https://arxiv.org/html/2603.20576v1)<br>
> Original-paper history only; later validators, hints, and task-specific prompts change comparability.
<!-- RELEASE-REFERENCE:END -->

[中文](data-agent-benchmark.md) | **English** · [Home](../README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Read the stated version’s complete main text and available appendices and checked the selected results; no independent experiment reproduction.

Read the complete 22-page main text and Appendices A–C, including all 54 questions, system/judge prompts and failure cases; also read the current official README and its rescoring events. The externally linked full raw trajectories were not downloaded.

[arXiv 2603.20576v1 · 2026-03-21](https://arxiv.org/pdf/2603.20576v1)
[Official repository documentation · 2026-09-30](https://github.com/ucbepic/DataAgentBench/blob/main/README.md)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement target

DAB derives four challenges from enterprise interviews across six industries: multi-database integration, mismatched join keys, text extraction and domain rules. Public data plus controlled perturbations yield 54 queries across twelve datasets, nine domains and four DBMSs, with every query spanning at least two databases. The proprietary enterprise data are not released. To retain deterministic references, the authors explicitly exclude open-ended analysis and changing external APIs.

[Source](https://arxiv.org/pdf/2603.20576v1)

<!-- EDITORIAL-METHOD:START -->
Editorial placement: Spider/BIRD mainly target supplied relational databases; DAB combines cross-database integration, mismatched join keys, text extraction and domain rules within queries. It adds heterogeneous access/integration. Excluding open-ended analysis means it does not replace InsightBench discovery or DSAgentBench desktop interaction.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Scoring and experimental conditions

Five models run fifty trials per query, totaling 13,500 trials. A ReAct scaffold provides database listing, read-only queries, Python execution and answer submission. Trials allow 100 iterations and one hour, with 600 seconds per tool; dataset descriptions and hints are supplied, and provider-default temperature/reasoning settings are used. Tool outputs beyond 10,000 characters are stored in files with context previews. pass@1 is averaged within each dataset and then equally across twelve datasets, not micro-averaged over 54 queries or best-of-fifty. Original answer checks favor recall and can accept extra incorrect values.

[Source](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Selected original-paper ReAct results

Original v1 validators; 54 queries ×50 trials per model, equally macro-averaged over twelve datasets; hints supplied; ReAct; 100 iterations/one hour/600 seconds per tool; costs cover all 2,700 trials, not one query.

| Model | pass@1 (0–1) | Cost across 2,700 trials (USD) |
| --- | --- | --- |
| Gemini-3-Pro | 0.38 | 1355 |
| GPT-5-mini | 0.30 | 67 |
| GPT-5.2 | 0.25 | 283 |

Source location: Tables 3–4, PDF p. 9; section 3.1, pp. 6–7 · [Source](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Separate same-model system comparison with Claude-Opus-4.6

Table 7; 54 queries, five trials each, dataset-macro average; same Claude-Opus-4.6; separate from the five-model main experiment; private orchestration and semantic layer vary together.

| System | pass@1 (0–1) |
| --- | --- |
| PromptQL | 0.51 |
| ReAct | 0.44 |

Source location: Section 3.4 and Table 7, PDF p. 11 · [Source](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:limitations:START -->
## Interpretation, source limitations and next experiment

The separate PromptQL comparison uses the same Claude-Opus-4.6 model and five trials per query. Its semantic layer, private prompts and orchestration change together, so 0.44→0.51 cannot be attributed solely to shared representations. The 85% error claim concerns 1,147 sampled completed-but-wrong trajectories classified by GPT-5, excluding non-submissions and runtime errors; it is not the fraction of all failures.

On June 12, 2026, the authors rescored stored submissions with revised validators and regenerated PATENTS references; on August 18, DEPS_DEV_V1 accepted any valid package tied at fifth place. The v1 values above therefore describe the historical protocol, especially not current unsolvability of patents. The live board distinguishes tuned prompts, hints, missing and contaminated trials; newer high scores do not isolate a component’s causal effect.

Pin current validators, prompts, model and budget, compare no hints with fixed hints, and separately add typed text extraction or reusable data profiles. Report exact complete-answer correctness, legacy recall-oriented checks, costs and dataset-macro scores so evaluator changes are not mistaken for agent progress.

[Source](https://arxiv.org/pdf/2603.20576v1)
<!-- EVIDENCE:limitations:END -->
