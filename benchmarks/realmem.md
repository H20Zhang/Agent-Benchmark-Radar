# RealMem：从 casual chat 转向 evolving project state

**中文** | [English](realmem.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.findings-acl.703/) · [代码](https://github.com/AvatarMemory/RealMemBench)

## 它在测什么

RealMem 覆盖 11 个 realistic project scenarios、超过 2,000 段 cross-session dialogues，任务中的 goals、artifacts 与 relevant state 会随项目进展变化。问题不再是日常闲聊事实，而是能否维护跨 session 的 project dependencies 与 evolving objectives。

## 相比什么前进了

LoCoMo 等 benchmark 主要测 conversation memory。RealMem 把长期记忆推向 persistent project state，使“旧目标是否已失效”“某个 artifact 处于什么版本”成为更接近生产协作的 memory 问题。

## 分数边界

natural-user-query performance 支持给定 synthetic trajectory 与 judge 下的 project-state tracking；它仍不能说明真实协作系统中的 permissions、writes 与 external tools 是否可靠，因为 trajectories 由 multi-agent pipeline 生成且 interaction 仍是 dialogue-only。

## 公平比较条件

锁定 trajectory generation、dialogue model、project scenario、history visibility 与 judge。不同 synthetic generator 可能改变 dependency density 与 difficulty。

## 下一步评测坐标

下一步要把 project memory 接到真实文件、代码、calendar/database writes 与权限系统，让 stale state 的操作后果可测。
