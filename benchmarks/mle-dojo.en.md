# MLE-Dojo

- **Measurement object:** The full trajectory of inspecting tasks, executing code, observing errors and HumanRank feedback, revising solutions, and submitting results in Gym-style MLE environments.
- **Closest predecessor:** MLE-bench primarily grades terminal submissions; MLE-Dojo turns 200+ tasks into interactive training/evaluation environments with a 150/50 split.
- **Decisive evidence:** A shared harness records HumanRank, stepwise progress, errors, and action breakdowns across four task families, making failure locations observable.
- **Score ceiling:** Final performance includes true-score feedback, scaffold, a 15-step budget, and best-of-two selection, so it is not directly comparable to score-hidden MLE-bench.
- **Strongest confounder:** Agents can repeatedly adapt to true scores, inviting feedback overfitting, and many evaluation tasks inherit public predecessor suites.
- **Remaining gap:** Problem definition, data acquisition, metric design, research-repository repair, and novelty.
- **Genealogy:** It advances MLE-bench's terminal contract into trainable interaction trajectories; `map_delta=reinforces`.

Primary: https://arxiv.org/abs/2505.07782

