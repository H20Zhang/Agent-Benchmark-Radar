# StateMemBench

- **Measurement object:** Whether answers use the currently operative state rather than a superseded state as facts, constraints, and decisions are revised across sessions.
- **Closest predecessor:** LongMemEval / MemoryAgentBench already cover updates; StateMemBench uses symbolic event programs, deterministic replay, and closed-pool grading to isolate state drift more directly from retrieval and generic reasoning failure.
- **Decisive evidence:** 234 multi-session scenarios and 322 probes; the grader separates current, targeted-superseded, and other outcomes. StateMem raises the same-backbone DeepSeek score from 0.205 to 0.363, while a length- and cost-matched control retains a +15–32 point structural gain.
- **Score ceiling:** The score supports current-state maintenance under explicit dependencies and controlled revisions; it is not a general memory-quality measure or direct evidence of long-horizon action benefit in the wild.
- **Strongest confounder:** The benchmark is aligned with state-structured methods; dialogue is model-synthesized, dependencies are explicit, and grading uses a fixed LLM judge.
- **Remaining gap:** Latent relation discovery, real user/environment drift, privacy governance, and whether state tracking improves later closed-loop action.
- **Genealogy:** `early_signal`. It advances update evaluation from “are old and new facts stored?” to “what is the operative state now?” without yet changing the durable map.

Primary: https://arxiv.org/abs/2608.19652
