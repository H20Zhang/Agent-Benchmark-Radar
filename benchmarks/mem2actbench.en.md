# Mem2ActBench: from remembered facts to grounded tool actions

[中文](mem2actbench.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2601.19935) · [ACL 2026](https://aclanthology.org/2026.acl-long.370/)

## What it actually measures

Mem2ActBench tests whether long-term memory is **proactively converted into tool use**. An agent must decide which tool to call and ground tool parameters in information learned from earlier interactions. The memory dependency is deliberately indirect: the task is not phrased as a request to recall a stored fact.

## What changed relative to prior evaluation

Most memory benchmarks stop at retrieval or answer generation. Tool-use benchmarks usually provide the information needed for the current call inside the immediate prompt. Mem2ActBench couples the two: success requires recovering a previously learned personal/contextual fact and applying it at the correct point in an action schema.

## Decisive evidence

The construction pipeline synthesizes 2,029 multi-turn sessions and 400 memory-dependent tool-use tasks from tool/dialogue sources; human checking finds 91.3% of the tasks strongly dependent on memory. Seven representative memory frameworks are evaluated, and the paper finds that current systems remain weak particularly on active memory utilization and parameter grounding.

## What the score supports

The benchmark supports claims about an end-to-end **memory → tool selection/argument grounding** pipeline. It is stronger than recall accuracy as evidence that stored information is operationally useful. It still does not isolate retrieval from reasoning: a correct memory can be retrieved but mapped to the wrong tool field, and a missed action may come from planning rather than memory storage.

## Fair comparison contract

Keep the tool schema, backbone, available tool set, session history, retrieval budget, and number of action attempts fixed. Report tool-selection and parameter-grounding errors separately when possible. Allowing one system to inspect extra tool documentation or to retry calls changes the action problem.

## What remains unmeasured

The tasks are synthesized around benchmark tool schemas rather than long-running real accounts with permissions, irreversible side effects, and evolving APIs. The protocol focuses on using remembered information, not on whether the memory was written, updated, or deleted correctly over months.

## Next discriminating validation

Introduce oracle-retrieval and oracle-planning controls. If oracle memory barely improves tool success, the bottleneck is action grounding; if it closes most of the gap, retrieval/write policy is the dominant research target.

## Genealogy

`memory QA → memory-conditioned decision → memory-grounded tool action`

Mem2ActBench makes “memory utility” concrete: a remembered fact matters only when it changes the right action.