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

## 演化位置

`natural-language database query → executable single-table SQL → cross-domain schema generalization`

WikiSQL 的重要性恰恰在于：后来的 benchmark 可以清楚说明它还漏掉了什么。