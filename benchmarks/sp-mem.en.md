# SP-Mem Privacy-Aware Memory Benchmark: Agent Memory / lifecycle privacy

[中文](sp-mem.md) | **English** · [Back to the entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.16551) · [Code and data](https://github.com/Jensassss/SP-Mem)

Places memory utility, consent, authorization, exact-value exposure, and cost in one protocol.

## What It Follows

Earlier evaluation usually compressed this problem into a shorter final score or a single proxy. This object turns its predecessor critique into an explicit capability × environment × protocol delta and retains an executable or auditable artifact.

## How It Is Evaluated

**Question:** Can personalized memory be used only when necessary and authorized without exposing private values?

**Measurement object:** Privacy-aware memory benchmark that jointly measures response quality, personalization, consent handling, exact-value exposure, and cost.

**Scale and protocol:** 1,000 synthetic profiles, 5,400 queries, four domains, and 376 subtasks. The protocol includes matched-privacy-preference-modes, pairwise-quality, exact-value-leakage, cost-accounting.

## What a Score Can Support

Matched modes over 1,000 profiles, 5,400 queries, and four domains score response quality, authorization requests, and exact-value exposure together. It supports system-level evidence under this environment, harness, model/tool, and resource configuration; unmatched variables prevent attribution to one component.

## Strongest Confounder

Explicit consent labels and an exact-string leakage proxy omit inference, re-identification, and adversarial multi-turn disclosure. The load-bearing confounders are synthetic-consent-labels, benchmark-system-codesign, exact-string-leakage-proxy.

## What It Still Does Not Measure

Explicit consent labels and exact-string leakage miss inference, re-identification, and adversarial multi-turn disclosure.

## Where It Fits in the Map

`map_delta=early_signal`. One paper is only a signal; a durable direction needs independent records bound to the same canonical direction key.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use SP-Mem to trade off privacy authorization and personalization within one experiment. Absence of exact-value repetition does not rule out inference. Treat it as a diagnostic of consent handling and direct disclosure, not a complete privacy guarantee.

### What a concrete task looks like

Illustrative task: a store contains an ordinary preference and information requiring authorization, but a service request needs only part of it. Appropriate behavior may use permitted information, request consent, or avoid disclosure rather than always answer or always refuse.

### Most discriminating experiment

Switch consent state for matched profiles while keeping service queries fixed, and jointly report utility and disclosure risk. Add semantic-paraphrase checks beyond exact-string leakage. Track unnecessary permission requests so privacy gains obtained through excessive friction remain visible.

### Pair with

[gatemem](gatemem.en.md) · [permemsafe](permemsafe.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->
