# LongMemEval-V2: memory as compressed experience over massive agent histories

[中文](longmemeval-v2.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2605.12493) · [Project](https://xiaowu0162.github.io/longmemeval-v2/) · [Code](https://github.com/xiaowu0162/LongMemEval-V2)

## What it actually measures

LongMemEval-V2 tests whether a memory system can turn huge collections of **web-agent and enterprise trajectories** into compact evidence useful for later reasoning. It covers static state recall, dynamic state tracking, workflow knowledge, environment-specific gotchas, and premise awareness rather than only conversational facts.

## What changed relative to prior evaluation

LongMemEval V1 scales user-assistant histories and makes update/temporal reasoning explicit. V2 changes both the source and scale of experience: histories can reach 500 trajectories and 115M tokens, and the useful knowledge includes procedures and environment-specific lessons learned through action. Memory must act as an experience compressor, not merely a chat-history retriever.

## Decisive evidence

The benchmark contains 451 manually curated questions across web and enterprise settings and five ability categories. AgentRunbook-C reaches 72.5 average accuracy versus 48.5 for the strongest reported RAG baseline and 69.3 for an off-the-shelf coding-agent memory approach. The coding-agent style retrieval also incurs high latency, making the accuracy–latency frontier part of the result rather than a footnote.

## What the score supports

The benchmark supports claims about extracting reusable knowledge from enormous trajectory histories and highlights that active agentic retrieval can outperform passive RAG at substantial cost. It does not isolate the memory component when agentic retrieval changes search depth, reasoning, or tool usage.

## Fair comparison contract

Fix history snapshot, backbone, maximum evidence returned, retrieval/tool-call budget, and answer evaluator. Report latency, token/tool cost, and evidence volume together with accuracy. Comparing fixed top-k RAG against unconstrained iterative search without accounting for budget answers a different question.

## What remains unmeasured

The final task is still context-gathering QA rather than closed-loop future task completion. Write/update cost for maintaining memory as trajectories arrive, stale procedure handling, and destructive environment change remain underexplored.

## Next discriminating validation

Convert the five knowledge categories into future executable tasks and compare equal-cost passive retrieval, compiled runbooks, and agentic reacquisition. The key systems trade-off is what experience should be retained versus cheaply rediscovered.

## Genealogy

`long chat history → agent trajectory archive → compressed reusable environment knowledge`

V2 makes memory compete directly with reacquisition over histories too large to revisit naively.