# MLE-bench

- **Measurement object:** Whether an agent can start from competition instructions and data, iterate experiments offline, and submit predictions scored against reconstructed tests and historical private-leaderboard medal thresholds.
- **Closest predecessor:** MLAgentBench has 13 often baseline-seeded tasks; MLE-bench expands to 75 from-scratch competitions and a human-relative medal contract.
- **Decisive evidence:** The same GPT-4o scores 0.8%, 4.4%, and 8.7% Any Medal under MLAB, OpenHands, and AIDE scaffolds; pass@6 also substantially exceeds pass@1.
- **Score ceiling:** Headline scores measure model+scaffold+retry+resources, not pure base-model MLE ability.
- **Strongest confounder:** Scaffold, retries, runtime, hardware, tools, and prompt assistance are load-bearing; the official leaderboard was later paused over fairness and version issues.
- **Remaining gap:** Problem formulation, dataset/metric design, messy research repositories, novelty, and human collaboration.
- **Genealogy:** It fills the autonomous ML-engineering branch: MLAgentBench→MLE-bench→MLE-Dojo→DeltaML/AI4AI; `map_delta=splits`.

Primary: https://arxiv.org/abs/2410.07095

