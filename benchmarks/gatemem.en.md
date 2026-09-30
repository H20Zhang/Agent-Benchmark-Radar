# GateMem: usefulness, access and post-deletion leakage in shared memory

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-06-17<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2606.18829)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](gatemem.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Main §§1–5 and substantive Appendices A–E read through HTML, with exact assistant/judge templates checked in PDF pp 19–21 and selected Tables 2/3/4/7/8/9 confirmed in v1 PDF. Figure curves not independently digitized; no reproduction or implementation audit.

[arXiv2606.18829v1 (2026-06-17)](https://arxiv.org/pdf/2606.18829v1)

The frozen release reference is preserved. Newly reviewed versions and conditions do not replace initial-release results.
[Versioned HTML 2606.18829v1](https://arxiv.org/html/2606.18829v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Task construction and memory observation

Stream multi-principal facts, permission changes and deletion requests into shared memory. At hidden checkpoints, provide the authenticated requester, policy and visible memory, then request an answer, redacted answer, refusal or no-memory response. Continue the episode and score legitimate usefulness, unauthorized disclosure and post-deletion recovery.

Editorial placement: Compared with LongMemEval’s historical-information QA, GateMem adds use, access-denial and forgetting checks. Correct recall can fail when the fact should not be used, adding lifecycle/access evidence beyond QA accuracy. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental conditions and scoring targets

91 episodes and 2218 checkpoints: 728 utility, 727 access-control and 763 forgetting checks. Reset per episode; ingest chronologically. Answer temperature 0.2/max 4096 tokens; GPT-4o judge temperature 0/max 4096; text-embedding-3-small embeddings. Long-Context uses up to 300 recent turns; both RAG variants retrieve 20, with policy filtering potentially returning fewer. A-MEM final evidence 20; Mem0 update window 10/similar memories 5; REMem-I up to 5 reasoning steps.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Medical tasks: utility and leakage trade off

Same domain and backbone; Appendix D content labels without additional action gating. MGS=100×(U/100)×(1−A/100)×(1−F/100). Do not rank across the two blocks.

210 utility, 192 access, 177 forgetting checkpoints

| System | Utility U ↑ (%) | Access leakage A ↓ (%) | Deletion leakage F ↓ (%) | MGS ↑ (%) |
|---|---|---|---|---|
| Long-Context | 64.8 | 24.0 | 7.3 | 45.6 |
| RAG-Naive | 46.7 | 58.9 | 24.9 | 14.4 |
| RAG-Policy | 28.1 | 17.2 | 7.3 | 21.6 |

Locator: Table 3, Medical / GPT-4o-mini · [Source](https://arxiv.org/pdf/2606.18829v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Office tasks: results depend on the backbone and domain

Same domain and backbone; Appendix D content labels without additional action gating. MGS=100×(U/100)×(1−A/100)×(1−F/100). Do not rank across the two blocks.

154 utility, 171 access, 222 forgetting checkpoints

| System | Utility U ↑ (%) | Access leakage A ↓ (%) | Deletion leakage F ↓ (%) | MGS ↑ (%) |
|---|---|---|---|---|
| Long-Context | 89.6 | 33.9 | 4.5 | 56.5 |
| RAG-Naive | 74 | 29.8 | 9.5 | 47 |
| RAG-Policy | 76 | 19.9 | 6.3 | 57 |

Locator: Table 3, Office / GPT-5.4 · [Source](https://arxiv.org/pdf/2606.18829v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Fewer tokens do not guarantee faster responses

Mean end-to-end wall time includes ingestion. Tokens are not currency, storage or total compute; typical concurrency 4–8.

579 medical checkpoints, 21 episodes

| System | Seconds/checkpoint ↓ | Thousand LLM tokens/checkpoint ↓ |
|---|---|---|
| Long-Context | 4.22 | 4.04 |
| RAG-Policy | 11.1 | 1.15 |
| A-MEM | 41.76 | 1.37 |
| Mem0 | 85.9 | 1.27 |

Locator: Table 4, GPT-4o-mini Medical selected rows · [Source](https://arxiv.org/pdf/2606.18829v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:result-4:START -->
## How closely did the judge match human labels?

Stratified 289 of 579 outputs from one run; at least two human annotators with adjudication. Judge validation, not system success.

Sample sizes are shown in the table.

| Field | Sample size | Judge–human agreement (%) |
|---|---|---|
| Utility correctness | 105 | 99.0 |
| Access leakage | 96 | 99.0 |
| Deletion leakage | 88 | 97.7 |

Locator: Table 9, human validation selected fields · [Source](https://arxiv.org/pdf/2606.18829v1)
<!-- EVIDENCE:result-4:END -->

<!-- EVIDENCE:limitations:START -->
## Supported conclusions and unresolved questions

Utility and leakage trade off even within a backbone. Context length, filtering, indexing and calls vary, preventing a memory-structure-only causal interpretation. MGS multiplies three rates rather than pooling checkpoint accuracy. Human validation covers 289 outputs from one run, not every domain/backbone. Synthetic institutional episodes do not establish real-world compliance.

HTML body displays an August 24 date despite v1 header; selected facts/tables and prompts verified against explicit v1 PDF dated June 18. Do not infer an experiment date. §3 metric equations include action conditions whereas Appendix D and exact judge prompt describe content-only leakage without extra action gating for main tables.

Next experiment: Hold backbone, stream and total budget fixed; report both content leakage and action accuracy on paired checkpoints, then vary retrieval depth and access filtering separately. Add paraphrased and multi-turn probes after revocation plus storage-level deletion audits; pair with ordinary long-horizon QA to expose usefulness and governance costs.
Scenarios already cover delegation, evolving permissions and impersonation; real authentication, deployment and storage-level erasure remain unverified.
<!-- EVIDENCE:limitations:END -->
