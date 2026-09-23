# LoCoMo-Conv: retrieving and using memory without an explicit factual query

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-03<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.03467)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](locomo-conv.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2609.03467) · [Code](https://github.com/MiuLab/LoCoMo-Conv) · [Data](https://github.com/MiuLab/LoCoMo-Conv/tree/main/data)

## What it measures

LoCoMo-Conv preserves LoCoMo histories, gold answers, and evidence dia_ids while recasting queries into dialog, implicit, counterfactual, and composed styles. It evaluates retrieval and free-form responses separately. The composed component has 1,069 clusters pairing two source questions. These are rewrites over existing histories, not newly collected natural longitudinal interactions. [Official protocol and data](https://github.com/MiuLab/LoCoMo-Conv/blob/main/README.md)

## Compared with what

Compared with LoCoMo, the intervention changes how the current request is expressed while keeping the history fixed. It tests whether explicit QA was revealing what to retrieve. Distinguish it from constraint-consistency evaluations such as LoCoMo-Plus: retaining source evidence identifiers makes the query-form, evidence-retrieval, and response-quality gaps particularly inspectable.

## Evaluation protocol

Public runners expose top-K, oracle, no-memory, query-rewriting, and CoT controls. The retrieval evaluator maps returned material to dia_ids through turn-text substring matching or metadata provenance for abstractive memories. Composed questions use the union of member evidence. Consequently, evidence recall is not semantic completeness of a returned summary: cross-representation comparisons require equally reliable source attribution. [Retrieval scoring implementation](https://github.com/MiuLab/LoCoMo-Conv/blob/main/retrieval/compute_retrieval_metrics.py)

## Decisive evidence and score boundary

The paper reports retrieval gaps for implicit and composed queries that explicit QA can obscure, and separates strong retrieval from good responses. It also describes silent grounding: memory may improve contextual appropriateness without explicitly stating the gold fact. Gold-fact mention is therefore not a complete conversational-quality metric, and scores from different judges should not be merged into an unconditional ranking. [Paper](https://arxiv.org/abs/2609.03467)

## Confounders and remaining coverage gaps

The strongest confounders are rewriting quality, category filtering, source-ID completeness, and response criteria. A raw-turn versus abstractive-memory recall gap can reflect attribution or information-preservation differences rather than retrieval policy alone. External application actions, long-term permission governance, and continual-learning costs remain unmeasured.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use it for conversational memory beyond explicit QA and for diagnosing why successful retrieval does not translate into response quality.

### What a concrete task looks like

Illustrative task: a user says “plan this weekend as usual” rather than asking for an old preference; the system must infer which history matters without copying the nouns of an explicit QA prompt.

### Most discriminating experiment

Pair explicit and implicit versions of the same source question and history, fixing embeddings, answerer, top-K, and token budget; then supply oracle evidence. Audit source recall, semantic preservation, fact use, and conversational appropriateness separately rather than collapsing all stages into one score.

### Pair with

[locomo](locomo.en.md) · [locomo-plus](locomo-plus.en.md) · [dolphinbench](dolphinbench.en.md)

<!-- RESEARCH-DECISION:END -->

---

Evidence checked: 2026-09-23. This note uses paper metadata and the official protocols, implementations, or dataset descriptions identified above. Structural validation is not factual certification, and experiments were not independently reproduced.
