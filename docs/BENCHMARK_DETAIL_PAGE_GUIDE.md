# Benchmark Detail Page Guide

Benchmark detail pages are not paper summaries. Their job is to help a researcher decide whether a benchmark can support a claim, how to compare results fairly, and what the benchmark still fails to measure.

Each maintained detail page should answer the following questions. Section titles may vary when a benchmark needs a different emphasis, but the information should remain recoverable.

## Required research content

1. **What does it actually measure?** Define the evaluation object, not only the task name. Include the main scale facts that materially affect interpretation: task count, data scale, modalities, environment, time horizon, or other defining dimensions.
2. **Compared with what?** Name the nearest predecessor or baseline evaluation object and state the real delta in capability, environment, or protocol. More examples alone are not a research delta.
3. **How is it evaluated?** Explain the important tracks, evaluator, execution environment, hidden/public split, tool contract, and budget dimensions. A reader should be able to tell which scores are and are not comparable.
4. **What does a score support?** State the strongest claim the metric can support and, just as importantly, what it cannot establish. Separate system-level evidence from component-level causal claims.
5. **What are the main confounders?** Prioritize the few factors most likely to change the conclusion: backbone, harness, tool interface, retries, context policy, judge, data overlap, environment drift, or participant variance.
6. **What is the fair-comparison contract?** List the protocol variables that must be aligned before placing two results in one leaderboard row or claiming a method improvement.
7. **What remains unmeasured?** Identify missing coordinates that would materially change research conclusions rather than producing an exhaustive wish list.
8. **What is the next discriminating validation?** Propose one experiment that would distinguish the strongest competing explanations for current gains or failures.
9. **Where does it sit in the evolution map?** Give a compact predecessor → benchmark → next-coordinate interpretation without implying unsupported historical lineage.

## Evidence discipline

- Prefer primary sources: paper, official repository, dataset/leaderboard, and challenge documentation.
- Do not call a score “current best” unless the exact track, protocol, source, and verification date are known and the tracked result set is sufficiently complete. Otherwise use “reported result” or “highest verified result currently tracked by Radar.”
- A distance from 100% is not automatically “research headroom.” Distinguish benchmark ceiling, human reference, best verified result, and practically attainable improvement.
- Do not infer a component contribution from a bundled system score without a controlled intervention or ablation.
- When harness, tool access, budget, or evaluator differs, treat the result as a different protocol cell unless the benchmark explicitly defines those differences as comparable.

## Writing style

Start with the research significance, then give the protocol details needed to judge it. Prefer concrete contrasts over generic praise. The page should be useful even to a reader who already read the abstract: it should tell them what the benchmark really licenses them to claim.

Chinese and English pages should remain semantically aligned. Exact sentence-level translation is not required, but neither page should contain a material methodological caveat, protocol condition, or result interpretation absent from the other.
