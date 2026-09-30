# MedMemoryBench: checkpoint QA over simulated longitudinal healthcare histories

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-12<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.11814)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](medmemorybench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 27 pages, main §§1–7 and Appendices A–G, including annotation qualifications, supplementary backbone/judge results, complete answering/judging prompts, baseline adaptations and research-only restrictions. Visually checked the main table and budget/cost figures.

[arXiv v1 / 2026-05-12](https://arxiv.org/pdf/2605.11814v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Twenty de-identified case-derived profiles are expanded into synthetic one-year event graphs. Patient/physician agents generate sessions, and accumulated summaries guide later simulation. High-priority facts such as allergies and contraindications seed memory-dependent queries; humans can revise inconsistent earlier dialogue after QA construction (§4).

In the sleep-apnea illustration, device-use duration and a sleep-related index change across visits; a later question must connect the appropriate historical measurement with the current stage, rather than copy the latest matching phrase (Figure 3). This is a benchmark scenario, not treatment guidance. Evaluation ingests chronological sessions and asks eligible queries every ten sessions, excluding future evidence (§5).

### Measurement genealogy

LoCoMo contributes a noise-injection preliminary test; LongMemEval and MemoryAgentBench supply prior updating/streaming coordinates. MedMemoryBench applies these concerns to medically structured histories with heterogeneous fact priority. Its novelty is this domain-specific combination, not evidence that all earlier memory benchmarks were static or noise-free.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

There are 2,020 sessions, 15,988 turns and 1,939 questions; Mixed adds roughly 200 auxiliary sessions per profile, including general-health and family-proxy dialogue. Six tasks cover Entity Exact Match (EEM), Temporal Location Accuracy (TLA), State Update Accuracy (SUA), Multiple Choice (MQ), Inference Generation (IG), and Multi-hop Clinical Deduction (MCD), using exact string/option matching or binary judging. Main systems share GPT-5.1, BGE-small-v1.5, default top-5 and chunk size 4,096; T=0.3 and output cap 10,240. Raw-history control has 128K context. MCD requires node/causal coverage ≥0.75, chain completeness ≥0.7 and the correct conclusion. Repetitions, confidence intervals and exact checkpoint weighting are not supplied.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected Table 2 comparisons, preserving reported values. Efficient and Mixed share clinical questions but differ in auxiliary history and potentially checkpoint placement. Default top-5 does not equal identical token exposure when memory units and persistent core memory differ.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Long-Context | 1,939 queries; six task-type accuracies averaged | Reported Avg. (%), Efficient / Mixed | 51.58 / 38.75 | Raw history; 128K context window; GPT-5.1; Claude-4-Sonnet judge where needed | Table 2, p.7 |
| Letta | 1,939 queries; six task-type accuracies averaged | Reported Avg. (%), Efficient / Mixed | 51.21 / 41.55 | Core memory plus retrieved memory; GPT-5.1; Claude-4-Sonnet judge where needed | Table 2, p.7 |
| A-Mem | 1,939 queries; six task-type accuracies averaged | Reported Avg. (%), Efficient / Mixed | 44.84 / 29.27 | Stored memory entries; GPT-5.1; Claude-4-Sonnet judge where needed | Table 2, p.7 |
| Embedding | 1,939 queries; six task-type accuracies averaged | Reported Avg. (%), Efficient / Mixed | 42.15 / 40.78 | Dense retrieval; BGE-small-v1.5; GPT-5.1; Claude-4-Sonnet judge where needed | Table 2, p.7 |
| A-Mem / MCD | 191 multi-hop clinical deduction questions | Accuracy (%), Efficient / Mixed | 31.93 / 10.80 | GPT-5.1; top-5 default; three judge thresholds plus correct conclusion | Table 2, p.7; Appendix D.2, p.25 |

Source: [Table 2, p.7; Appendix D.2, p.25](https://arxiv.org/pdf/2605.11814v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Table 2 Avg. reproduces an unweighted mean of six task accuracies, not a verified pooled accuracy over 1,939 queries. Letta narrowly trails raw history in Efficient; gains in some Mixed cells mean degradation is not universal per task. Appendix E buffers HippoRAG-v2 until a final-session index call, leaving its checkpoint behavior unresolved; MIRIX and ReMem also receive substantial adaptations. Annotation staff are identified as medical-division engineers, without explicit clinician credentials. Human agreement is 87.5% on 200 judged outputs, with weaker inference-generation agreement. Hallucination is non-refusal among incorrect answers, not harm per encounter. No clinical efficacy or deployment safety follows.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Audit checkpoint traces to prove each method has indexed only available history and aligns Mixed/Efficient queries at equivalent clinical states. Hold query evidence fixed, vary noise separately from history length, and add oracle retrieval at every checkpoint. Report patient-cluster uncertainty and separate stale-state, proxy-person confusion, missing evidence and medically plausible alternative reasoning.
<!-- EVIDENCE:next:END -->
