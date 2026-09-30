# MLE-bench: competition submissions and historical medal thresholds

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2024-10-09 · paper v1<br>
> **o1-preview + AIDE — Competitions with at least bronze: 16.9%**<br>
> Best main-experiment setup in the initial 75-competition benchmark; not per-question accuracy or a later extended-budget board. [Original source](https://arxiv.org/abs/2410.07095v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](mle-bench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and versions

Full substantive paper and appendix reading completed for the stated primary version; experiments were not independently reproduced.

Read the entire substantive 27-page v1 and Appendices A.1–A.8, including the full competition/split inventory, scaffold configuration and obfuscated-task example.

[arXiv 2410.07095v1 · 2024-10-09](https://arxiv.org/pdf/2410.07095v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## What the method measures

MLE-bench evaluates final prediction files against historical private-leaderboard medal thresholds. Its submission validator exposes format validity, not test performance. AIDE searches candidate solutions and uses GPT-4o for feedback even with another generation model.

<!-- EDITORIAL-METHOD:START -->
The benchmark repackages seventy-five Kaggle competitions: agents read descriptions/training data, conduct local experiments and produce submission files, then hidden evaluation compares results with historical medal thresholds. AIDE debugs, expands and improves a tree of candidate programs, while OpenHands follows an interactive software workflow. An illustrative task trains a predictor, selects it using local validation and emits predictions aligned to test rows. The submission validator checks format rather than exposing hidden scores, although prior knowledge of public competitions and solutions can still influence performance.

Editorial placement: MLAgentBench centers improvement over supplied baselines; MLE-bench emphasizes full competition delivery and historical medal tiers. MLE-Dojo adds explicit iterative score feedback. Final submission without hidden-score access differs from score-visible optimization.
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Runs receive 24 hours, one A10 with 24 GB GPU memory, 36 vCPUs and 440 GB host RAM. OpenHands has a 100 GiB subcontainer allowance. Main text specifies 500 AIDE nodes, while its appendix configuration lists 2,000 steps; the mismatch remains unresolved.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

V1; 75 competitions. Any Medal is the proportion of runs earning at least bronze, averaged over seeds; values are mean ± SEM.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| o1-preview + AIDE | 75 competitions × 16 seeds | Any Medal (%) | 16.9 ± 1.1% | 24 h; GPT-4o feedback | Table 2, p. 6 |
| GPT-4o + AIDE | 75 competitions × 36 seeds | Any Medal (%) | 8.7 ± 0.5% | 2024-08-06; 24 h | Table 2, p. 6 |
| GPT-4o + OpenHands | 75 competitions × 3 seeds | Any Medal (%) | 4.4 ± 1.4% | 2024-08-06; 24 h; 100 GiB | Table 2, p. 6; A.6.2, p. 18 |
| GPT-4o + AIDE · pass@6 | 75 competitions; estimated from 36 seeds | Any-success coverage (%) | 17.0% | 6 independent attempts × 24 h | §3.2, p. 6; Figure 3, p. 7 |

Fact source: [Table 2, p. 6; Table 2, p. 6; A.6.2, p. 18; §3.2, p. 6; Figure 3, p. 7](https://arxiv.org/pdf/2410.07095v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Medal rates include failures; SEM describes seed variability. Pass@6 is any-success coverage, not a demonstrated selection policy. Reconstructed holdouts and later methods complicate comparison with historical humans. Different scaffolds and memory allowances prevent single-component causal attribution.

<!-- EDITORIAL-NEXT:START -->
Next, compare tree search and linear revision under matched model, hardware and budgets, testing candidate selection without hidden scores. Repeat on fresh or obfuscated competitions. Higher pass@6 coverage does not establish a deployable method for selecting among six outputs.
<!-- EDITORIAL-NEXT:END -->
<!-- EVIDENCE:limitations:END -->
