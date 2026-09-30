# MAPLE: consistency across scientific paper search queries

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-04<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2608.15624)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](maple.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 24 pages: §§1–6, limitations, Appendices A–F, query-generation and judging prompts, and Tables 1–25. Visually checked Tables 5 and 13.

[arXiv v1, 2026-08-16](https://arxiv.org/pdf/2608.15624v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

AllAspect requires every associated query to retrieve its target; AnyAspect requires one. AspectCoverage averages query success within each paper, then across papers. These are paper-level measures, not a three-category checklist (§4.1).
MAPLE-Synth extracts motivation, method and experimental aspects from OpenReview discussions of ICLR 2026 papers, retrieves same-aspect human exemplars from LitSearch/PaSa, and guides GPT-5.4 generation and decontextualization. Retrieval targets full papers; semantic search and full-text relevance judgments select hard negatives, while ACL Anthology provides background negatives. An illustrative quantization paper must be recovered through separate queries about its motivation, technique and experimental conditions, each placing the target within the top twenty rather than relying on one easy aspect.

Editorial placement: LitSearch already links queries to full text, and PaSa introduces researcher-style search. MAPLE adds many queries pointing to one paper and tests consistent recovery across them. It measures retrieval consistency, not survey writing or verification of scientific conclusions. AllAspect also declines as query count and difficulty increase, so its gap from AnyAspect does not alone establish failure to understand a paper.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

The corpus contains 73,973 papers, including 210 targets and 23,739 mined hard negatives; 2,095 queries include 415 multimodal references. GPT-5.4 generates queries; DeepSeek-V4-Pro filters negatives. Text inputs are truncated to model limits; screenshots serve multimodal models. Exact limits, hardware and repeated-run uncertainty are unspecified (§§3–4; Appendices C, F).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected factual cells; scores are percentages. MAPLE-1Q retains the same corpus, representations and ranking procedure while sampling one query per target paper. Main evaluation uses target-paper IDs, not an answer-generation judge.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| GritLM-7B / AllAspect | MAPLE; 210 target papers | AllAspect@20 (%) | 15.7 | Holistic extracted full text; model-limit truncation | Table 5, p. 6 |
| GritLM-7B / AnyAspect | MAPLE; 210 target papers | AnyAspect@20 (%) | 98.1 | Same main-run representation | Table 5, p. 6 |
| GritLM-7B / AspectCoverage | MAPLE; macro-average over 210 papers | AspectCoverage@20 (%) | 61.8 | Average of within-paper query success | Table 5, p. 6 |
| GritLM-7B / MAPLE-1Q | MAPLE-1Q; 210 sampled queries | Recall@20 (%) | 60.00 | Matched corpus, representation and ranking | Table 6a, p. 7 |

Source: [Table 5, p. 6; Table 6a, p. 7](https://arxiv.org/pdf/2608.15624v1)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

Accepted ICLR 2026 papers and generated queries constrain generalization. The abstract-overlap filter does not prove that full text is necessary. Negative labels remain model judgments. Human-exemplar counts conflict: Appendix B gives 11/33/40, Table 11 gives 48/105/47. The abstract’s 15.7% is the main holistic result; later representation experiments reach 24.76% (Table 13).
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Fix query count per paper and representation budget; compare holistic and chunked encoders, with bootstrap intervals clustered by paper. Audit negatives and use independently collected researcher queries before interpreting all-query failure as incomplete scientific understanding.
<!-- EVIDENCE:next:END -->
