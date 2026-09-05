# ClaimProbe: claim-source faithfulness auditing for Deep Research reports

[中文](claimprobe.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)

## What it actually measures

ClaimProbe measures **faithfulness in the transformation from retrieved evidence to final report claims**. With the evidence set fixed, it audits each claim for source support, correct attribution, missing citations to available support, and coverage of necessary facts. The protocol therefore separates writer-side evidence materialization and attribution from retrieval/search quality.

## What changed relative to predecessors

DeepResearch Bench, DAS-Bench, and LitReview Arena cover holistic report quality, citation/discourse properties, and expert preference. Their aggregate scores can still compress several failure layers into one number: evidence can be missing, retrieved but omitted, written but misattributed, or faithfully written yet poorly presented. ClaimProbe adds a finer **`retrieved evidence → written claim → cited source`** diagnostic coordinate that is more useful for locating the failing system layer.

## Decisive evidence

In the Enterprise Deep Research **fixed-evidence writer intervention**, upstream evidence is held constant while hallucination drops from **15.89 to 5.02**, misattribution from **18.94 to 5.43**, and necessary-fact recall rises from **36.83 to 45.85**. Because the retrieval set does not change, this evidence more directly supports a writer-side materialization/attribution improvement than an end-to-end score that could be driven by better search or planning.

## What the score supports

ClaimProbe can support the statement that, given the same evidence, one writer or synthesis mechanism hallucinates less, attributes sources more accurately, or materializes more necessary facts. It cannot support the claim that the complete deep-research agent retrieves better evidence. Nor do local faithfulness gains fully determine report utility: holistic RACE gains are relatively small and readability sometimes declines, showing that factual faithfulness and overall usefulness are distinct objectives.

## Fair comparison contract

Writer comparisons should fix the evidence set, claim segmentation, support-search procedure, available citations, writer token budget, prompt, and judge. Giving one writer more relevant evidence and then attributing lower hallucination to the writing mechanism would break the contract. Evaluator comparisons should also report human agreement and support-retrieval recall because judge errors directly enter the benchmark score.

## Evidence strength and limitations

The main hallucination judge reaches only **Cohen κ=0.484** with humans, and support search is limited to a **top-20 embedding shortlist**. The dynamic-update study covers only **five DeepResearch Bench tasks**. The strongest current inference is therefore the relative writer-layer effect under fixed evidence, not the absolute prevalence of every claim-level error across deep research.

## How to use it in research

ClaimProbe is useful as a **failure-layer attribution benchmark** for agentic retrieval and report generation. A cleaner experimental sequence is to fix retrieval while comparing writers, then fix the writer while changing retrieval, and only afterward evaluate end-to-end report utility. This avoids package-level claims such as “the final report improved” that cannot identify whether search, evidence selection, synthesis, or citation grounding caused the gain.

## Next discriminating validation

Two gaps have the highest leverage: improve claim-support evaluation to stronger human agreement and validate shortlist recall; then test on a much larger held-out set whether local faithfulness improvements consistently translate into expert report preference. If they do not, future benchmarks should preserve factual faithfulness and research usefulness as separate coordinates.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use ClaimProbe to distinguish unsupported claims, misattribution, and omissions in research reports, particularly for writer-side improvements under fixed evidence. Failure to find support can arise from generation or from the auditor's source shortlist, requiring separate checks.

### What a concrete task looks like

Illustrative task: a claim is supported by one retrieved source but cites another that does not support it, while a different claim has no support anywhere in the evidence set. Both reduce trust but require different repairs.

### Most discriminating experiment

Compare writers over a fixed evidence set and manually review all sources for a sample of claims labeled unsupported to estimate shortlist misses. Jointly report necessary-fact coverage, support, and readability so writing less or excessive claim fragmentation cannot game faithfulness.

### Pair with

[deepresearch-bench](deepresearch-bench.en.md) · [ragtruth](ragtruth.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

`map_delta=early_signal`. ClaimProbe adds an independent `retrieved evidence → written claim → cited source` layer but one paper does not change the durable Benchmark Map. Its broader implication is that Deep Research evaluation may need to evolve from scoring one final artifact to **layered evaluation of retrieval, materialization, attribution, and utility**.

**Primary:** https://arxiv.org/abs/2608.28643 · **Code:** https://github.com/SalesforceAIResearch/claimwriter-deep-research
