# InMind：当 personal fact 与 query 语义很远，retrieval 需要 world knowledge bridge

**中文** | [English](inmind.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.24368) · [代码](https://github.com/imlrz/InMind)

## 它在测什么

InMind 有 125 个 expert-verified tasks、覆盖 10 个 life domains。每个 task 都有 direct query 与 indirect query：后者只有先用 world knowledge 理解某个 personal fact 为什么相关，才能触发正确 retrieval，因此 embedding similarity 不再足够。

## 相比什么前进了

普通 memory retrieval 假设 query 与 stored fact 在语义空间接近。InMind 用 paired controls 把 storage failure、backbone knowledge gap、retrieval-routing failure 与 final application failure 区分开，专门测 implicit association retrieval。

## 分数边界

direct/indirect 差距支持“系统在世界知识桥接后是否能找到 target memory”的判断；它不测 update、forget 或 actions。base-model world knowledge 本身是必要变量，因此换 backbone 后绝对分数不能直接归因给 memory retriever。

## 公平比较条件

锁定 base model、embedding/retrieval budget、synthetic personal facts、fixed background trace 与 judge，并分别报告 direct 与 indirect conditions。

## 下一步评测坐标

下一步应让 implicit association 在动态、多事实 memory 中竞争，并验证被召回的关联是否真的改善后续行动而非只答对一个问题。
