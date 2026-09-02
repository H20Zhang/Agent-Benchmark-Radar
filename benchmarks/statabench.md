# StatABench：统计 agent 既要会概念，也要会选择并执行正确统计工具

**中文** | [English](statabench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2606.22977)

## 它在测什么

StatABench 包含 Stat-Closed：404 个 questions、18 个 statistical topics、4 种 formats；另有 198 个 practical tool-use tasks，基于 35-function statistics toolkit；以及 Stat-Open 的 30 个 modeling competitions。它同时测概念判断、统计 procedure/tool selection、execution 与开放建模。

## 相比什么前进了

一般 data-science benchmark 将 statistics 淹没在 coding workflow 中。StatABench 把 statistical reasoning 与工具调用显式分层，可以观察 agent 是“不懂方法”还是“懂但调用/参数错”。

## 分数边界

closed/practical/open scores 支持当前 topic mix、toolkit 与 competitions 下的统计能力；三个 settings 不同，不能压成一个统一模型排名。

## 公平比较条件

锁定 Stat-Closed/Practical/Open track、toolkit version、data split、runtime、model access 与 evaluator。open competitions 还需锁定 compute budget。

## 下一步评测坐标

下一步应加强 assumption checking、uncertainty communication 和 causal/statistical model criticism，而不仅是选对函数。
