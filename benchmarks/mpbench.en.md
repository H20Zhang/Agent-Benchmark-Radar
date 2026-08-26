# MPBench

- **Measurement object:** Whether six malicious-content classes enter persistent memory through four write channels and are retrieved by a related query in a later session.
- **Closest predecessor:** LoCoMo and LongMemEval measure benign fidelity; AgentDojo and InjecAgent measure same-session hijacking. MPBench separates writing from later retrieval across sessions.
- **Decisive evidence:** Mean ASR/conditional RSR is 34.25%/17.40% for OpenClaw and 66.67%/64.70% for HERMES; PromptArmor reaches only 67.67% TPR at 1% FPR.
- **Score ceiling:** Scores characterize system-plus-harness exposure to persistent poisoning, not the base model alone.
- **Strongest confounder:** The agents differ in write and retrieval policy, and some channels use static labeled context.
- **Remaining gap:** Multiple backbones, fully executable delivery, natural drift, and benign utility.
- **Genealogy:** It fills the transition from benign memory fidelity to persistent poisoning; `map_delta=splits`.

Primary: https://arxiv.org/abs/2606.04329

