# Warehouse Reliability Bench：Data Agent 最危险的失败不是答错，而是“看起来成功但业务上错”

**中文** | [English](warehouse-reliability-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.09254) · [代码](https://github.com/k-w-lee/query_proof)

## 它在测什么

Warehouse Reliability Bench 含 400 个 tasks，建立在两个 deterministic synthetic warehouses 上；184 个可直接回答，216 个应该 clarify、abstain 或 refuse，另有 80 个 held-out cases。核心指标包括 Business Truth Rate 与 False Success Rate，并通过 executable ground truth、behavior contract 与 rule gates 检查系统有没有把业务语义做错却宣布成功。

## 相比什么前进了

传统 text-to-SQL 只问 SQL/结果是否匹配。真实 BI 中更危险的是 metric definition、grain、join 或 time semantics 错了但输出仍合理。该 benchmark 把“什么时候不能回答”和 business truth 一起放进评测。

## 分数边界

Business Truth / False Success 支持在 synthetic warehouse rules 与 validators 下的可靠性；它不代表真实企业全部 semantic complexity，但比单纯 SQL execution 更接近 analyst risk。

## 公平比较条件

锁定 warehouse generation、business rules、behavior contract、validator version、agent hints 与 tool budget。answerable 与 clarify/abstain/refuse slices 应分别看。

## 下一步评测坐标

下一步需要 real semantic layers、metric changes、access policies 与 downstream decision cost，让错误业务答案的影响成为可量化 outcome。
