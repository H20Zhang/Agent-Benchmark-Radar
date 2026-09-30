# MemCalib: proposition influence and bidirectional errors

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.24259)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memcalib.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read main Sections 1–5 and Appendices A–J, including reward equations, normalization/projection, construction, complete directional results, transfer, all ablations, judge prompt and human audits. PDF localization examples read; plotted curves not digitized and mathematical results not independently replicated. Advertised GitHub URL/API returned 404; Hugging Face README fetch returned 401 and was not pursued. No executable scorer or dataset access certified.

[arXiv 2609.24259v2 (2026-09-22)](https://arxiv.org/html/2609.24259v2)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

MemCalib assigns each proposition in supplied memory a target influence: Ignore leaves no atom-specific footprint, Bound provides local support and Control constrains a core conclusion. Models see natural memory paragraphs; a judge labels each atom’s realized influence in the response. Calibration means matching influence levels, not confidence probabilities. The separate MemCalib-RL method splits nine target/actual transitions into reward channels and redistributes credit using fixed-response token-likelihood changes after atom ablation; it is not a second benchmark.

Editorial placement: RPEval already grades Ignore/Support/Dominate preference use. MemCalib moves to propositions within composite blocks and broadens domains to health, assistance and coding-language tasks. Its addition is finer-grained influence and bidirectional errors, not the first selective-memory-use evaluation.
Illustrative levels: an old food preference should be ignored for an unrelated technical question; relevant background may provide bounded support; an explicit language requirement may control the requested output. The target depends on the question rather than being a permanent property of the proposition.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

There are 15,000 examples and 234,220 atoms: 7500 health examples and 3750 each in assistance/coding. Ignore accounts for 84.3% of atoms, with 6–63 atoms per example. The 13,500/1500 train/test split reserves another 1500 training examples for validation. SFT uses 12,000 examples; other methods share a 4000-example cold start and train on the remaining 8000. Testing uses non-thinking generation, temperature/top-p 1 and three seeds; DeepSeek-V4-Pro is the primary judge. Mapping A/B/C to 0/1/2, O and U sum over/under-use rank distances. SCS averages 2 raised to −(O+U); Exact requires no errors; sMOS/sMUS average 1 minus 2 raised to −O/−U. Scores are scaled to 0–100, so one rank error halves a sample’s SCS.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 1, selected untrained model profiles

Same test and primary judge. SCS/severity are 0–100 scores; Exact is response-level. Qwen3-8B over-uses less but under-uses more. Size, generation and architecture vary together, so this is not a causal parameter-count experiment.

1500 test examples per seed; mean and SD over three seeds.

| Model | SCS mean | SCS SD | Exact (%) | Over-use severity | Under-use severity |
|---|---|---|---|---|---|
| GPT-5.6-SOL | 46.25 | 0.6 | 28.4 | 38.45 | 22.92 |
| Qwen3-8B | 31.17 | 0.21 | 15.29 | 37.19 | 45.66 |
| Qwen3.5-35B-A3B | 26.54 | 0.28 | 12.24 | 64.76 | 19.93 |

Locator: Table 1, selected untrained model profiles · [Source](https://arxiv.org/html/2609.24259v2)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Tables 2 and 9, Qwen3-8B selected training comparisons

Qwen3-8B with DeepSeek-V4-Pro judging. GRPO reduces under-use but increases over-use versus cold start. MemCalib-RL improves both, yet SFT still has lower over-use severity, so it does not win every metric. Three-seed SD is not a confidence interval.

1500 held-out examples per seed; training data and initialization are described above.

| Method | SCS mean | SCS SD | Exact (%) | Over-use severity | Under-use severity |
|---|---|---|---|---|---|
| Cold-start | 51.98 | 1.24 | 33.87 | 21.97 | 33.41 |
| SFT | 65.72 | 0.64 | 49.49 | 13.58 | 24.04 |
| GRPO | 67.61 | 0.71 | 52.18 | 23.91 | 11.27 |
| MemCalib-RL | 79.54 | 0.77 | 67.89 | 14.98 | 6.81 |

Locator: Tables 2 and 9, Qwen3-8B selected training comparisons · [Source](https://arxiv.org/html/2609.24259v2)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Appendix C, natural and stress-stratified human audit

One human annotator, blinded to model-judge decisions, applies the same atom rubrics. All 127 natural-sample Ignore labels agree; stress sampling covers nine target/actual combinations and has 26 Bound/Control swaps. The 96.7% headline does not characterize every boundary.

150 natural plus 150 stress-stratified response–atom judgments; Wilson intervals.

| Sampling scheme | Agreements | Sample size | Agreement (%) | 95% lower | 95% upper |
|---|---|---|---|---|---|
| Natural | 145 | 150 | 96.7 | 92.4 | 98.6 |
| Stress-stratified | 111 | 150 | 74.0 | 66.4 | 80.4 |

Locator: Appendix C, natural and stress-stratified human audit · [Source](https://arxiv.org/html/2609.24259v2)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 11, selected RPEval transfer results

No extra training; RPEval explicit multi-preference subset with separate preference memories. Macro requires every preference in a response to be used correctly; Micro counts preferences. Overall gains accompany worse UPB, precluding a claim of bidirectional transfer improvement.

150 queries, three sampling seeds; preference-level denominator varies by query and is not separately printed.

| Qwen3-8B checkpoint | All-preferences-correct Macro (%) | Preference-level Micro (%) | Under-use bias UPB (%) |
|---|---|---|---|
| Base | 19.78 | 61.98 | 3.53 |
| MemCalib-RL | 33.78 | 78.12 | 8.84 |

Locator: Table 11, selected RPEval transfer results · [Source](https://arxiv.org/html/2609.24259v2)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Scoring measures observable response footprint, not acceptance: explicitly correcting or warning about an atom counts as at least Bound. Rebutting an Ignore atom can therefore be over-use without false belief or unsafe action. Half the examples concern health and target levels are mainly model-generated/reviewed; scores certify neither clinical correctness nor executable code. Ablation likelihood is an attribution proxy; the human Top-3 measure requires only one relevant sentence among three, not 99% causal token-localization accuracy. The primary judge participates in construction review, SFT screening, rewards and evaluation; swapping to Qwen preserves rankings but lowers absolute scores.

MemCalib-RL Qwen3-8B SCS falls from 79.54 under DeepSeek-V4-Pro to 72.19 under Qwen3.8-Max; high rank correlation is not absolute score agreement. Training gains are compared with Cold-start, not an equal-cost no-training system, and full-parameter versus LoRA adaptation differs across model sizes. No matched end-to-end training-cost table is supplied. On 2026-09-30 the advertised GitHub repository returned 404 through web and API; the public Hugging Face README request returned 401 Unauthorized, and that route was stopped. These are current source-access observations, not proof the artifacts never existed.



Next: Retain directional metrics and existing judge/localization ablations; add atom-count-stratified scores, ignore-all and oracle-relevant-atom controls, plus independent multi-annotator audits of Bound/Control and safety corrections. Match training compute before comparing algorithms and test utility in retrieval/action pipelines.
<!-- EVIDENCE:limitations:END -->
