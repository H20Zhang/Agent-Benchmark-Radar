# LitReview Arena / LitReviewBench / LitJudge

## What it actually measures

This benchmark/evaluator family measures **expert utility of an open-ended literature-review artifact**, not only citation count or a static rubric. Domain experts provide pairwise preferences over coverage, claim support, organization, research recommendations, and overall usefulness, while LitJudge is calibrated against those expert preferences as an automatic evaluator.

## What changed relative to predecessors

Evaluations such as DeepSurveyBench usually rely on fixed rubrics or automated judges and lack large topic-matched expert preference sets. SciArena has competitive comparison but is not specialized for decomposing complete literature reviews into evidence coverage, claim support, and research recommendations. The main measurement advance here is making **which review experts would actually prefer to use** a target, while separately testing how well automatic judges approximate that preference.

## Decisive evidence

Reported non-human systems achieve only a **23.0% decisive overall win rate against human drafts**. A generic judge correlates with expert utility at only **ρ=.467**, while LitJudge improves the correlation to **ρ=.792**. These numbers expose two distinct gaps: current systems remain well below expert-preferred artifacts, and generic automated evaluators are themselves imperfect proxies for expert research utility.

## What the score supports

The results support the claim that an expert-calibrated evaluator better matches expert rankings on the evaluated topics, and that current automated literature-review systems retain substantial headroom under expert utility. They do not isolate an agent architecture as the cause of system differences because token, tool, search, and retrieval budgets are not strictly matched across packaged systems.

## Fair comparison contract

System comparisons should align topic set, available corpus/search APIs, token budget, retrieval rounds, citation policy, and maximum runtime. Evaluator comparisons should align the pair set, expert population, dimension definitions, and tie policy and should report held-out calibration rather than only performance on preference data used to train LitJudge.

## How to use it in research

The benchmark is valuable because it moves deep-research evaluation from “does this look like a survey?” toward **does an expert judge that it covers the right evidence, supports its claims, and yields useful research decisions?** A new agentic-search or report-writing method should ideally report retrieval-evidence quality, final-report expert preference, and the calibration gap between automated judges and experts rather than optimizing only a judge proxy.

## Next discriminating validation

The main gaps are domain-specific norms, living-review updates, citation verification, cost matching, and genuinely held-out judge validation. The highest-leverage question is whether LitJudge's stronger correlation transfers across domains, new topic distributions, and unseen system families instead of primarily fitting the current expert-preference distribution.

<!-- RESEARCH-DECISION:START -->

## Research decision card

### When to use it

Use LitReview Arena to test alignment between automatic literature-review assessment and domain experts. Expert calibration improves relevance, while pairwise wins still depend on generation budgets, sources, and style. They do not score an internal retrieval component in isolation.

### What a concrete task looks like

Illustrative task: experts compare anonymized reviews of the same topic along organization, argument, and support dimensions, then their judgments calibrate an automatic evaluator. Better flow need not imply more complete literature or a more defensible research gap.

### Most discriminating experiment

Validate on topics and experts held out from calibration, controlling report length, source pool, and generation budget. Report citation verification separately from expert preference and test ranking stability across disciplines and evaluators rather than only the calibration set.

### Pair with

[das-bench](das-bench.en.md) · [deepresearch-bench](deepresearch-bench.en.md)

> **How to read scores:** align task / split, model and harness, tools and environment versions, resource budget, stopping and retry rules, and evaluator. Aggregate scores from different protocol cells are system-level evidence first; without a matched intervention or ablation, do not attribute the gap directly to one component.

<!-- RESEARCH-DECISION:END -->

## Genealogy

The work moves deep-research evaluation from static result rubrics toward expert-preference calibration; `map_delta=early_signal`. It becomes a durable evaluator shift only if independent benchmarks repeatedly show systematic divergence between generic LLM judges and expert research utility.

Primary: https://arxiv.org/abs/2608.21374
