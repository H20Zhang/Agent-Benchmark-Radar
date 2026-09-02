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

## 演化位置

`single-table SQL → unseen multi-table schema → enterprise SQL workflow`

Spider 奠定了 cross-schema generalization；后续 benchmark 主要是在把 database 与 workflow 变得更真实。