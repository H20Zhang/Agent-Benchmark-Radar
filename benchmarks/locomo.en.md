# LoCoMo: dialogue QA, event summaries and memory representation

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2024-02-27 · paper v1<br>
> **GPT-3.5-turbo-16K + observation RAG (top-5) — QA overall F1: 41.4**; **GPT-3.5-turbo — Event-summary FactScore F1: 45.9**<br>
> Best automated QA overall F1 in Tables 2–3 and event-summary F1 in Table 4, respectively; human controls excluded. [Original source](https://arxiv.org/html/2402.17753v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](locomo.md) | **English**

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Reviewed the stated paper version, method, experimental setup, key results and limitations; no independent reproduction.

Substantive sections 1–9 and Appendices A–D read in PDF text: generation, three tasks, setup, main results, limitations/impacts, prompts/examples, dataset and implementation, additional results. Table 2/3/4/5/7 values read from PDF extraction. Figure-only plot coordinates not digitized. February v1 result tables additionally checked for historical-reference reconciliation.

[ACL 2024 final proceedings](https://aclanthology.org/2024.acl-long.747.pdf)

[Supplementary source 2402.17753v1, inspected 2026-09-30](https://arxiv.org/html/2402.17753v1)

The frozen release reference is preserved; newer paper results do not replace initial-release scores.
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## How tasks create memory demands

Two persona-conditioned agents converse along dated causal event graphs; humans repair inconsistent dialogue, images and event grounding. Evaluate historical QA, event-summary factual coverage and multimodal continuation separately. Observations convert utterances into speaker-linked factual statements with source turn IDs.

Editorial placement: Relative to shorter multi-session dialogue evaluations, LoCoMo extends persistent personas into longer conversations with image sharing and evaluates QA, event summaries and dialogue generation. Later work reusing only QA does not cover the full original task suite. This is an evaluation-coordinate comparison, not a claim of direct dataset inheritance.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental settings and scoring targets

Ten English test conversations average 588.2 turns, 27.2 sessions and 16,618.1 tokens. There are 1,986 QA items: 841 single-hop, 282 multi-hop, 321 temporal, 96 open-domain and 446 adversarial. Images become BLIP-2 captions for QA/summary. DRAGON retrieves dialogues, observations or summaries; k counts units, not matched tokens. Evaluation temperature 0/top-p 1, one inference run per model.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Larger context can improve recall while weakening abstention

Normalized answer partial-match F1,0–100. Older dialogue truncated for constrained windows; human and model access conditions are not equivalent compute budgets.

1,986 QA items; temporal 321/adversarial 446. These are F1 scores, not counts of correct answers. Overall aggregation is reproduced as reported, not reconstructed from category means.

| System | Context | Overall F1 | Temporal F1 | Adversarial F1 |
|---|---|---|---|---|
| gpt-3.5-turbo / 4K | 4K | 23.9 | 15.6 | 34.8 |
| gpt-3.5-turbo / 16K | 16K | 35.9 | 24.3 | 14.8 |
| gpt-4-turbo / 128K | 128K | 51.6 | 51.4 | 15.7 |
| Human | — | 87.9 | 92.6 | 89.4 |

Locator: ACL final Table 2 · [Source](https://aclanthology.org/2024.acl-long.747.pdf)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Evidence representation changes retrieval and answer quality

Answer F1 / annotated-evidence recall, 0–100. DRAGON retriever and common reader; representation and context length differ.

Same QA benchmark; summary recall counts relevant sessions, not necessarily preservation of their answer facts.

| System | k | Overall F1 | Overall R@k |
|---|---|---|---|
| gpt-3.5-turbo + Dialog RAG / k=5 | 5 | 38.8 | 56.7 |
| gpt-3.5-turbo + Observation RAG / k=5 | 5 | 43.3 | 56.2 |
| gpt-3.5-turbo + Observation RAG / k=25 | 25 | 42.1 | 67.5 |
| gpt-3.5-turbo + Summary RAG / k=5 | 5 | 30.9 | 72.1 |

Locator: ACL final Table 3 · [Source](https://aclanthology.org/2024.acl-long.747.pdf)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Event summaries use a different metric

Adapted atomic-fact summary scores, 0–100. Incremental event summarization; no RAG condition; model and window both differ.

Ten conversations, 35.8 ground-truth events/conversation on average; summary metric differs from QA F1.

| System | Context | FactScore precision | FactScore recall | FactScore F1 |
|---|---|---|---|---|
| Llama-3-70B-Instruct | 4K | 40.3 | 35.6 | 37.8 |
| gpt-4-turbo | 128K | 51.9 | 46.5 | 48.9 |

Locator: ACL final Table 4 · [Source](https://aclanthology.org/2024.acl-long.747.pdf)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and next validation

Evidence representation changes answer quality: observations improve F1 despite similar top-5 evidence recall, and higher recall need not improve answers. The ten synthetic, human-edited dialogues, single runs, lexical scoring and caption substitution limit external validity; no architecture-only effect or deployment gain is established.

February v1 and ACL final contain different models/results; historical 41.4/45.9 confirmed in v1 Tables 3/4. ACL Table 3 extraction has an observation row k=5 after k=25; omitted that ambiguous row from selected facts. ACL prose contains inconsistent Gemini naming versus Table 2; use the printed Table 2 model labels. Do not infer normalized lexical F1 as binary accuracy.

Next: Retain original QA F1 alongside any later judge. Fix reader, test items and token budget; compare raw turns, observations, full history and supplied evidence. Pair with LongMemEval for temporal updates and MemoryArena for whether recovered history changes action success.
QA and summaries use 10 human-edited dialogues; MiniGPT-5 continuation training uses 50 additional unfiltered dialogues. The ACL final RAG reader is labeled gpt-3.5-turbo, distinct from the original 16K label.
<!-- EVIDENCE:limitations:END -->
