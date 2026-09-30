# MLAgentBench: iterative experiments over supplied ML baselines

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2023-10<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2310.03302)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mlagentbench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read all substantive text of the 39-page v2 and Appendices A–F, including the complete example trajectory. V1 was checked only for its abstract, method/experiment sections and Figures 3–6; no full v1 reading is claimed.

[arXiv 2310.03302v2 · 2024-04-14](https://arxiv.org/pdf/2310.03302v2) · [arXiv 2310.03302v1 · 2023-10-05](https://arxiv.org/pdf/2310.03302v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

MLAgentBench asks an agent to improve a supplied ML task baseline through code, experiments and recorded research steps. The paper agent combines recent history, planning and fact checking; the scaffold comparison does not isolate any one component.

<!-- EDITORIAL-METHOD:START -->
Agents receive a task description, training/evaluation code and data, modify modeling or preprocessing in a workspace, run experiments and retain observations in a research log. An illustrative workflow inspects a classifier baseline, changes a permitted module, trains a candidate, reads validation feedback and delivers code. Success is improvement relative to each task’s own baseline, so equal relative thresholds need not imply equal difficulty. Planning, history retrieval and fact checking jointly alter behavior; a whole-scaffold score difference is not a standalone memory benefit.

Editorial placement: compared with DS-1000 snippets, MLAgentBench adds experimental choices and feedback loops. MLE-bench uses broader competitions and medal thresholds. Improving a supplied baseline and reaching historical competition tiers are separate evaluation coordinates.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

V2 averages success across 13 tasks with eight trials each. Success requires at least 10% baseline improvement; some baselines are trivial predictions. The selected comparisons share a 50-action, five-hour cap. GPT-4 elsewhere receives only 30 actions.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V2 Tables 3/5; success is percent of trials meeting the task-specific improvement threshold, averaged over tasks. Matched backbone comparisons, not component ablations.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Claude v3 Opus + paper agent | 13 tasks × 8 trials | Mean success (%) | 37.5% | opus-20240229; 50 actions; 5 h | Table 3, p. 7; Table 5, p. 15 |
| Claude v3 Opus + LangChain | 13 tasks × 8 trials | Mean success (%) | 33.7% | 50 actions; 5 h; ReAct | Table 5, p. 15 |
| GPT-4-turbo + paper agent | 13 tasks × 8 trials | Mean success (%) | 26.0% | 0125; 50 actions; 5 h | Table 3, p. 7; Table 5, p. 15 |
| GPT-4-turbo + LangChain | 13 tasks × 8 trials | Mean success (%) | 1.0% | 0125; 50 actions; 5 h; ReAct | Table 5, p. 15 |

Fact source: [Table 3, p. 7; Table 5, p. 15; Table 5, p. 15](https://arxiv.org/pdf/2310.03302v2)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The 37.5% Opus result is from the April 2024 revision, not the 2023 release. Average improvement excludes invalid submissions, unlike success. The appendix CIFAR-10 trace exposes test accuracy, so uniform hidden-score isolation cannot be assumed. Baseline choice and task-specific evaluation limit comparisons with Kaggle medal benchmarks.

<!-- EDITORIAL-NEXT:START -->
Next, hold model, action cap and baselines fixed while separately removing log retrieval, planning and fact checking. Report valid-submission rate and compute cost over all attempts alongside success; small task coverage and weak baselines are important alternative explanations for aggregate gains.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
