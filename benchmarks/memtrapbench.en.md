# MemTrapBench

- **Measurement object:** Whether an agent can decide if faithfully stored, semantically relevant history should influence current reasoning rather than reusing it mechanically.
- **Closest predecessor:** LoCoMo / LongMemEval-style evaluation asks whether information can be recalled; MemTrapBench moves the failure coordinate to whether relevant memory should be used.
- **Decisive evidence:** It pairs the same current task under memory and no-memory conditions across 1,050 multi-turn instances spanning reasoning fixation and belief distortion. The paper reports that every tested memory strategy underperforms no memory, with the largest drop exceeding 10 percentage points.
- **Score ceiling:** The result supports measurable harm from relevant-but-invalid history under deliberately constructed context shifts; it does not support the claim that long-term memory is harmful on average.
- **Strongest confounder:** Final questions are intentionally solvable without history, so the no-memory condition avoids the planted prior by construction; synthetic dialogue, judging, and framework × backbone interactions affect magnitude.
- **Remaining gap:** Natural-workload prevalence of harmful reuse and autonomous applicability judgments in open environments.
- **Genealogy:** `early_signal`. It independently supports a memory-validity-before-use direction alongside staleness/update benchmarks, but one work does not rewrite the durable Benchmark Map.

Primary: https://arxiv.org/abs/2608.20202
