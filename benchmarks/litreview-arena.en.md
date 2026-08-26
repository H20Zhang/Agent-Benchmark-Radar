# LitReview Arena / LitReviewBench / LitJudge

- **Measurement object:** Open-ended literature reviews judged by domain-expert pairwise preferences over coverage, claim support, structure, research suggestions, and overall utility, plus a calibrated automatic judge.
- **Closest predecessor:** DeepSurveyBench-style static evaluation lacks large topic-matched expert preference data, while SciArena-style battles do not decompose full review quality.
- **Decisive evidence:** Nonhuman systems win only 23.0% of decisive overall comparisons against human drafts; a generic judge reaches ρ=.467 with experts on utility, while LitJudge reaches .792.
- **Score ceiling:** The evidence supports closer expert alignment on this dataset; unmatched token, tool, and search budgets prevent architecture attribution.
- **Strongest confounder:** Proprietary systems have unequal budgets, and the public release omits raw replicate annotations and complete written rationales.
- **Remaining gap:** Field norms, living reviews, citation verification, cost matching, and truly held-out judge validation.
- **Genealogy:** It moves deep-research evaluation from output rubrics toward expert-preference calibration; `map_delta=early_signal`.

Primary: https://arxiv.org/abs/2608.21374

