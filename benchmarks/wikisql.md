# WikiSQL：text-to-SQL 的早期可执行锚点，但只覆盖单表查询

**中文** | [English](wikisql.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

## 它在测什么

WikiSQL 包含 80,654 个 natural-language/SQL examples，覆盖 24,241 张 Wikipedia tables。核心 contract 是把问题翻译成可执行 SQL，并用 execution result 判断正确性；query 主要是单表 selection、filter 与 aggregation。

## 相比什么前进了

早期 semantic parsing 常用小型 domain-specific datasets。WikiSQL 把 text-to-SQL 扩到大规模、跨表 schema 的训练/测试环境，并推动 execution accuracy 成为自然语言数据库接口的标准指标之一。

## 分数边界

高 execution accuracy 支持单表 schema grounding 与 SQL generation；它不支持多表 join、复杂业务语义、数据库探索或 agentic analysis。现代模型在 WikiSQL 上接近饱和，也不能推出真实 Data Agent 已解决。

## 公平比较条件

锁定 split、schema serialization、execution engine、value access 与 decoding constraints。使用额外 schema/value hints 的系统应和纯 text-to-SQL 分开。

## 下一步评测坐标

Spider 将问题推进到 unseen multi-table databases；更进一步的 Data Agent benchmark 还需要跨库、非结构化数据、分析过程与业务正确性。
