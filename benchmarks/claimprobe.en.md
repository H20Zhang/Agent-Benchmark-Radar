# ClaimProbe: claim-source faithfulness auditing for Deep Research reports

[中文](claimprobe.md) | **English** · [Back to entry](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)

**One line.** ClaimProbe audits each claim after retrieval for support, correct attribution, uncited support, and necessary-fact coverage, separating writer-side faithfulness from retrieval/search quality.

**Question.** DeepResearch Bench, DAS-Bench, and LitReview Arena cover holistic reports, citation/discourse quality, and expert preference, but aggregate scores can still mix retrieval, writing, and presentation quality.

**Evidence.** In the Enterprise Deep Research fixed-evidence writer intervention, hallucination drops 15.89→5.02, misattribution 18.94→5.43, and necessary fact recall rises 36.83→45.85. Because upstream evidence is held fixed, this supports a writer-side evidence-materialization/attribution effect, not better retrieval or planning.

**Caveat.** The main hallucination judge reaches only Cohen κ=0.484 with humans, support search is limited to a top-20 embedding shortlist, the dynamic-update study covers only five DeepResearch Bench tasks, and holistic RACE gains are small with readability sometimes lower.

**Map.** `early_signal`: adds a distinct `retrieved evidence → written claim → cited source` diagnostic coordinate, but one paper does not change the durable Benchmark Map.

**Links.** [Primary](https://arxiv.org/abs/2608.28643) · [Code](https://github.com/SalesforceAIResearch/claimwriter-deep-research)
