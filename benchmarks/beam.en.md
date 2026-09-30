# BEAM: memory evaluation across long synthetic conversations

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-10 · paper v1<br>
> **LIGHT / Llama-4-Maverick — Average @500K: 0.359**; **LIGHT / Llama-4-Maverick — Average @10M: 0.266**<br>
> Best ten-ability averages at the selected lengths in Table 1; 500K and 10M are different settings. [Original source](https://arxiv.org/html/2510.27246v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](beam.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 80 pages: §§1–6 and Appendices A–G, including generation algorithms, all 44 prompt listings, complete provided task and scratchpad examples, and ablation/retrieval tables. Visually checked Tables 1 and 8. A later v2 exists; these results remain tied to v1.

[arXiv v1 / 2025-10-31](https://arxiv.org/pdf/2510.27246v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

BEAM generates narrative plans, expands them into user–assistant conversations, then human-validates probes and atomic answer criteria. Each conversation has two probes for each of ten abilities. Nine abilities use 0/0.5/1 criterion satisfaction; event ordering uses LLM-aligned Kendall tau-b. The displayed average therefore is not binary answer accuracy (§2).

A contradiction probe asks about prior attendance after incompatible statements; the reference expects both claims and a clarification request. Event ordering follows when topics were mentioned, not necessarily real-world event dates (Appendices B.6, D; Listings 6, 16).

### Measurement genealogy

Relative to LoCoMo and LongMemEval’s conversational-memory tests, BEAM adds much longer planned narratives, broader domains and a ten-ability profile. LIGHT combines an episodic index, recent-turn working memory and a compressed scratchpad. The remaining coordinate is whether the same supported questions survive longer histories at matched ingestion and answer-time cost.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The dataset contains 100 conversations and 2,000 probes. Inference temperature is 0. RAG retrieves five dialogue pairs with BGE-small-en-v1.5/FAISS. LIGHT additionally uses Qwen2.5-32B-AWQ for indexing/filtering and GPT-4.1-nano to compress scratchpads from a 30K threshold toward 15K tokens. Qwen uses 128K for vanilla and 32K for RAG/LIGHT. At 10M, vanilla sees only the recent window. Judge identity, working-memory length, repeated runs and per-bucket sample counts are not pinned (§§3–4).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected factual rows from v1. The denominator of Average is ten ability scores; nine aggregate rubric nuggets and one uses event-order correlation. Each chat contributes twenty probes, but counts by length bucket are not reported. The judge model is unspecified.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| Llama-4-Maverick-fp8 / LIGHT / 500K | BEAM v1 500K bucket; mean over 10 abilities; bucket question count unstated | Reported mixed-metric average (unitless) | 0.359 | Key–value index, filtered scratchpad, recent turns | Table 1, p.8 |
| Llama-4-Maverick-fp8 / RAG / 500K | BEAM v1 500K bucket; mean over 10 abilities; bucket question count unstated | Reported mixed-metric average (unitless) | 0.330 | Top-5 raw dialogue pairs; same BGE embedder | Table 1, p.8 |
| Llama-4-Maverick-fp8 / LIGHT / 10M | BEAM v1 10M bucket; mean over 10 abilities; bucket question count unstated | Reported mixed-metric average (unitless) | 0.266 | Key–value index, filtered scratchpad, recent turns | Table 1, p.8 |
| Llama-4-Maverick-fp8 / RAG / 10M | BEAM v1 10M bucket; mean over 10 abilities; bucket question count unstated | Reported mixed-metric average (unitless) | 0.249 | Top-5 raw dialogue pairs; same BGE embedder | Table 1, p.8 |
| Gemini-2.0-flash / LIGHT / 10M | BEAM v1 10M bucket; mean over 10 abilities; bucket question count unstated | Reported mixed-metric average (unitless) | 0.192 | Key–value index, filtered scratchpad, recent turns | Table 1, p.8 |
| Gemini-2.0-flash / RAG / 10M | BEAM v1 10M bucket; mean over 10 abilities; bucket question count unstated | Reported mixed-metric average (unitless) | 0.216 | Top-5 raw dialogue pairs; same BGE embedder | Table 1, p.8 |

Source: [Table 1, p.8](https://arxiv.org/pdf/2510.27246v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The selected Gemini rows refute a universal LIGHT advantage. Table 8 also shows benefits from removing working memory at some shorter lengths, contrary to the blanket claim that every component always helps. Its first two base averages differ from Table 1’s Qwen rows, and the ablation backbone is not explicitly identified. Early-evidence-biased generation and different questions across length groups preclude a pure length-effect estimate.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Use identical probes and evidence at several history lengths, match total retrieved and scratchpad tokens, and publish ingestion calls/cost. Pin the judge and event-alignment procedure, validate a blinded human subset, and report each ability separately with conversation-clustered uncertainty.
<!-- EVIDENCE:next:END -->
