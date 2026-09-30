# DSGym: shared execution environments and no-data shortcut filtering

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-01-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2601.16344)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dsgym.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive text of the 37-page v1 and Appendices A–E, including refinement, full competition inventory, all cases, failure definitions, training settings and complete prompts. Tables 3–5 and Figure 5 were visually checked.

[arXiv 2601.16344v1 · 2026-01-22](https://arxiv.org/pdf/2601.16344v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

DSGym standardizes stateful Docker/Jupyter execution. It removes tasks answered correctly without data by at least three of five models. SFT uses 2,000 synthetic query/trajectory pairs filtered by execution-aware judging and semantic diversity.

<!-- EDITORIAL-METHOD:START -->
The platform standardizes persistent code execution for analysis and prediction. Analysis tasks require computation from files; prediction tasks require models and scorable outputs. An illustrative workflow inspects columns/distributions, cleans and computes in a notebook, repairs through execution feedback and submits. No-data filtering removes questions solved by several models without consulting the files; execution and diversity filters select synthetic trajectories for supervised training. This controls one shortcut class without ruling out others in retained tasks.

Editorial placement: rather than connecting suites such as DABStep through different executors, DSGym emphasizes a common environment and no-data shortcut audit. Relative to DataSciBench’s task checks, it also trains on synthetic execution trajectories. Environment, filtering and training effects require separate attribution.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Evaluation uses CodeAct, temperature 0, no auxiliary tools and exact matching with numeric tolerance. Concrete action/time/hardware limits, tolerance values and repeat count are unspecified. SFT runs six epochs at learning rate 2e-5.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1 shared scaffold. Analysis accuracy divides by evaluated tasks; DSBio has 90 tasks, while DABStep-hard’s evaluated count is not explicitly stated in the paper.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Kimi K2 Instruct · DSBio | DSBio; 90 tasks | Accuracy (%) | 43.33% | Kimi-K2-Instruct-0905; T=0 | Table 3, p. 10 |
| Qwen3-4B-DSGym-SFT-2k · DSBio | DSBio; 90 tasks | Accuracy (%) | 21.11% | General-analysis SFT; T=0 | Table 5, p. 13 |
| Qwen3-4B-DSGym-SFT-2k · DABStep-hard | DABStep-hard; count unspecified | Accuracy (%) | 33.07% | Seed tasks include DABStep; T=0 | Table 5, p. 13 |
| GPT-4o · DABStep-hard | DABStep-hard; count unspecified | Accuracy (%) | 7.41% | gpt-4o-2024-08-06; T=0 | Table 5, p. 13 |

Fact source: [Table 3, p. 10; Table 5, p. 13](https://arxiv.org/pdf/2601.16344v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The trained 4B model beats GPT-4o only on DABStep easy/hard, not all analysis tracks. The no-data filter does not prove contamination absence. DSPredict’s reported percentage denominators do not match corpus counts clearly, while runtime budgets remain unknown. Seed/test independence for same-domain synthesis is also incompletely specified.

<!-- EDITORIAL-NEXT:START -->
Next, audit shortcuts with models excluded from filtering and split synthesis seeds/test tasks across domains. Under matched CodeAct budgets, compare no training, random-trajectory training and filtered-trajectory training, reporting both original and filtered suites.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
