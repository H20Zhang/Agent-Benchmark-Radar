# MUSES / CiteRoots

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2026-08-31<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2609.00313)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

## Measurement object

Tests prospective literature retrieval from an author’s prior work, separating later citations, unfamiliar sources, rhetorical roots and author-endorsed inspiration.

## What changed compared with predecessors

Makes future-use retrieval and the distinction between citation role and actual author endorsement explicit, instead of treating citation as a single relevance label.

## Protocol and comparison controls

CiteNext, CiteNew and CiteNew-Isolated progressively exclude familiar sources. CiteRoots adds rhetorical and author-endorsed targets. Author history precedes the focal boundary; the latter labels are still collected retrospectively.

## Decisive evidence and score ceiling

A lean SPECTER2 multi-centroid baseline is strongest among the reported method classes. The author-endorsed retrieval-evaluable subset is much smaller than all collected pairs, so tier comparisons also change gold-label density and cohort.

## Strongest confounders and limitations

Agreement with citation rhetoric is not agreement with author-endorsed inspiration. Avoid causal claims about creativity from retrieval scores. Release claims are present in the paper, but a specific downloadable package was not independently verified.

## Coverage gap and next experiment

Time-safe retrieval inputs do not make retrospective endorsement labels prospective experimental evidence of scientific impact.

Keep the multi-centroid baseline, match cohorts and positive-label counts, and blind the endorsement audit. Evaluate whether retrieved unfamiliar work changes a later research decision, rather than only recovering retrospective labels.

## Genealogy and use

[MAPLE](maple.en.md) · [ScholarQuest](scholarquest.en.md)

This entry is an `early_signal`: acceptance of a useful evaluation object does not promote one paper into a durable field-map claim.

## Primary sources and version

[Paper](https://arxiv.org/abs/2609.00313) · [Reviewed full text](https://arxiv.org/html/2609.00313v1)

First public event: **2026-08-31**. Reviewed: **2026-09-17**. Source release and Radar acceptance are separate events.

[中文](muses-citeroots.md) · [Complete index](../library/README.en.md)
