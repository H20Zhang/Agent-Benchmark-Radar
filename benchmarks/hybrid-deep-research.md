# HybridDeepResearch

## 测量对象

测智能体在 SQL 与网页证据之间传递实体、筛选条件和候选集合时，能否保持约束并完成端到端回答。

## 相比前身改变了什么

相较独立 SQL 或搜索评测，直接考察 SQL→搜索、搜索→SQL 和并行结果融合中的交接。

## 协议与比较条件

S2SQL 用只读执行及对齐后的结果表评分；另两类用 LLM 判答案。Pass@8 指八次至少成功一次，Avg@8 才是逐次平均；实时网页与冻结语料结果应分开。

## 决定性证据与结论上限

官方仓库区分论文用 preview 与新版 release：88 道题被改写，标准答案与参考 SQL 不变。人工挑出的高难子集不能代表全部 380 题。

## 最强混淆与限制

首发日期存在一手来源冲突：博客写 6 月 3 日，README 写 6 月 2 日，暂保留月份精度。9 月 8 日论文不是基准初次发布；判分器、提示、搜索后端和重试预算也会影响成绩。

## 未覆盖与下一步实验

公开 SQLite 开发环境与受治理的 Snowflake 评测环境不同；总分不能单独定位跨源交接机制。

固定模型与预算，比较无桥接提示、正确桥接实体和完整交接产物，分离跨源传递失败与 SQL/搜索内部失败。

## 谱系与使用建议

[LiveSQLBench](livesqlbench.md) · [DataSpace](dataspace.md) · [FDABench](fdabench.md)

本条为 `early_signal`：接受一个有用的测量对象，不据单篇结果改写长期稳定的领域地图。

## 一手来源与版本

[论文](https://arxiv.org/abs/2609.09410) · [已核全文](https://arxiv.org/html/2609.09410v1)

[code](https://github.com/Snowflake-AI-Research/HybridDeepResearch)

[data](https://huggingface.co/datasets/Snowflake/HybridDeepResearch)

[较早公告](https://www.snowflake.com/en/blog/engineering/hybrid-deep-research-benchmark/)

首发：**2026-06**；核验：**2026-09-17**。首发日期与本次收录日期分开。

[English](hybrid-deep-research.en.md) · [返回完整索引](../library/README.md)
