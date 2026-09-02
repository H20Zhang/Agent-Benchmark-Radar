# DreamBench-SWE

## What it actually measures

DreamBench-SWE measures **memory hygiene in multi-session software engineering**. A later coding task must decide whether evidence retained from an earlier session—evidence that cannot be reconstructed from the current repository—is still current, scoped, authorized/relevant, and therefore should be used, or whether it should now be suppressed. Hidden executable oracles score the resulting code changes, so memory affects real action rather than only QA.

## What changed relative to predecessors

MemoryArena and WorldMemArena already connect memory to later action, while SWE-bench supplies executable software tasks. DreamBench-SWE crosses the two into controlled **repository-continuation memory traps**: the protocol controls what was revealed earlier, what can be re-inferred from the current repository, and which retained evidence has become invalid in the successor task. The later Agent Memory Bench for coding agents provides a complementary real-repository comparison.

## Decisive evidence

In v2, each complete condition contains **60 traps × 3 seeds = 180 S3 cells**. In the successor, B0 scores **21/180**, B5 **82/180**, the typed-plus-raw reference probe **83/180**, and one pinned Mem0 literal-storage configuration **97/180**. All available memory-versus-B0 comparisons reject the null after Holm correction. The key conclusion is that the benchmark has substantial power to distinguish conditions that retain otherwise unavailable historical evidence from the no-memory baseline.

## What the score supports

The results support DreamBench-SWE as a discriminating executable memory-profile benchmark and show that some tasks become much more solvable when cross-session evidence is available. They do not establish mechanism superiority or equivalence among B5, typed-plus-raw, Mem0, or other memory-bearing conditions, and they do not directly generalize to coding products because memory configuration and coding harness jointly form the treatment.

## Fair comparison contract

Wake/judge/model stack, coding harness, tool permissions, filesystem/network access, trap set, seed, memory-injection format, and oracle should be aligned. Most importantly, distinguish **memory availability** from **memory-policy quality**: outperforming B0 when a condition simply receives more otherwise-unavailable evidence shows that history is useful, not that a particular memory architecture is superior.

## How to use it in research

The benchmark is useful for three separate coding-agent-memory claims: whether retained information changes future action when needed, whether invalid old information is suppressed, and whether scope/authorization metadata changes behavior correctly. Researchers should report use-when-needed, suppress-when-invalid, and final executable success separately rather than compressing all behavior into one aggregate number.

## Next discriminating validation

The main gaps are production-scale real repositories, cross-model and cross-harness transfer, and limited B0 headroom in C9/C10, which prevents broad rejection/abstention claims. The highest-value next study would transplant the same memory-hygiene protocol into real repository continuations and compare coding harnesses under matched evidence access, separating benchmark-trap effects from harness-specific effects.

## Genealogy

The benchmark decomposes “does past experience help later action?” into whether retained evidence remains **current, scoped, authorized/relevant, and correctly suppressed when it should not be used**; `map_delta=early_signal`. It is an important action-grounded lifecycle coordinate beyond memory QA, but still needs independent external validation.

Primary: https://arxiv.org/abs/2608.20664
