# MemEye：先证明问题真的需要 visual memory

**中文** | [English](memeye.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.15128) · [代码](https://github.com/MinghoKwok/MemEye)

## 它在测什么

MemEye 发布 371 个 mirrored multiple-choice/open-ended questions，覆盖 8 个 life-scenario tasks，并按 visual-evidence granularity 与 reasoning depth 组织。关键协议包含 visual-necessity ablation：移除图片后如果仍能答，问题就不是强 visual-memory evidence。

## 相比什么前进了

许多 multimodal memory dataset 实际可以依赖文本 caption、常识或 question shortcut。MemEye 把“视觉证据是否不可替代”变成验证步骤，从而更可信地测 fine-grained visual retention、temporal state tracking 与 evolutionary synthesis。

## 分数边界

MCQ 与 open-ended judge 分数支持在构造场景中使用必要 visual evidence 的能力；它们不说明真实多模态 agent 的长期 action utility。judge、multimodal backbone 与 scenario construction 仍是重要变量。

## 公平比较条件

锁定 mirrored question set、visual-necessity filter、backbone、image preprocessing 与 judge，并分别报告 MCQ/open-ended，不应互相混排。

## 下一步评测坐标

下一步要让被保留的 visual evidence 决定之后的操作，并检查跨 session 图像状态变化与冲突更新。
