# OntologyBench

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-09-08<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.08174)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

## Measurement object

Tests whether dense retrieval satisfies ontology-defined concepts, relations and conjunctive phenotype constraints rather than semantic similarity alone.

## What changed compared with predecessors

Adds structured compatibility targets and ontology-aware diagnostic baselines to text retrieval evaluation.

## Protocol and comparison controls

The release includes checksummed task artifacts, a BM25 baseline and common retrieval evaluators. It distinguishes concept-only from unified training supervision; candidate scoring must be interpreted together with first-stage recall.

## Decisive evidence and score ceiling

The strongest practical contribution is a runnable test of partial versus joint constraint matching. Official provenance also records discrepancies between selected archived outputs and published aggregates; inspect that record before exact reproduction.

## Strongest confounders and limitations

Task-wise directed-pair separation is not entity-disjoint or inverse-relation-disjoint evaluation. Report the split explicitly; do not call these results inductive generalization or medical performance.

## Coverage gap and next experiment

Shared ontology vocabulary and allowed cross-task overlap do not establish unseen-entity induction or clinical diagnostic validity.

Add entity- and inverse-edge-disjoint controls and an oracle candidate pool. Separate missing candidates from ranking failures and unsatisfied conjunctions.

## Genealogy and use

[BEIR](beir.en.md) · [BRIGHT](bright.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.08174) · [Reviewed full text](https://arxiv.org/html/2609.08174v1)

[code](https://github.com/cindyzhangxy/OntologyBench)

[data](https://huggingface.co/datasets/cxyzhang/OntologyBench)

First public event: **2026-09-08**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](ontologybench.md) · [Complete index](../library/README.en.md)
