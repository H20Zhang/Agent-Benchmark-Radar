# InjecMEM: separating memory exposure from output steering

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-24<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.23471)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](injecmem.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Substantive main 1–5 and Appendices A–H read, including threat model, metric equations, defenses, corpus construction, transfer procedures/artifacts and qualitative fused-context cases. No attack execution, implementation audit or independent reproduction; note omits operational payloads.

[arXiv 2608.23471v1 (2026-08-24)](https://arxiv.org/html/2608.23471v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

This is a memory-injection method and controlled evaluation protocol. One submitted interaction is logged; later topic queries may retrieve it and alter responses. The method separates topic retrieval exposure from generation-side interference optimized on accessible backbones and varied surrogate contexts. Store internals are black-box, but the backbone is white-box and final-prompt format is recovered beforehand. Evaluation separates retrieved-page exposure, target-string generation conditional on retrieval and their joint occurrence.

Editorial placement: Compared with direct retrieval-store poisoning such as AgentPoison, InjecMEM uses a logged interaction that later enters memory retrieval and separates exposure from generation steering. This changes the threat model and attack pipeline; conditional attack success is not a general memory-quality score. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Primary backbone Qwen2.5-7B-Instruct, mainly MemoryOS with additional MemGPT evaluation. Synthetic corpus: 944 conversations/3096 user–assistant pages across 19 domains; about 50 held-out queries/domain and 10 full-pipeline seeds. Prefill precedes injection, followed by non-target dialogue drift. RSR measures presence in the fused prompt; ASR-c conditions on retrieval; ASR-j uses all target queries. Success is normalized target-string matching, not successful harmful action. Numeric retrieval capacities/decoding settings are incompletely reported.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Table 3, controlled system comparison

Primary Qwen2.5-7B-Instruct; MemGPT reuses the MemoryOS-optimized generation component under a different prompt layout. 76.6% is not end-to-end risk.

19 domains, about 50 queries/domain, 10 seeds; ASR-c only retrieved cases, exact per-row conditional counts not supplied

| System | Retrieval RSR (%) | Conditional ASR-c (%) | Joint ASR-j (%) |
|---|---|---|---|
| MemoryOS | 46.5 | 76.6 | 35.6 |
| MemGPT | 37.2 | 48.6 | 18.1 |

Locator: Table 3, controlled system comparison · [Source](https://arxiv.org/html/2608.23471v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Table 6, selected retrieve-time defenses

Attack filtering occurs after retrieval; BBR is separately measured at ingestion. Judge detector Qwen2.5-0.5B at threshold 0.5; perplexity threshold selected by sweep. Dashes preserve unreported values; conditional ASR is undefined when RSR=0.

Main controlled queries; BBR uses separate benign ingestion pages, count unspecified

| Defense | RSR (%) | ASR-j (%) | ASR-c (%) | Benign write blocking BBR (%) |
|---|---|---|---|---|
| No defense | 46.5 | 35.6 | 76.6 | 0 |
| LLM-as-a-Judge | 36.2 | 27.3 | 75.4 | 0.65 |
| Perplexity | 0 | — | — | 71.8 |

Locator: Table 6, selected retrieve-time defenses · [Source](https://arxiv.org/html/2608.23471v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Table 5, joint-training transfer selected metric

Joint optimization used Qwen and Mistral; Llama is a held-out family. Conditional steering illustrates the transfer boundary, not overall risk.

Retrieved cases only; exact conditional counts not supplied

| Test backbone | Jointly optimized ASR-c (%) |
|---|---|
| Qwen2.5-7B-Instruct | 70.5 |
| Mistral-7B-Instruct-v0.3 | 43.2 |
| Llama-3.1-8B-Instruct | 0 |

Locator: Table 5, joint-training transfer selected metric · [Source](https://arxiv.org/html/2608.23471v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## Table 8, WildChat-background check

WildChat provides non-target prefill/drift conversations; other settings follow the main experiment. SD is not a confidence interval or a clinical/financial outcome score.

Three seeds/topic; first-query retrieval setting; exact per-seed sample count not separately given

| Topic | RSR@1 mean (%) | ASR-j mean (%) | ASR-j SD (points) |
|---|---|---|---|
| Health | 64.7 | 46.0 | 5.29 |
| Finance | 60.0 | 40.7 | 7.02 |

Locator: Table 8, WildChat-background check · [Source](https://arxiv.org/html/2608.23471v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Results expose a vulnerability in raw-interaction-retaining systems under the specified white-box optimization, not an upper risk bound for all memory architectures. Aggressive rewriting remains untested. Retrieval-filter security and write-time benign blocking measure different stages; zero BBR does not prove intact task utility. WildChat supplies benign backgrounds for two topics, not deployment evidence. Held-out-family failure limits transfer; concatenated per-family attacks are not universal zero-shot transfer. Non-target preservation lacks a broad quantitative utility evaluation.

Appendix A table leaves conditional ASR undefined at RSR 0, while threshold prose calls it 0. Preserve undefined denominator rather than claim measured 0. BBR is benign write-time rejection although attack defenses operate at retrieval time. Table 1 RSR@k is over first k topic queries, not retrieval top-k; Table 3 overall 46.5 has a different aggregation and should not be substituted for Table 1@50=35.4. Domain-average metrics should not be assumed to multiply exactly; pooling weights/counts not fully supplied. BadChain comparison adapts/compresses its multistep procedure and omits a fixed victim trigger; 0% is only for this adapted setting. Single poisoning interaction does not count prior prompt-format recovery or offline white-box optimization as free black-box access.



Next: Measure write retention, retrieval exposure, conditional steering and joint steering separately under matched queries/budgets. Pair per-stage false blocking with benign task success, including rewrite-heavy stores and longer drift. Separate trained backbones, unseen same-family variants and unseen families using non-operational targets.
<!-- EVIDENCE:limitations:END -->
