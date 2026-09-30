# Mem-Gallery: organization and updating of multi-session visual-text memory

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-01-07<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://aclanthology.org/2026.acl-long.1892/)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](mem-gallery.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading coverage and version

Full substantive paper and appendix reading completed for the stated version; experiments were not independently reproduced.

Read all 35 proceedings pages, pp.40750–40784: §§1–5, limitations and Appendix A.1–A.10, including full task definitions, baseline implementations, metrics, all retrieval/backbone tables and all three illustrated case studies. Visually checked Tables 4/12 and the visual-reasoning case.

[ACL 2026 / 2026-07 / 2026.acl-long.1892](https://aclanthology.org/2026.acl-long.1892.pdf)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## Method and measurement

Human-designed stories and reorganized MMRC sessions become long image–text conversations; annotations identify supporting rounds. Memory accumulates round by round before answering nine task types spanning extraction/adaptation, reasoning and knowledge management. Test-time learning means using newly seen exemplars without parameter updates (§3; Appendix A.3).

In one case, a new dog photograph must be compared with a friend’s previously mentioned pet. UniversalRAG retrieves the Cairn Terrier clue yet contradicts that clue in its final comparison; retrieval success alone therefore does not establish visual reasoning success (Figure 17).

### Measurement genealogy

LoCoMo supplies the multi-session conversational precedent, while MMDU/MMRC supply localized multimodal dialogue precedents and some construction material. Mem-Gallery joins cross-session persistence with visual search, exemplars and corrections. The next coordinate is isolating perceptual loss, memory loss and post-retrieval reasoning under the same evidence budget.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup

Twenty conversation scenarios contain 240 sessions, 3,962 rounds, 1,003 history images and 1,711 QA pairs. Text methods receive GPT-5.1 captions. MemEngine uses a fixed seed, temperature 0, GME-Qwen2-VL-2B-Instruct embeddings and default top-10 retrieval; open backbones run with vLLM on A100s. Other method settings follow original implementations; exact caps and repeat counts are unspecified. F1 is mean normalized token overlap; the separate Qwen-2.5-72B-Instruct judge uses five grades from 0 to 1 (Appendices A.2, A.5).
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:results:START -->
## Selected quantitative evidence

Selected factual cells. Answer F1 is averaged across 1,711 QA pairs. Retrieval recall averages the recovered-clue fraction over 1,527 supported questions, excluding 184 refusal questions; that denominator is calculated from Table 8 and the Table 16 exclusion rule. No LLM judge is used for these selected F1/recall values.

| System / comparison | Dataset / denominator | Metric / unit | Result | Conditions | Source |
| --- | --- | --- | --- | --- | --- |
| A-Mem / Qwen-2.5-VL-7B | Mem-Gallery; 1,711 QA pairs | Mean answer F1 (0–1) | 0.6228 | Top-10 where applicable; GPT-5.1 captions | Table 4, p.40756 (PDF p.7) |
| MuRAG / Qwen-2.5-VL-7B / K=10 | Mem-Gallery; 1,711 QA pairs | Mean answer F1 (0–1) | 0.6966 | Top-10 multimodal memory; same embedder | Table 4, p.40756 (PDF p.7) |
| MemGPT / Gemini-2.5-Flash-Lite | Mem-Gallery; 1,711 QA pairs | Mean answer F1 (0–1) | 0.7202 | Text memory with GPT-5.1 captions; native memory control | Table 12, p.40776 (PDF p.27) |
| MuRAG / Gemini-2.5-Flash-Lite | Mem-Gallery; 1,711 QA pairs | Mean answer F1 (0–1) | 0.7155 | Top-10 multimodal memory | Table 12, p.40776 (PDF p.27) |
| MuRAG / Qwen-2.5-VL-7B / K=20 | Mem-Gallery; 1,711 QA pairs | Mean answer F1 (0–1) | 0.6884 | Top-20; same corpus and answerer | Table 15, p.40780 (PDF p.31) |
| MuRAG / clue recall / K=10 | Mem-Gallery; 1,527 supported questions (derived) | Mean Recall@10 (0–1) | 0.8601 | Annotated clue entries; no refusal questions | Table 16, p.40781 (PDF p.32) |
| MuRAG / clue recall / K=20 | Mem-Gallery; 1,527 supported questions (derived) | Mean Recall@20 (0–1) | 0.9228 | Same clue protocol; expanded retrieval | Table 16, p.40781 (PDF p.32) |

Source: [Table 4, p.40756 (PDF p.7); Table 12, p.40776 (PDF p.27); Table 15, p.40780 (PDF p.31); Table 16, p.40781 (PDF p.32)](https://aclanthology.org/2026.acl-long.1892.pdf)
<!-- EVIDENCE:results:END -->

<!-- EVIDENCE:limitations:START -->
## Limits and interpretation

The backbone-specific reversal in the preceding table prevents a universal claim that caption memory is inferior. Equal retrieved-entry counts do not equal image-token or compute budgets, and full-memory baselines truncate. Higher recall at larger K need not improve answer F1. The judge explicitly rewards confidence and penalizes some hedging/filler, introducing style sensitivity; no independent human judge-calibration study is reported. These are synthetic conversational results, not deployment or action-safety evidence.
<!-- EVIDENCE:limitations:END -->

<!-- EVIDENCE:next:START -->
## Next experiment

Use clue-provided images and matched caption token budgets to separate perception from retrieval. Cross these controls with fixed backbone and memory updates, then measure answer F1, clue recall and correction success with per-conversation uncertainty and complete image/ingestion costs.
<!-- EVIDENCE:next:END -->
