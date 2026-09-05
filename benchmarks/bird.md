# BIRD：让 text-to-SQL 真正面对大型、脏的 database content

**中文** | [English](bird.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2305.03111) · [项目页](https://bird-bench.github.io/)

## 它到底测什么

BIRD 把 **large database content、external knowledge、dirty value 与 query efficiency** 放进 text-to-SQL。数据有 12,751 对 question–SQL、95 个 database，总计 33.4 GB，覆盖 37 个专业领域。

## 相比此前评测多测了什么

Spider 的主难点是 unseen schema，但弱化了 database content。BIRD 加入 value grounding：问题里的表达可能和数据库值不直接匹配，数据可能有噪声，需要 external knowledge 桥接，而且两条都正确的 SQL 也可能有完全不同 execution cost。

## 决定性证据

原论文报告 test 上 ChatGPT + CoT 在有 external knowledge 时 execution accuracy 为 40.08%，而 human performance 为 92.96%。它还显式分析 SQL efficiency，不再把所有“能跑对”的 SQL 当成等价。

## 这个分数能证明什么

BIRD 对现实 database-value comprehension + SQL generation 证据更强，但仍不能证明 enterprise-agent competence：任务一开始已经知道 database，不要求跨系统发现、metadata search 或 multi-step workflow execution。

## 公平比较契约

应固定 database snapshot、external-knowledge access、schema/value retrieval policy、SQL engine、model 与 execution budget，并把 execution accuracy 与 efficiency 分开报告。value retrieval 本身就是被测能力，不能偷偷换成 oracle match。

## 还没有测什么

business semantics、permission、schema drift、多数据库系统、write operation 和 clarification 都不在主 protocol。database 很大也不等于 enterprise catalog 很复杂。

## 下一步最有判别力的验证

让同一套 BIRD-optimized schema/value retrieval 不改配置地迁移到 Spider 2.0 与 LiveSQLBench，检查 value grounding 是通用能力还是 benchmark-specific engineering。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究数据库值、脏数据与外部知识对 SQL 正确性的影响。查询效率应在结果正确的前提下解释；更快执行一条语义错误的查询，不构成数据库问答系统的有效改进。

### 一个具体任务长什么样

示意任务：问题中的业务描述与数据库字段值不直接一致，系统需要查看数据并使用给定知识确定筛选和连接条件。只读模式定义可能无法处理缩写、缺失值或编码差异。

### 最有判别力的实验

固定外部知识、数据库内容与执行预算，比较只看模式、允许值检索和正确值给定。对正确查询单独测运行代价，并复核金标查询争议，避免把标注问题或缓存差异算作方法能力。

### 建议搭配

[spider](spider.md) · [livesqlbench](livesqlbench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`unseen schema → database-value grounding → enterprise metadata/workflow reasoning`

BIRD 是 text-to-SQL 从纯 semantic parsing 开始变成 data retrieval problem 的关键一步。