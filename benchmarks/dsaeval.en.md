# DSAEval: multimodal data science in persistent sessions

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-01-20<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2601.13591)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](dsaeval.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the complete 35-page v3 and Appendices A–K, including validation, every prompt, full code/report examples, all judge tables, the complete weight sweep and error audit. V3 evaluates 13 models, not the older note’s 11.

[arXiv 2601.13591v3 · 2026-09-07](https://arxiv.org/pdf/2601.13591v3)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

DSAEval uses persistent, multi-query notebook sessions and report-style outputs. Scores combine reasoning, code and results with weights 0.3/0.3/0.4, then average Claude-Haiku-4.5 and GPT-5.1 judgments. These are rubric points, not execution-success percentages.

<!-- EDITORIAL-METHOD:START -->
Problems are organized into persistent notebook sessions around datasets, allowing later questions to reuse earlier objects and analysis. Outputs include reasoning, code and result reports rather than only short answers. An illustrative sequence cleans and plots data, answers a dependent statistical question and explains conclusions. Multimodal configurations inspect visual outputs while text-only configurations rely on textual observations, changing available evidence rather than just output format. Two judges assess reasoning, code and results before aggregation.

Editorial placement: DS-1000 snippets and DA-Code’s task workflows are useful references. DSAEval adds cumulative multi-query context, visual feedback and report-style grading. Its scores are not directly comparable to binary execution success or evidence of long-term cross-project memory.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The suite has 641 problems and 285 datasets. Sessions allow 20 turns, with a one-hour timeout per iteration and four A100 80 GB GPUs. Three PhD candidates calibrated the judges on Gemini-3-Pro’s complete log, not all agent styles.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V3 dual-judge protocol; scores range 0–10. CV rows compare the same model with plot observations disabled/enabled. Their category sample counts are not explicitly reported.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Claude-Sonnet-4.5 · overall | 641 assigned tasks; missing-output policy unclear | Mean overall score (0–10) | 8.164 | Reported main value; dual judges | §5, p. 7 |
| MiMo-V2-Pro · overall | 641 assigned tasks; missing-output policy unclear | Mean overall score (0–10) | 7.912 | Same session budget; dual judges | §5, p. 7 |
| Qwen3-VL-30B · CV | CV subset; paired task count unspecified | Text → multimodal (0–10); relative gain; 90% CI of difference | 4.07 → 4.53; +11.30%; [0.0, 0.9] | 10,000 paired bootstrap resamples | Table 2, p. 6; §4.1, p. 7 |
| GPT-5-nano · CV | CV subset; paired task count unspecified | Text → multimodal (0–10); relative gain; 90% CI of difference | 5.53 → 5.88; +6.33%; [-0.3, 0.9] | 10,000 paired bootstrap resamples | Table 2, p. 6; §4.1, p. 7 |

Fact source: [§5, p. 7; Table 2, p. 6; §4.1, p. 7](https://arxiv.org/pdf/2601.13591v3)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Multimodal gains are relative changes; several paired confidence intervals include zero. Valid-output handling is not fully specified. Main Claude score 8.164 slightly differs from averaging appendix judge summaries. Public-source contamination and a contradictory time-series reference split remain risks; judge agreement does not establish error-free ground truth.

<!-- EDITORIAL-NEXT:START -->
Next, match sessions/budgets and intervene on visual observations, textual alternatives and state resets. Combine numerical checks with independent blind review to determine whether multimodal gains correct analytical errors or primarily affect judge preferences.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
