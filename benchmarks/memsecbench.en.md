# MemSecBench: separating attack completion from selective repair

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-07-29<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2607.27080)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memsecbench.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Read the full main paper and Appendices A–F, including taxonomy, complete case example, backend/runtime settings and evidence gates. All five judge prompts read from the 28-page PDF where HTML omits them. Configuration-profile figures were inspected through captions and reported values, not digitized. No implementation download independently located through the paper/PDF and targeted title search; no code audit or attack execution.

[arXiv 2607.27080v1 (2026-07-29)](https://arxiv.org/html/2607.27080v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Each MemSecBench case contains Write, Execute and Forget tasks. An accepted write must also leave the target malicious semantics in backend state. Only then do Execute and Forget start independently from the same poisoned snapshot. Execute checks exposure, adoption and a consequence recorded by a controlled service; Forget checks that dangerous semantics no longer operate while required benign memories remain. Repair is a separate branch, not recovery of an environment after an executed attack.

Editorial placement: Relative to poisoning evaluations such as MPBench’s untrusted-input-to-memory setting, this study adds consequence verification and selective repair for the same semantics, plus matched whole-stack comparisons. Its addition is the linked post-write branches, not a claim that every predecessor lacks execution or repair analysis.
Illustrative branching example: a write leaves both a dangerous suggestion and a legitimate preference. Execute checks the target consequence in a simulated service; Forget restarts from the poisoned snapshot and must neutralize the suggestion while preserving the preference.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

The 310 English cases span 48 contexts: 113 code/science, 107 daily-life and 90 office cases. Two harnesses (OpenClaw/Hermes), four backends (Native/Mem0/Mem0-Graph/A-MEM) and three models (DeepSeek-V4-Pro/MiniMax-M3/GPT-5.5) produce 24 configurations, with one run per case/configuration. Each stage gets 900 seconds; Hermes permits 32 turns and OpenClaw up to 8192 output tokens per response. Capacity, retrieval, embeddings, internal calls and session injection differ by backend. Comparisons fix harness/model; Native is not the same implementation across harnesses. Except deterministic W1, DeepSeek-V4-Pro judges at temperature zero, with source, timing and final-service-record gates.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 2, OpenClaw / GPT-5.5 selected stack comparison

OpenClaw and GPT-5.5 are fixed. E2E-ASR uses all 310 cases; SRSR uses each row’s poisoned subset, so repair populations differ. Mem0-Graph here is entity-linked retrieval without relation edges or multi-hop traversal.

310 cases per row; repair denominators 240/214/196/267 respectively.

| Backend | Poisoned cases | All cases | Complete attacks | E2E-ASR (%) | Selective repairs | Conditional SRSR (%) |
|---|---|---|---|---|---|---|
| Native | 240 | 310 | 177 | 57.1 | 210 | 87.5 |
| Mem0 | 214 | 310 | 135 | 43.55 | 184 | 85.98 |
| Mem0-Graph | 196 | 310 | 127 | 40.97 | 170 | 86.73 |
| A-MEM | 267 | 310 | 166 | 53.55 | 249 | 93.26 |

Locator: Table 2, OpenClaw / GPT-5.5 selected stack comparison · [Source](https://arxiv.org/html/2607.27080v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 2, harness-dependent A-MEM repair contrast

Separate from the OpenClaw comparison. Under Hermes, A-MEM lowers complete attack incidence while also lowering conditional repair. Resistance and recovery are different dimensions; single-run descriptive contrasts do not establish universal rankings.

310 cases per row; SRSR denominators are 254 and 267.

| Configuration | Poisoned cases | Complete attacks | Attack N | E2E-ASR (%) | Selective repairs | SRSR (%) |
|---|---|---|---|---|---|---|
| Hermes / GPT-5.5 / Native | 254 | 186 | 310 | 60.0 | 130 | 51.18 |
| Hermes / GPT-5.5 / A-MEM | 267 | 145 | 310 | 46.77 | 64 | 23.97 |

Locator: Table 2, harness-dependent A-MEM repair contrast · [Source](https://arxiv.org/html/2607.27080v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Figure 4 and lifecycle findings, selected repair outcomes

Each outcome first conditions on successful poisoning within a configuration, then averages 24 configurations equally. F2 covers required benign memories still present after Write, excluding benign content already lost during Write. Semantic retention does not guarantee later retrieval or task success.

Configuration-specific poisoned subsets; no pooled common case denominator.

| Outcome | Configuration macro average (%) |
|---|---|
| Dangerous semantics neutralized F1 | 86.3 |
| Required benign semantics retained F2 | 62.5 |
| Both / selective repair | 56.1 |

Locator: Figure 4 and lifecycle findings, selected repair outcomes · [Source](https://arxiv.org/html/2607.27080v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 7 and Appendix E.6, semantic-judge validation

The same stratified 500 records are labeled independently by two humans; deterministic W1 is excluded. Only agreement accuracy is reported, without checkpoint-specific precision/recall or a guarantee that every full chain is correctly judged.

500 semantic checkpoint records, not 500 complete lifecycle cases.

| Reference labels | Matching labels | Sample size | Agreement (%) |
|---|---|---|---|
| Annotator 1 | 453 | 500 | 90.6 |
| Annotator 2 | 459 | 500 | 91.8 |

Locator: Table 7 and Appendix E.6, semantic-judge validation · [Source](https://arxiv.org/html/2607.27080v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Persistence 84.2% and complete attack 50.3% use all cases; conditional execution 59.6% and repair 56.1% are configuration macro averages on poisoned subsets and cannot simply be multiplied as pooled probabilities. Repair permits correction or explicit invalidation, not necessarily physical erasure; inaccessible caches/latent state are outside the audit. Controlled gateway, Mailpit and GitLab records verify sandbox consequences, not harm to real recipients or production systems. Access to a supported carrier is assumed, so real compromise prevalence is unmeasured. Without repeated-run uncertainty, results describe these configurations and cases.

The construction section names GPT-5.5 as authoring model and says it differs from evaluated backends, but Table 2 also evaluates GPT-5.5. Treat the claimed separation as unresolved. The DeepSeek-V4-Pro judge is also an evaluated backend; independent model-judge sensitivity is not reported. A-MEM uses benchmark patches, fixed DeepSeek-V4-Pro clean initialization and no exposed update operation; it is not an unmodified upstream product. The paper describes released code/manifests, but no implementation URL was located in the inspected paper/PDF or targeted title search; do not claim downloaded implementation verification.



Next: Retain branching and final-state gates, adding clean controls and benign task tests after repair. Compare repair on the intersection of poisoned cases across backends alongside all-case risk. Match capacity, embeddings and call budgets, repeat seeds and swap judges to distinguish memory semantics, adapters and executors.
<!-- EVIDENCE:limitations:END -->
