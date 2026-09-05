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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究企业 SQL 工作流中的元数据搜索、方言与代码库导航，但必须先选定具体轨道。论文原始设置、Snow、Lite 与 DBT 不是同一任务集合；讨论难度或当前成绩时，轨道与版本比‘Spider 2.0’这个总名称更重要。

### 一个具体任务长什么样

示意任务：系统先查看企业数据库元数据和项目说明，再运行多条查询或修改转换项目，最终交付结果文件。正确查询需要同时理解数据模式、执行环境和任务产物，而不是输出一段看起来合理的 SQL。

### 最有判别力的实验

分别报告所选轨道、环境版本、允许访问的元数据与执行预算。把已知正确表的 oracle 条件单列，不与普通发现设置混排；对相同骨干比较元数据检索和工作流策略，定位发现、生成与执行各阶段的收益。

### 建议搭配

[livesqlbench](livesqlbench.md) · [data-eng-bench](data-eng-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single query → complex unseen schema → large enterprise SQL workflow`

到 Spider 2.0，text-to-SQL benchmark 已经明确变成了一个 agent-systems problem。