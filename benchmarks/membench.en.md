# MemBench: memory accuracy, latency and history-length stress tests

<!-- RELEASE-REFERENCE:START -->
> **Best at release (historical reference)** · 2025-06 · paper v1<br>
> **RetrievalMemory / Qwen2.5-7B — Factual participation @100K accuracy: 83.3%**; **RetrievalMemory / Qwen2.5-7B — Factual observation @100K accuracy: 93.3%**<br>
> Separate best 100K factual-memory settings in Table 3 with Qwen2.5-7B fixed; no synthetic overall score including reflective memory. [Original source](https://arxiv.org/html/2506.21605v1)<br>
> Historical difficulty reference, not current SOTA; tasks, versions, and experimental conditions are not interchangeable.
<!-- RELEASE-REFERENCE:END -->

[中文](membench.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 17 pages, including §§1–5, limitations and Appendices A–D: profiles, factual/reflective examples, statistics, generation prompts and detailed results. Visually checked Tables 3–4 and 10–12.

[arXiv v1 / 2025-06-20](https://arxiv.org/pdf/2506.21605v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

MemBench starts from user–entity graphs, turns attributes into evidence-bearing conversations or observed messages, inserts unrelated news-derived material, and ingests the result chronologically. Synthetic streams test factual recall and preference/emotion inference. Participation replays predefined assistant replies; it does not measure an agent’s freely chosen actions. Answers are multiple-choice, scored against labels. Recall@10 concerns evidence retrieval; latency concerns individual memory operations (§§3–4).

For example, a correction changes an event duration from four days to one; the later choice question should use the corrected value. Repeated preferences for different sweet-and-salty dishes support a higher-level taste judgment (Figure 3; Appendix A.4).

### Measurement genealogy

MemSim supplies the graph-based simulation foundation. Compared with long-history QA in LoCoMo and LongMemEval, MemBench makes participation versus observation and factual versus reflective content explicit evaluation coordinates, alongside operation time and history-length stress. The next coordinate is whether these stored or inferred memories improve subsequent actions under matched costs.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Main runs use MemEngine, Qwen2.5-7B and multilingual-e5-small. News-derived noise lengthens histories. Ordinary samples contain 360/280 factual and 120/60 reflective items for participation/observation; enlarged samples contain 90/84 and 30/15. Exact memory caps, sampling settings, timing hardware and repetition counts are not specified.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected reported values, not a composite ranking. Accuracy is correct choices divided by evaluated questions; the paper reports sampled item counts but does not fully reconcile effective denominators. Timing is seconds per memory operation, not complete answer latency.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| RetrievalMemory / Qwen2.5-7B / participation | Factual, nominal 100K; 90 sampled items | Choice accuracy (0–1) | 0.833 | MemEngine; multilingual-e5-small; noisy history | Table 3, p.7 |
| FullMemory / Qwen2.5-7B / participation | Factual, nominal 100K; 90 sampled items | Choice accuracy (0–1) | 0.489 | Same factual sample; window cap unspecified | Table 3, p.7 |
| RetrievalMemory / Qwen2.5-7B / observation | Factual, table labels 100K; 84 sampled items; effective denominator unresolved | Choice accuracy (0–1) | 0.933 | MemEngine; multilingual-e5-small | Table 3, p.7 |
| GenerativeAgent / Qwen2.5-7B / write | Factual participation; per operation; timing sample size unspecified | Write latency (seconds / operation) | 6.116 | Memory write only; hardware unspecified | Table 3, p.7 |
| GenerativeAgent / Qwen2.5-7B / preference | Ordinary reflective participation; per-slice denominator unspecified | Choice accuracy (0–1) | 0.742 | Preference slice; predefined dialogue | Table 10, p.17 |
| GenerativeAgent / Qwen2.5-7B / emotion | Ordinary reflective participation; per-slice denominator unspecified | Choice accuracy (0–1) | 0.412 | Emotion slice; predefined dialogue | Table 10, p.17 |

Source: [Table 3, p.7; Table 10, p.17](https://arxiv.org/pdf/2506.21605v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Table 4 repeats all RetrievalMemory accuracy cells from Table 3; retain them as reported, not independently confirmed. Its ordinary reflective scores match preference columns in Table 10, which separately reports emotion. Observation lengths conflict between §4.1 and table headings, and 0.933 cannot be reconstructed from 84 single binary trials. Capacity curves therefore do not identify an architecture-only storage limit.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Release an item-level scoring ledger, reconcile the duplicated cells and lengths, and repeat with fixed answerer/context caps. Plot factual, preference and emotion accuracy against ingestion and query cost, using the same questions as noise increases.
<!-- EVIDENCE:next:END -->
