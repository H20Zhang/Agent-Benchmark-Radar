# InsightBench：Data Analyst 的输出不是 SQL，而是有价值的 insight

**中文** | [English](insightbench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2407.06423) · [代码](https://github.com/ServiceNow/insight-bench)

## 它在测什么

InsightBench 构造 100 个 business-use-case datasets，并植入可验证 insights。agent 需要经历 question formulation、EDA、insight discovery 与 recommendation，最终用 two-way LLM evaluator 等方式判断报告是否捕捉到重要洞察，而不是只执行预先指定 query。

## 相比什么前进了

text-to-SQL benchmark 已经告诉系统要回答什么。InsightBench 把“应该分析什么、什么结果值得报告”加入 evaluation object，更接近 analyst 的开放式工作。

## 分数边界

insight coverage 支持在 planted-insight distribution 与 judge 下发现预设业务模式；它不证明真实业务价值，因为 synthetic/planted patterns 与 evaluator 会定义什么算“洞察”。

## 公平比较条件

锁定 dataset generation、insight references、analysis budget、agent scaffold 与 evaluator generation。不同 judge 或 planted-insight density 应分 snapshot。

## 下一步评测坐标

下一步要从“找到预埋 insight”走向真实业务语义、利益相关者目标与 decision impact，评价洞察是否改变实际决策。
