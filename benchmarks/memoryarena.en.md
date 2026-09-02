# MemoryArena: memory that must improve later action

[中文](memoryarena.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2602.16313) · [Project](https://memoryarena.github.io/) · [Code](https://github.com/ZexueHe/MemoryArena)

## What it actually measures

MemoryArena asks whether an agent can turn earlier interaction experience into **better later decisions**. Its multi-session Memory–Agent–Environment loops contain interdependent subtasks: actions produce feedback, the useful parts of that feedback must be distilled, and later sessions require reusing the distilled experience rather than merely answering questions about a transcript.

## What changed relative to prior evaluation

LoCoMo-style evaluation asks whether past conversational information can be recalled or reasoned over. MemoryArena changes the dependent variable from retrospective answer quality to downstream action quality. It spans web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning, so the relevant memory may be a failed action, a discovered constraint, or an environment-specific strategy rather than a fact that appears verbatim in history.

## Decisive evidence

The paper reports a sharp gap between conventional memory QA and the agentic setting: systems that are close to saturation on LoCoMo still perform poorly when memory must guide multi-session action. The released harness includes long-context, lexical/vector retrieval, graph-based retrieval, and dedicated memory systems, making the failure difficult to explain as one missing retrieval implementation.

## What the score supports

A MemoryArena score is evidence for the **whole experience-to-action loop** under a fixed model, tool interface, environment, and session protocol. It does not by itself show that a particular memory representation, retriever, or consolidation algorithm caused the gain, because planning quality and tool execution remain on the causal path.

## Fair comparison contract

Hold the backbone, environment version, tool interface, session boundaries, action budget, and observation access fixed. Report memory construction/update cost separately from online action cost. A comparison that gives one system richer observations or more retries is measuring a different agent loop, not a cleaner memory component.

## What remains unmeasured

The benchmark still uses bounded benchmark environments rather than months of open-ended deployment. Governance, deletion, privacy boundaries, and cross-user memory are outside the main target. It also does not fully decompose whether a failure came from writing the wrong experience, retrieving the wrong experience, or ignoring correct retrieved experience.

## Next discriminating validation

Add stage-level counterfactuals: oracle-write, oracle-retrieve, and oracle-use variants on the same trajectories. That would turn MemoryArena from a strong system benchmark into a diagnostic benchmark that can say **where** the memory-to-action loop breaks.

## Genealogy

`conversation recall → trajectory memory → experience-conditioned action`

MemoryArena is important because it moves the success criterion from remembering the past to changing future behavior.