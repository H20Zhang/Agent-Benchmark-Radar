# MEMLENS: visual-memory accuracy under controlled history length

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-05-14<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2605.14906)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](memlens.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 63 pages, main §§1–5 and Appendices A–I, including every published prompt, visual example, adapter description, judge audit, matched-subset result, error taxonomy and limitation. Checked the blank page 32 and visually inspected Tables 16/21. Omitted helper prompts and unreproduced code are not claimed as audited.

[arXiv v1 / 2026-05-14](https://arxiv.org/pdf/2605.14906v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

A fixed question and its evidence sessions are embedded into progressively longer, timestamped histories. Images are selected before dialogue generation; entity names are abstracted so text often cannot identify the visual referent. QA covers extraction, cross-session aggregation, temporal reasoning, four-step updates and abstention (§3). In the hat-preference example, successive images anchor changing preferences; the final hat image determines the current value, so recalling an earlier attractive hat fails (Figure 14). This is offline QA over frozen histories, not an online write/delete test.

### Measurement genealogy

LongMemEval supplies the five-ability conversational template, MMLongBench supplies multimodal length accounting, and LoCoMo/Mem-Gallery provide multi-session precedents. MEMLENS adds evidence-image removal controls and shared length conditions. Its comparison is between specified deployed pipelines, not an architecture-only experiment.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The full set has 789 questions. Direct LVLMs use 32K/64K/128K; seven memory agents use a fixed, seed-42 stratified 195-question subset through 256K. Table 16 rescored direct models on those same IDs. Text-only agents receive BLIP-2 captions; M3-Agent receives session composites; M2A/M3C retain embeddings. Qwen3-VL-235B-A22B-Instruct judges binary answers, with independent and human audits. Outputs over 500 parsed words are auto-zeroed; generation caps are 2,048 direct/16,384 thinking tokens. Native image-token accounting, decoding temperatures and agent retrieval budgets are not fully enumerated.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected values retain the paper’s reported scale. Do not rank a 789-question row against a 195-question row as if denominators matched. Image ablation and deterministic rescoring are diagnostic controls, not additional leaderboard cells.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Qwen3.5-122B-A10B / direct | Full MEMLENS; 789 questions | Reported overall accuracy (%), 32K / 128K | 58.68 / 45.50 | Raw interleaved images/text; Qwen3-VL-235B judge | Table 13, p.49 |
| Qwen3-VL-8B (I) / direct | Canonical shared subset; 195 questions | Reported overall accuracy (%), 32K / 128K | 50.77 / 34.36 | Raw images; same subset/judge, different interface from agents | Table 16, p.50 |
| Mem0 / Qwen3-8B | Canonical shared subset; 195 questions | Reported overall accuracy (%), 32K / 128K | 31.79 / 30.26 | BLIP-2 captions; FAISS; no original pixels at answer time | Table 14, p.49 |
| GPT-5.4 / evidence-image ablation | 634 image-essential/supportive questions | Reported accuracy (%), images present / removed | 93.13 / 1.74 | Gold evidence facts; no haystack; not long-context accuracy | Table 3, p.6 |
| All evaluated rosters / closed-form audit | 12,234 model–item pairs at 32K | Accuracy (%), LLM judge / deterministic rule | 42.3 / 37.8 | Mixed full/subset rosters; only deterministically scorable answers | Table 12, p.39 |

Source: [Table 13, p.49; Table 16, p.50; Table 14, p.49; Table 3, p.6; Table 12, p.39](https://arxiv.org/pdf/2605.14906v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The evidence-image ablation covers 634 questions, not all 789, and uses isolated gold facts rather than full histories. Adapter loss, retrieval, backbone and post-training differ jointly; neither score gaps nor error labels isolate their causal contributions. M3-Agent can reread composites, contrary to the blanket claim that all agents lose pixel access. Table 21 and §G.6 use noncanonical scores; some Table 14/16 category totals also fail to reconstruct their stated overall values. Judge rules change closed-form rankings and over-credit answers, so “no leaderboard reordering” is too strong. Four length points do not establish continuous memory safety.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

First reconcile per-item outputs, denominators and all derived totals. On the common 195 IDs, hold checkpoint and answer budget fixed and vary only original pixels, fixed captions and retrievable raw-image pointers. Audit retrieval using all required sessions, not a 0.5-recall threshold; report exact-match, judge and human disagreement together with ingestion cost and retained bytes.
<!-- EVIDENCE:next:END -->
