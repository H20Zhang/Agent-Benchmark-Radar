# Snapshot Compatibility Audit

- **Measurement object:** Whether a RAG agent's answer changes across growing corpus snapshots beyond its own within-snapshot sampling variance.
- **Closest predecessor:** Stable-RAG and Con-RAG perturb fixed evidence; this work uses nested corpus snapshots as a deployment upgrade and subtracts within-snapshot disagreement.
- **Decisive evidence:** NQ excess churn is 6.438 pp exact and 10.250 pp semantic even though aggregate EM changes by only −1.50 pp; 40 stable flips account for 10.00 pp semantic churn.
- **Score ceiling:** The audit establishes snapshot incompatibility, not that every answer flip is factually harmful.
- **Strongest confounder:** One shard ordering, primarily one generator family, unrecorded temperature/top-p, and a model-based semantic judge.
- **Remaining gap:** Live refresh, multi-step trajectories, causal document attribution, and direct harm measurement.
- **Genealogy:** It adds corpus versioning to the RAG regression contract; `map_delta=reinforces`.

Primary: https://arxiv.org/abs/2608.22856

