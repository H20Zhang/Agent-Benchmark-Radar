# SCALE-QA

- **Measurement object:** Whether a memory system can reconstruct the causally relevant episode in a flat, mixed-topic long-running thread when a later task decision depends on dormant local constraints, rather than merely retrieving semantically similar chunks.
- **Closest predecessor:** LongMemEval already tests cross-session reasoning, updates, and abstention but preserves timestamped session structure; SCALE-QA removes explicit boundaries and makes identifying the operative episode part of the task.
- **Decisive evidence:** The benchmark contains 3,000 audited questions across 10 domains and 4,346 exact evidence snippets; one deterministic runtime scales from 16K through 128K with a 400-question 1M diagnostic. At 128K, GPT-4o-mini Full Context scores 29.8% despite 100% evidence containment, separating “evidence is visible” from “the right episode is operationally reconstructed.”
- **Score ceiling:** The evidence supports SCALE-QA as a discriminating episode-integrity diagnostic. TSIM's 5.6–17.6 point gains over the strongest corresponding baseline across backends are system-level evidence and do not isolate segmentation, indexing, or routing as the cause.
- **Strongest confounder:** Counterfactual synthetic construction plus deterministic four-way MCQ; answerer choice, retrieval-context budget, and runtime noise construction remain part of system-level comparisons.
- **Remaining gap:** Natural long-running logs, open-ended responses, tool follow-up, and later action. The paper's LongMemEval transfer diagnostic uses transductive configuration selection and therefore is not held-out generalization evidence.
- **Genealogy:** It extends LongMemEval-style cross-session memory into recovering which interleaved episode and constraints actually bind the current task; `map_delta=early_signal`, so one work does not rewrite the durable Benchmark Map.

Primary: https://arxiv.org/abs/2608.25655
Code/data: https://github.com/LordTARN1SHED/SCALE-QA
