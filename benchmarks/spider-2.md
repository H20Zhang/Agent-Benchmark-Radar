# Spider 2.0：enterprise text-to-SQL 已经变成 agent workflow

**中文** | [English](spider-2.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2411.07763) · [项目页](https://spider2-sql.github.io/)

## 它到底测什么

Spider 2.0 测 **真实 enterprise text-to-SQL workflow**，而不是一次 query generation。632 个任务来自真实应用数据库，常有 1,000+ column，并使用 BigQuery、Snowflake 等 cloud system；完成任务可能要搜 metadata、查 dialect documentation、读 project code、写多个 query，完整 workflow 甚至超过 100 行 SQL。

## 相比此前评测多测了什么

Spider 1.0 测 unseen schema generalization，BIRD 加入 realistic database value；Spider 2.0 进一步把“工作单位”本身改掉：agent 必须在大型数据环境里导航并构造 multi-step SQL workflow，已经更像 data engineering / analytics，而不是一次 semantic parsing prediction。

## 决定性证据

原始评估中，基于 o1-preview 的 code agent 在 Spider 2.0 上只有 17.0% success；同一框架在 Spider 1.0 为 91.2%，BIRD 为 73.0%。这个断崖直接说明：旧 benchmark 的高分没有迁移到 enterprise workflow complexity。

## 这个分数能证明什么

Spider 2.0 支持其环境下 enterprise SQL workflow 的 end-to-end competence，但不能把失败单独归因给 SQL reasoning；metadata retrieval、long-context management、dialect knowledge、code navigation 和 agent scaffold 都在因果链上。

## 公平比较契约

应 pin database/cloud snapshot、SQL dialect、metadata/codebase access、agent harness、model、execution/retry budget 与 evaluator。给一边预选 relevant table，和让另一边自己发现，已经不是同一道题。

## 还没有测什么

business definition、stakeholder ambiguity、governance、permission、production write 与 persistent maintenance 仍只覆盖一部分；真实 warehouse 还会持续变化，而不是一次 benchmark run 内冻结。

## 下一步最有判别力的验证

通过 oracle intervention 把 performance 拆成 metadata discovery、semantic/schema resolution、workflow planning、query execution、repair，判断 17% 的主要瓶颈到底是 retrieval/context 还是 SQL/program synthesis。

## 演化位置

`single query → complex unseen schema → large enterprise SQL workflow`

到 Spider 2.0，text-to-SQL benchmark 已经明确变成了一个 agent-systems problem。