# MemoryArena：直接测 memory 能否改善未来 action

**中文** | [English](memoryarena.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.16313) · [代码](https://github.com/ZexueHe/MemoryArena)

## 它在测什么

MemoryArena 把任务拆成相互依赖的多 session subtasks，早期 action 与 feedback 需要被压缩成 memory，并在后续 shopping、search、travel、math、physics 等任务中真正指导决策。evaluation endpoint 是后续 task success，而不是“能否回答过去发生了什么”。

## 相比什么前进了

传统 memory benchmarks 常把 memorization 与 acting 分开。MemoryArena 把 `Memory-Agent-Environment` loop 闭起来，使 experience distillation、preference planning、progressive search 等能力只有在之后行动更好时才体现价值。

## 分数边界

更高 task success 支持“在该 agent/environment/harness 下，记住过去经验提高了未来任务表现”；它仍不能单独定位 memory write、retrieval 或 planning 哪一层起作用。不同 retry budget、tool version 与 agent model 会改变系统级结果。

## 公平比较条件

锁定 agent backbone、environment snapshot、tool interface、session dependency 与 memory integration。若 baseline 没有相同工具或 retry budget，就不能把差值归因给 memory。

## 下一步评测坐标

下一步需要更长寿命、不可逆 actions、权限与恢复，让 stale/incorrect memory 的长期代价也可测。
