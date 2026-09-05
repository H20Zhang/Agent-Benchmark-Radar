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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合把统计知识、工具调用和完整建模报告放在同一评测设计中。闭合题和开放报告的证据强度不同；漂亮报告不保证统计方法正确，工具名称正确也不保证参数和适用前提正确。

### 一个具体任务长什么样

示意任务：系统根据数据和研究问题选择统计方法、执行工具并解释结果。若分布或独立性假设不成立，软件仍可能返回显著结果，因此应审查方法适用性而不只检查调用成功。

### 最有判别力的实验

分开报告知识题、工具参数和开放报告，固定工具集及评价器。增加违反统计前提的对照数据，检查系统是否改用合适方法或保留判断；开放报告还应进行独立方法学复核。

### 建议搭配

[causalds](causalds.md) · [dare-bench](dare-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
