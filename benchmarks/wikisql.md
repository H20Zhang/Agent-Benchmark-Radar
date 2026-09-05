# WikiSQL：大规模 executable text-to-SQL 的起点，但还不是复杂数据库推理

**中文** | [English](wikisql.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/1709.00103)

## 它到底测什么

WikiSQL 在 **单张 Wikipedia table** 上评估 natural-language-to-SQL，并可通过真正执行 query 判断结果。原始发布包含 80,654 对人工标注 question–SQL，覆盖 24,241 张 table，SQL grammar 受限且基本不涉及多表 join。

## 相比此前评测多测了什么

WikiSQL 之前的 semantic-parsing dataset 通常规模更小、domain 更窄。它第一次把 execution-grounded text-to-SQL 扩到足以支持神经模型训练/评估的规模；Seq2SQL 还直接利用数据库执行结果，为 SQL 中无序部分提供 reinforcement-learning signal。

## 决定性证据

Seq2SQL 论文报告：相比 attentional seq2seq baseline，execution accuracy 从 35.9% 提升到 59.4%，logical-form accuracy 从 23.4% 提升到 48.3%。这证明 SQL structure 与 execution supervision 都具有实质价值。

## 这个分数能证明什么

WikiSQL 证明的是：模型能否把问题映射成一张已知 table 上的简单 executable query。它对 enterprise data agent 的证明很弱，因为 schema discovery、join、nested query、business semantics、database value 与 workflow planning 基本都不存在。

## 公平比较契约

应固定 official split、table content、SQL grammar、execution engine，以及是否允许 execution-guided decoding；execution accuracy 与 exact logical-form matching 要分开报告，因为语义等价 SQL 可能长得不同。

## 还没有测什么

它没有像 Spider 那样真正测试复杂 unseen multi-table schema generalization，也不覆盖 dirty data、external knowledge、SQL dialect 或 interactive database exploration。

## 下一步最有判别力的验证

今天更适合把 WikiSQL 当作一条 scaling curve 的低阶基线：single table → unseen multi-table schema → large dirty database → enterprise workflow，而不是 frontier endpoint。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合作为可执行自然语言数据库查询的历史参照，不宜作为复杂数据智能体的主要终点。单表查询的正确性与跨表关系、业务口径或端到端分析是不同层级的能力；今天使用它应说明其低阶控制组角色。

### 一个具体任务长什么样

示意任务：问题指定一张表中的筛选条件与聚合目标，系统生成 SQL 并执行。它可以检验条件和值是否映射正确，但无需在多个数据库中发现来源或推断业务关系。

### 最有判别力的实验

固定表、问题切分与执行环境，分别报告逻辑形式和执行结果，并区分是否使用执行反馈。把同一方法放到多表与未见模式任务中，观察优势是否保留，而不是把单表提升直接推广为数据库推理进步。

### 建议搭配

[spider](spider.md) · [bird](bird.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`natural-language database query → executable single-table SQL → cross-domain schema generalization`

WikiSQL 的重要性恰恰在于：后来的 benchmark 可以清楚说明它还漏掉了什么。

## 结论边界

该分数不能单独证明端到端真实场景能力；模型、harness、工具预算和 evaluator 都可能形成混杂因素，跨设置比较必须先控制这些变量。