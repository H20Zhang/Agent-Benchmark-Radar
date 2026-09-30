# Data Engineering Benchmark：容器内可执行的数据工程任务

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-07-29<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://github.com/Snowflake-Labs/data-eng-bench)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** | [English](data-eng-bench.en.md) · [主入口](../README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围与版本

已核对下述官方协议、实现配置和可获得结果；未独立复现实验，未声称完整论文阅读。

完整读取官方 README、提交协议、指标计算源码与所述配置，核对修复提交说明；没有逐个审计全部 103 个任务，也未找到官方论文。

[官方仓库文档 · a3278ad102829a6084dde086244a0ef665a8011c · 2026-09-30](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)

模型结果缺口：本次未能读取官方 Harbor 成绩，固定提交内也没有模型结果行；不以任务数量或配置示例冒充实验成绩。
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 方法与测量对象

data-eng-bench 将代理放入容器化 dbt 项目，给出工单式需求，要求修改或创建模型、运行转换并修复问题。隐藏 pytest 验证器逐行比较已物化数据与参考结果。103 个任务共享一个合成零售仓库，既可在本地 DuckDB 上运行，也可在 Snowflake 隔离克隆库中运行；覆盖分析模型、错误修复、维度／快照和增量数据工程。

[来源](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)

<!-- EDITORIAL-METHOD:START -->
编辑比较：与 Spider 一类只交 SQL 的任务相比，Data Engineering Benchmark 以容器中的工程产物、环境约束与可执行测试为终点，更接近 DAComp 的工程侧。它增加实现与验证工作流，但当前可核验材料不足以填入模型结果，因此这里只定位协议，不推断系统排名。
<!-- EDITORIAL-METHOD:END -->
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 评分与实验条件

官方提交协议要求固定数据集版本、覆盖全部任务、每题至少三次，错误和被判定违规的运行都计零。当前指标源码中，Accuracy 是成功运行数除以全部运行数；另算按任务平均的 pass@2/pass@3，不能混用。示例配置使用 Claude Code/Claude Opus 4.8/high、三次尝试和四路并发，它是可运行配置，不是已测成绩。一个实际任务配置规定代理 4,000 秒、验证器 3,000 秒、2 CPU 和 8,000 MB 内存；不能未核对全部任务就宣称是统一预算。

[来源](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:limitations:START -->
## 结果解读、来源限定与下一步

本次完整读取官方总说明、提交协议、指标计算与上述配置，但未逐个审计全部任务。未找到官方论文；链接的 Harbor 榜单本次无法读取，仓库内也没有已提交结果行，因此没有足够证据填入模型成绩或宣称修复后无人重跑。已确认的修复涉及 Snowflake 连接及清理；仅编译／解析通过不能替代端到端复验。

官方说明将一个时区敏感的 DuckDB 任务标为建议性结果。旧版 Harbor 还可能静默忽略禁用网页工具的选项；参考解法已经公开，必须验证隔离实际生效。

固定验证器和后端版本，对同一模型做完整三次运行，分别报告运行级准确率、任务级 pass@k、环境故障和被取消成绩；对协议修复前后用相同代理重跑，并隔离公开参考答案以减少泄露。

[来源](https://github.com/Snowflake-Labs/data-eng-bench/blob/a3278ad102829a6084dde086244a0ef665a8011c/README.md)
<!-- EVIDENCE:limitations:END -->
