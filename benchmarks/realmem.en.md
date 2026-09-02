# RealMem: memory for evolving long-term projects

[中文](realmem.md) | **English** · [Back to Radar](../README.en.md) · [Benchmark Library](../library/README.en.md)

[Paper](https://arxiv.org/abs/2601.06966) · [ACL 2026](https://aclanthology.org/2026.findings-acl.703/) · [Code](https://github.com/AvatarMemory/RealMemBench)

## What it actually measures

RealMem evaluates memory in **long-term project-oriented interaction**. The agent must track goals, schedules, decisions, evolving project attributes, and dependencies across sessions, then answer natural user queries against the current project state.

## What changed relative to prior evaluation

Casual conversation and task-dialogue memory can treat sessions as collections of personal facts. A project creates a different object: state is jointly produced over time, commitments have deadlines, later decisions supersede earlier ones, and relevance depends on the current project phase. RealMem synthesizes this evolution explicitly.

## Decisive evidence

The benchmark contains more than 2,000 cross-session dialogues across 11 project scenarios. Its generation pipeline combines project-foundation construction, multi-agent dialogue generation, and memory/schedule management so that project state evolves rather than remaining a static fact set. Experiments show current memory systems struggle with dynamic context dependencies and long-term project state.

## What the score supports

RealMem supports claims about retrieval and reasoning over evolving project histories. Because final evaluation remains query answering, it is indirect evidence for whether memory improves actual project execution, scheduling, or artifact delivery.

## Fair comparison contract

Fix project history, time checkpoint, backbone, retrieval budget, schedule visibility, and query evaluator. Evaluate superseded versus still-active facts separately, and prevent later project state from leaking into earlier checkpoints.

## What remains unmeasured

Project success is more than answering questions: agents must create artifacts, negotiate scope, manage permissions, recover from failures, and execute irreversible actions. Those operational loops are largely outside the benchmark.

## Next discriminating validation

Attach executable project tasks to each checkpoint—update a plan, edit an artifact, choose the next action—and score consistency with the evolving project state. That would test whether memory reduces real coordination error rather than only improving QA.

## Genealogy

`casual conversation memory → cross-session project state → persistent work context`

RealMem makes evolving project state a distinct memory object, closer to how workplace agents will actually be used.