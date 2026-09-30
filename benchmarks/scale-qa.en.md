# SCALE-QA: Reconstructing the operative episode in interleaved dialogue

<!-- RELEASE-REFERENCE:START -->
> **Release result (historical reference; not a best claim)** · 2026-08-26 · paper v1 snapshot<br>
> **Full Context / GPT-4o-mini — Accuracy: 29.8%** (128K Full Context accuracy)<br>
> Original full-context baseline, not a launch winner inferred from one recorded score. [Original source](https://arxiv.org/abs/2608.25655)<br>
> From a previously curated original-paper record, for historical reference; not rerun in this update and not current SOTA.
<!-- RELEASE-REFERENCE:END -->

[中文](scale-qa.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

The full primary paper was read for methods, setup, results and limitations; experiments were not independently reproduced.

Read Sections 1–9 and Appendices A–F: construction/human audits, runtime packing, TSIM implementation and configuration selection, all primary results/ablations, million-token diagnostic, transfer, statistics and costs. Reviewed the August 26, 2026 first version without executing code. Closed-loop evidence hit, independent exact-evidence recall and different sample sizes are kept distinct.

[Full primary paper](https://arxiv.org/pdf/2608.25655v1) · 2608.25655v1
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## Relation to neighboring evaluations

The closest predecessor is LongMemEval: decisive historical evidence is embedded in scalable chat distraction. SCALE-QA removes supplied session/topic boundaries, replaces direct personal-fact QA with task decisions governed by local constraints, and uses deterministic four-choice grading. The recovery unit becomes the episode jointly establishing a rule, exception and scope rather than one relevant sentence. It adopts the scalable-history/distractor design but generates new audited counterfactual questions; LongMemEval is evaluated separately for transfer. Episode-integrity failure can coexist with retrieval misses, positional effects and update errors rather than forming a mutually exclusive taxonomy.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Each domain starts with 5–10 human seeds, expanded by models into dialogue, four options, a label and exact evidence. Ten domains contribute 300 questions each, totaling 3,000, with 750 labels per option. The codex and claude-code partitions contain 1,500 records each; these are dataset labels, not evaluated methods. Fictional organizations, local policies, nonstandard identifiers and counterintuitive exceptions reduce generic-prior shortcuts. Machine filters accept 28.8% and three reviewers accept 84.3% of reviewed candidates; all 3,000 final records pass full-turn exact alignment across 4,346 evidence snippets. An illustrative model-selection question depends on an earlier episode imposing a single-consumer-GPU/CPU policy and reduced budget. Recalling only a lightweight preference can omit the binding rule; this is local evidence reasoning, not universal hardware advice.

The runtime builder mixes backgrounds with chat noise into an unsegmented turn stream. Reported experiments use an author-generated seed plus WildChat; the public default instead uses UltraChat, so exact reproduction needs the pinned WildChat rebuild and hashes. Length is estimated as roughly 1.3 times whitespace words. Truth backgrounds total about 393,245 estimated tokens; smaller targets use deterministic capacity-constrained batches with a default 0.82 truth cap. The main 128k setting has four batches. Memory persists with answer writeback inside each batch and resets between batches, allowing earlier answers to affect later context.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Experimental setup and scoring

TSIM embeds turns with BAAI/bge-large-en-v1.5, comparing incoming turns with a recent-four-turn semantic center at threshold 0.70, adding 0.03 for model-to-user transitions, with 120/320 estimated-token episode guards. It indexes raw turns, episode summaries and clusters. Summaries are deterministic recency/ID-prefixed text truncated to 1,200 characters; cluster summaries combine recent members, without LLM summarization calls. It retrieves 28/20/2 items across views, maps hits to episode scores and selects five episodes, capping prompt units at eight messages with two-message overlap. Cluster text routes evidence rather than entering the answer prompt.

Each 16k–128k main setting uses all 3,000 questions. The 128k backbones are Gemma2:9b, Gemini 2.5 Flash and GPT-4o-mini, with one frozen TSIM configuration. Configuration selection uses 300 search questions, 600 confirmation questions, 200 answer-validation questions and a full-set retrieval check; the full result is not wholly untouched blind testing. Accuracy is correct four-option selection, with 25% random chance. CL Hit is expected-evidence presence along backend-conditioned closed-loop trajectories and should be compared within backbone. Rationale cosine similarity is semantic overlap, not correctness. Separate exact-evidence recall@5 checks whether the union of five returned units covers all gold evidence. Main API latency comes from serial Quick100 controls while accuracy uses the full set; the 1M experiment is a stratified 400-question diagnostic. Complete main-generation caps are not consolidated in the text, so equal compute should not be assumed.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Main comparisons at the 128k target

Each row uses 3,000 questions in the same four runtime batches with persistent writeback. Accuracy denominator is all questions; CL Hit is backbone-conditioned closed-loop evidence hit, not fixed-corpus recall comparable across backbones. Context is average answer-selected text, excluding all offline index views and construction cost.

| Backbone / method | Accuracy (%) | CL Hit (%) | Mean context tokens |
|---|---|---|---|
| Gemma2:9b / MemGPT | 60.1 | 62.6 | 2301.9 |
| Gemma2:9b / TSIM | 69.6 | 70.7 | 1060.8 |
| Gemini 2.5 Flash / MemGPT | 74.6 | 62.3 | 2349.6 |
| Gemini 2.5 Flash / TSIM | 80.2 | 67.9 | 1275.3 |
| GPT-4o-mini / Tuned Hybrid-Rerank | 56.2 | 63.5 | 3004.2 |
| GPT-4o-mini / TSIM | 73.8 | 74.2 | 1043.6 |

Source: Tables 2 and 29 · [Paper](https://arxiv.org/pdf/2608.25655v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Exact evidence and system costs

Recall@5 uses all 3,000 questions and checks complete evidence coverage by the union of five units. Co-containment uses only multi-snippet questions; its exact sample count is not given and must not be set to 3,000. Values are 0–1 proportions. Separate cost replay reports TSIM/Standard RAG at 6,281/5,554 vectors, 24.986/4.178 ms ingestion per turn, and 141.093/21.478 ms median retrieval, specific to this implementation/hardware.

| Retrieval unit | All-evidence recall@5 | Multi-snippet co-containment |
|---|---|---|
| Standard RAG chunk | 0.456 | 0.004 |
| Fixed 128-token window | 0.719 | 0.675 |
| Fixed 320-token window | 0.577 | 0.831 |
| TSIM episode | 0.810 | 0.890 |

Source: Tables 21 and 24 · [Paper](https://arxiv.org/pdf/2608.25655v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:result-3:START -->
## Separate sample for the million-token diagnostic

Gemini 2.5 Flash on a stratified 400-question subset at the 1M construction target, not the full 3,000 or the main-table latency sample. Input scale is in tokens, with TSIM showing selected context, excluding full pre-indexing costs.

| Method | Accuracy (%) | 95% Wilson interval (%) | Mean input scale | Serial latency (s) |
|---|---|---|---|---|
| Full Context | 87.2 | [83.6, 90.2] | 1.05M | 23.87 |
| TSIM | 96.5 | [94.2, 97.9] | ~1.3k | 2.16 |

Source: Section 6.4; Figure 5 · [Paper](https://arxiv.org/pdf/2608.25655v1)
<!-- EVIDENCE:result-3:END -->

<!-- EVIDENCE:interpretation:START -->
## What the evidence supports

TSIM has the highest aggregate accuracy on all three backbones. The closest Gemini comparison improves over MemGPT by 5.58 points with paired-bootstrap interval [4.15,6.97]. It does not win every domain: Gemini software is 85.3% for TSIM versus 91.7% for MemGPT, and daily life is 81.3% versus 83.7%. A stronger GPT-4o-mini chunk control combines BM25, BGE reranking, HyDE, RRF, parent windows and MMR, reaching 56.2% versus TSIM’s 73.8%; this is not a one-component causal intervention. Progressive ablation reports 26.2% standard retrieval, 43.4% fixed windows, 55.5% semantic episodes and 74.2% full stack; its final value belongs to a separate run from the main 73.8%.

Exact-evidence diagnostics support episode-based retrieval, but compact answer prompts trade against higher ingestion/retrieval costs. The 1M diagnostic shows that visible evidence does not guarantee correct rule use, without establishing performance on every natural million-token conversation. Provider cache reuse can change economics. LongMemEval’s 71.0% versus 61.2% fixed-chunk result uses a configuration selected on full-set retrieval criteria: it is transductive diagnosis, not a strict unseen-distribution generalization estimate.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source gaps and next test

Counterfactual synthesis plus zero-shot-hardness and oracle-answerability filtering favor local-constraint tasks rather than natural chat prevalence. The 300-item human audit sees short source dialogues, median seven turns and about 136 tokens, not noise-packed histories. Its 296/299 majority correctness and κ=0.895 are not a human 128k retrieval ceiling. Four-choice evaluation excludes open-ended answers, clarification, tool behavior and partial correctness; errors also include reader misuse of recovered rules. Closed-loop writeback changes later memory, so cross-backbone CL Hit differences cannot all be assigned to retrieval.

Next tests should use independent untuned natural conversations, paired no-writeback/shared-writeback controls, matched context budgets for episodes/windows, amortized indexing costs, end-to-end latency and repeated runs. Batch-level rather than only question-level resampling could examine dependence induced by shared closed-loop state.

Length accounting: 128k is a packing target, not each provider’s native token count. The GPT-4o-mini full-context diagnostic reports mean 88,425 tokens there and 29,938 at the nominal 16k point; targets must not be presented as measured inputs. Appendix Table 28 purports to partition outputs into hit/miss × correct/wrong, but several rows neither sum to 100% nor reconstruct accuracy. Gemini TSIM gives 66.5, 1.2, 8.4 and 2.8, totaling 78.9; correct cells total 74.9 rather than 80.2%. This unresolved source-accounting issue prevents precise error attribution from that table.
<!-- EVIDENCE:limitations:END -->
