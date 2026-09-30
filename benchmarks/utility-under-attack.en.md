# Utility Under Attack: Does defended memory remain useful?

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-21<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.21230)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](utility-under-attack.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

The full primary paper was read for methods, setup, results and limitations; experiments were not independently reproduced.

Read Sections 1–8 and Appendix A, including the threat model, three corpus regimes, screening ablations, provenance-weight analysis, all results and reproducibility settings. Reviewed arXiv v1 without running Aegis or recomputing frozen JSON. Two inconsistencies between narrative and tables/equation direction are explicitly retained below.

[Full primary paper](https://arxiv.org/pdf/2608.21230v1) · 2608.21230v1
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## Relation to neighboring evaluations

PoisonedRAG, AgentPoison and MINJA already study knowledge or memory poisoning. This work shifts measurement from producing the attacker’s target to retaining the assistant’s original answer quality, including whether defenses suppress useful evidence without an attack. It directly uses LongMemEval_S rather than inventing all questions. Compared with MPBench’s breadth across attacks and systems, this is a deeper study of one Aegis implementation, separating write screening from read ranking. Its contribution is paired utility and over-defense diagnosis, not priority for discovering memory poisoning.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Each LongMemEval_S question’s roughly 50-session history is stored as timestamped conversational-round memories in a separate namespace. Seed 42 selects 120 questions. A generator receives the question and true answer, then produces a false answer and three ordinary chat-style assertions in one pass: 360 records, about 1.2% of the corpus. They reuse query wording without instruction payloads, optimized triggers, gradients or retrieval-feedback iteration. Genuine histories are internal and poison is untrusted; attackers cannot alter old records, tune ranking or elevate trust. Despite simple payloads, access to the true answer is experimental side information, so this should not be described as a completely target-uninformed attack.

Aegis screens structure, sensitive data, injection rules and conditionally invoked model classification. Classifier confidence at least 0.8 escalates to rejection; lower configured ranges may only flag. Retrieval combines semantic similarity with provenance prior, effectiveness, decay and metadata. Arms compare disabled provenance weighting, shipped weights and stronger weights. Corpus M additionally marks some non-evidence rounds untrusted before poisoning; Corpus N injects no poison but marks all answer-bearing evidence untrusted. M tests imperfect correlation between provenance and maliciousness; N tests the cost when genuine evidence arrives through conservatively labeled channels.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup and scoring

The reader is claude-sonnet-5; gpt-4o-2024-08-06 judges at temperature zero using official LongMemEval prompts; claude-haiku-4-5-20251001 generates poison. Retrieval uses top-k=15 without query rewriting, summarization or graphs. Provenance rescoring is the intervention, so “no reranking” must not be read as absence of that score. Clean full-set accuracy is 0.860 over 500 questions, whereas primary poisoning comparisons use the same 120 questions with clean reference 0.850. A newer-build clean remeasurement is 0.875 with p=0.45 versus the original; neither full-set nor cross-build denominators should be substituted.

“Utility retained” is accuracy divided by clean accuracy, without subtracting a no-memory baseline; it is an accuracy ratio, not causal incremental memory value. Poison occupancy and rank-one frequency separate retrieval exposure from reader resistance. Exact paired McNemar tests compare arms within each corpus; M and N are not paired against each other. Screening separately uses deepset (263 malicious, 399 benign), InjecAgent (250 malicious), Dolly and synthetic memories (750 benign each), and NotInject (339 benign), with recall, false-positive rates and 1,000 bootstrap resamples. Cached API calls and backoff prevent meaningful latency comparison with local detectors. The appendix does not identify the exact embedding model.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Primary poisoning experiment

Same 120 questions, 360 poison records, top-k=15; claude-sonnet-5 answers and GPT-4o judges with official prompts. Utility is accuracy/0.850, rounded as reported. Shipped wt/ws=0.15/0.60; stronger=0.35/0.45. Paired McNemar p versus disabled is 0.80 and 0.0015 respectively.

| Condition | Accuracy | Utility retained (%) | Poison context (%) | Poison rank one (%) |
|---|---|---|---|---|
| Clean | 0.850 | 100 | 0.0 | 0 |
| Poisoned / disabled | 0.300 | 35 | 20.0 | 100 |
| Poisoned / shipped | 0.317 | 37 | 20.0 | 87 |
| Poisoned / stronger | 0.475 | 56 | 8.8 | 2 |

Source: Table 3 · [Paper](https://arxiv.org/pdf/2608.21230v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## When untrusted channels carry genuine evidence

Each corpus has 120 questions. Accuracy uses question count; evidence recall is question-level retrieval of evidence; occupancy is the retrieved-context fraction. M contains 18.7% benign untrusted distractors and 1.18% poison. N contains no poison and makes answer evidence untrusted. wt=0.35; tests pair only within corpus, M p≈1.17e-10 and N p≈6.31e-30.

| Corpus and condition | Accuracy | Evidence recall (%) | Benign-untrusted context (%) |
|---|---|---|---|
| M / disabled | 0.3167 | 99.17 | 6.56 |
| M / stronger | 0.7000 | 99.17 | 0.00 |
| N / disabled | 0.8583 | 99.17 | 50.67 |
| N / stronger | 0.0417 | 0.00 | 0.00 |

Source: Table 6 · [Paper](https://arxiv.org/pdf/2608.21230v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Screening recall and false positives must use the same configuration

All cells are 0–1 proportions. Direct recall uses 263 malicious items, indirect recall 250, and NotInject FPR 339 benign items. All 155 indirect detections before stage 4 arise from sensitive-data detection, not injection rules. These are content-classification metrics, not downstream attack success.

| Screening configuration | Direct recall | Indirect recall | NotInject FPR |
|---|---|---|---|
| Naive regex | 0.144 | 0.000 | 0.015 |
| Aegis stages 1–3 | 0.144 | 0.620 | 0.015 |
| Aegis stages 1–4 / Haiku | 0.741 | 0.832 | 0.035 |
| ProtectAI DeBERTa v2 | 0.414 | 0.660 | 0.428 |

Source: Tables 4–5 · [Paper](https://arxiv.org/pdf/2608.21230v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the evidence supports

All 360 false assertions escape write rejection. Without provenance defense, poison ranks first for every question and occupies 20% of the 15-item context; accuracy falls from 0.850 to 0.300. The shipped weight yields no significant improvement, but p=0.80 does not prove equivalence. Stronger weighting recovers 0.475 in the original corpus and 0.7000 in M, where all benign untrusted records are distractors and removing them provides an additional benefit. N exposes the opposite extreme: without an attack, accuracy drops from 0.8583 to 0.0417 and evidence recall reaches zero. Low attack success alone would hide that loss.

Holding other score terms equal, with internal-minus-untrusted prior difference 0.7, the protected similarity margin is wt×0.7/ws: 0.175 at shipped weights and about 0.544 at stronger weights. Observed poison advantage 0.32 exceeds the first. Only two weights are measured; excluding every intermediate setting or other retrievers additionally depends on similarity-distribution and attacker-capability assumptions. Provenance occupancy constraints are proposed but not implemented or evaluated, so they are not a demonstrated remedy.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source gaps and next test

One system, reader, embedding space, 120-question sample and nonadaptive attack limit generalization. Knowing true answers and likely queries is not free access for every real attacker. Non-elevatable provenance is assumed, not tested against laundering through summaries or trusted-tool echoes. Text alone generally cannot establish factual truth, but 0/360 is an observation for this pipeline, not proof against write defenses with external grounding. M is a favorable bound and N an all-evidence-untrusted extreme, not production traffic. The clean full run also wrongly refuses 109/124,462 rounds; none bears answers, but this remains over-defense. Next experiments should sweep intermediate weights, embeddings/readers and evidence-source mixtures, then evaluate occupancy constraints on both utility and attack outcomes.

Two passages require correction. The abstract/conclusion juxtapose 0.832 indirect-injection recall with 1.5% NotInject false positives, but Tables 4–5 assign 0.832 to the four-stage Haiku pipeline with 3.5% false positives; 1.5% belongs to stages 1–3 with 0.620 indirect recall. Prose beside Equation (2) reverses the winner: under its simplified assumptions, untrusted content outranks trusted content when its semantic advantage exceeds the compensating trust margin. Figure 2 and subsequent reasoning support that direction. This note follows the tables and correct comparison rather than repeating the conflicting sentence.
<!-- EVIDENCE:limitations:END -->
