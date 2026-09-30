# LIT-RAGBench: remove the retriever and test whether the generator can use RAG context

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2025-10-22<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2603.06198)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](lit-ragbench.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

Read All Sections 1–7, dataset example, results and limitations; appendices inspected: No separate appendix; prompts deferred to repository and not independently inspected; visual checks: Figure 3 and Table 2 checked on rendered page 7. Not performed: No rerun, prompt/code audit or overall-score aggregation reconciliation

[arXiv 2603.06198v1 — arXiv v1, 2026-03-06; PDF marked LREC 2026](https://arxiv.org/pdf/2603.06198v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Like RGB, LIT-RAGBench controls supplied evidence, adding fictional content, logic, tables and deletion variants. Removing the retriever helps localize reader errors but cannot rank complete search systems.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

The benchmark isolates the generator rather than the retriever. Three native Japanese authors design fictional company, product and person scenarios, aided by GPT-5 and independently reviewed by two contributors. Fifty-four main tasks cover integration, reasoning, logic and tables; forty-two combine two capabilities and twelve one. Removing gold evidence creates fifty-four insufficient-evidence tasks, supplemented by three conflicting-evidence and three incomplete-chunk tasks, for 114 per language. English is GPT-5-translated with human curation described in the abstract. Models receive shuffled relevant/distractor chunks directly, at least eight per task and roughly 512 tokens each, and must answer from context or abstain when evidence is insufficient.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

GPT-4.1-2025-04-14 assigns binary semantic-consistency judgments against reference answers, without a reported dataset-specific human-agreement test. Selected versions are GPT-5-2025-08-07, o4-mini-2025-04-16 and Claude-Sonnet-4-2025-05-14. Configurable models use temperature zero and top_p=1; reasoning models use maximum generation length. Categories overlap, so compound tasks contribute to both. Main averages the four main categories; abstention contains sixty tasks and over-abstention uses fifty-four answerable main tasks. The overall aggregation formula does not fully agree with Figure 3, so the selected evidence emphasizes identifiable category scores.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## Correct abstention versus over-abstention

All values use a 0–1 scale. Main averages four overlapping categories across fifty-four main tasks; abstention uses sixty tasks and over-abstention fifty-four, with GPT-4.1 judging.

| English model | Main mean | Abstention accuracy | Over-abstention |
|---|---|---|---|
| Claude-Sonnet-4 | 0.65 | 0.967 | 0.37 |
| o4-mini | 0.839 | 0.9 | 0.074 |
| GPT-5 | 0.828 | 0.933 | 0.093 |

Source: Tables 2–3 · [Paper](https://arxiv.org/pdf/2603.06198v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:result-2:START -->
## Language differences for the same model

On a 0–1 scale, with 114 tasks per language; reasoning/table scores use their overlapping category subsets and over-abstention fifty-four tasks. English translates the same scenarios rather than an independently sampled benchmark.

| Claude-Sonnet-4 language | Reasoning accuracy | Table accuracy | Over-abstention |
|---|---|---|---|
| Japanese | 0.783 | 0.677 | 0.148 |
| English | 0.565 | 0.516 | 0.37 |

Source: Tables 2–3 · [Paper](https://arxiv.org/pdf/2603.06198v1)
<!-- EVIDENCE:result-2:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Abstention should be read together with refusal on answerable tasks. Claude-Sonnet-4 reaches English abstention accuracy 0.967, but over-abstains on 0.370 of the fifty-four main tasks and has Main mean 0.650. The corresponding o4-mini values are 0.900, 0.074 and 0.839. Caution and usefulness therefore differ, and language-specific results matter. This benchmark does not evaluate ranking, tool choice or autonomous multi-turn search; agentic RAG is a proposed extension, not an established capability here.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

The sample is small and imbalanced, and insufficient-evidence variants share their underlying fifty-four scenarios rather than creating 114 independent situations. Fictional entities reduce memorization but do not remove language or synthesis-style bias. Overlapping capability labels prevent pure single-factor category comparisons, and shuffling does not prove that position effects disappear. Next, publish reproducible aggregation rules, repeat over document-order seeds, audit the judge with humans, expand contradictory/incomplete-chunk cases, and compare generators on identical retrieval results.

Section 5.2 defines overall as the mean of five category accuracies, but GPT-5 Japanese Table 2 values average to about 0.862, not Figure 3’s 0.872. Do not silently assign macro-average semantics to that figure. Section 5.3 describes Qwen Instruct/Thinking best open-weight values as 0.859/0.821, whereas Figure 3 shows Thinking 0.840 Japanese and 0.859 English; 0.821 is its Japanese Main mean in Table 2. Abstention aspect percentages 34.6/1.9/1.9 are not percentages of 114 unique questions; category/aspect incidences differ because main tasks can overlap. Only three contradictory and three incomplete-chunk questions per language support those individual subaspect claims.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [rgb](rgb.en.md) · [t2-ragbench](t2-ragbench.en.md)
