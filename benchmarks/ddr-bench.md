# DDR-Bench：data agent 能不能自己决定“什么值得查”

**中文** | [English](ddr-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.02039) · [代码](https://github.com/thinkwee/DDR_Bench)

## 它到底测什么

DDR-Bench 测 **investigatory intelligence**：agent 拿到 data/entity context，但没有预定义 analytical question，需要自己设 goal、探索并发现可验证 insight。这和用户已经告诉你“请做什么分析”的 executional intelligence 不同。

## 相比此前评测多测了什么

大多数 data-agent benchmark 都从 well-formed task 开始，而真实 analyst 经常从“这里到底发生了什么？”开始。DDR 把 problem formulation 放进 agent loop，并用 checklist-based evaluation 让 open-ended discovery 仍有部分可验证 ground truth。

## 决定性证据

benchmark 覆盖 healthcare record、SEC 10-K/XBRL financial data 与 behavioral data 等真实 domain。论文发现 frontier model 已出现一定 autonomous exploration 能力，但 long-horizon exploration 仍困难，而且表现不只由 scaffold 大小或模型规模决定，还依赖 agent 本身的探索策略。

## 这个分数能证明什么

DDR-Bench 能支持 checklist 范围内 autonomous exploration 的判断，但不能等价于真正 novel discovery：任何 checklist 都预先定义了一组期待发现，open-ended credit 也会受到 evaluator/judge 影响。

## 公平比较契约

应固定 data snapshot、starting metadata、toolset、model、exploration budget 与 evaluator。不能给一边额外 candidate goal/schema interpretation，并要同时报告 insight coverage、成本和 exploration depth。

## 还没有测什么

business value、causal validity、checklist 外 novelty 与 stakeholder relevance 没有被完整测量；真实 investigation 还需要交互 clarification 和“证据什么时候已经够了”的 stopping judgment。

## 下一步最有判别力的验证

混合 planted verifiable insight 与真正 unlabeled dataset，再由 blinded domain expert 评 novelty。关键是区分 agent 会不会寻找 important unknown，而不是只会找回 benchmark 作者预埋的 checklist item。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究只给目标实体和数据元信息时，系统是否知道什么值得调查。它比回答指定查询更接近自主研究，但检查清单只能代表部分可验证发现；更多文字和更多工具调用都不等于更有价值的洞察。

### 一个具体任务长什么样

示意任务：系统拿到一个实体后自主建立假设、查询相关数据、检验异常并形成报告。何时停止也是任务的一部分；找到一个看似异常的数值后，应继续验证而不是立即编写结论。

### 最有判别力的实验

在相同实体与预算下比较自主目标设定和人工研究问题给定，分别统计已验证发现与无支持主张。固定终止规则或单列自终止成本，并复核检查器漏掉的有效发现，避免只优化预设清单。

### 建议搭配

[insightbench](insightbench.md) · [dataclawbench](dataclawbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`answer a specified query → choose analytical subgoals → autonomous data investigation`

它把 agency 从执行阶段前移到了“决定要分析什么”。