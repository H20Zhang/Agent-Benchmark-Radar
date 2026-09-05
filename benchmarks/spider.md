# Spider：让 text-to-SQL 真正泛化到 unseen database schema

**中文** | [English](spider.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/1809.08887) · [项目页](https://yale-lily.github.io/spider)

## 它到底测什么

Spider 测 **complex cross-domain text-to-SQL generalization**：10,181 个问题、5,693 条 unique SQL、200 个 multi-table database、138 个 domain，而且 train/test 使用不同 database，因此系统必须面对 unseen schema。

## 相比此前评测多测了什么

WikiSQL 基本是一张 table + 受限 grammar；Spider 把 join、nested query、set operation、aggregation 与新 schema 放到中心。研究问题从“是否记住 query pattern”变成“能不能把自然语言对齐到陌生 relational structure”。

## 决定性证据

发布时最强模型在 database split 上 exact match 只有 12.4%。低分不只是规模大，因为 train/test 在 SQL program 与 database schema 两个维度都不同，刻意阻断 template reuse。

## 这个分数能证明什么

Spider 对 static、相对紧凑 database 下的 schema generalization 与 complex SQL generation 证据很强；高分却不能证明系统能处理 dirty value、超大 catalog、dialect documentation、business-rule drift 或 multi-query workflow。

## 公平比较契约

应固定 database split、schema serialization、value-access policy、SQL evaluator 与 model/tool budget，并区分 exact match / execution evaluation；任何额外 schema-linking retrieval 或 metadata 都应披露。

## 还没有测什么

schema 相比 enterprise warehouse 仍小，database content 也不是主要难点；每个任务都有比较明确的 query intent。真实 analyst 还需要搜 metadata、澄清 business term，甚至判断“这里根本不应该执行 query”。

## 下一步最有判别力的验证

把 Spider 当 schema-generalization rung，同一 agent 继续跑 BIRD、Spider 2.0 与 reliability-oriented warehouse task。不同 rung 上的退化曲线比单个 Spider leaderboard 数字更有信息量。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合检验跨数据库模式的 SQL 泛化，但静态问题到查询的映射并不覆盖完整企业分析。必须区分生成 SQL 与真正理解业务语义；形式匹配与结果等价也不是同一个正确性定义。

### 一个具体任务长什么样

示意任务：用户的问题需要连接几张表，系统在未见数据库模式中判断键关系并生成嵌套或聚合查询。即使 SQL 能执行，连接方向、聚合范围或重复行处理仍可能使答案错误。

### 最有判别力的实验

保持数据库切分，比较相同骨干下的模式链接与查询生成策略，并用执行等价检查补充形式匹配。加入正确相关表给定条件，区分模式发现与查询构造；不要使用测试模式调参后仍称零样本泛化。

### 建议搭配

[bird](bird.md) · [spider-2](spider-2.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-table SQL → unseen multi-table schema → enterprise SQL workflow`

Spider 奠定了 cross-schema generalization；后续 benchmark 主要是在把 database 与 workflow 变得更真实。