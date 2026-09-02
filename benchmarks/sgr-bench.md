# SGR-Bench：搜索失败可能发生在“已经找到网站，但没进入正确 retrieval state”

**中文** | [English](sgr-bench.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.22219) · [数据](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)

## 它在测什么

SGR-Bench 包含 100 个 expert-curated tasks，覆盖六类 source family 与 12 个 public data ecosystems。任务的关键不是找到正确网站，而是继续配置 filter、hierarchy、scope 或 view，直到页面进入能暴露答案的正确 retrieval state；最终用 item-F1 / row-F1 评价结构化 evidence extraction。

## 相比什么前进了

BrowseComp 类 benchmark 主要问“能不能在 web 上找到隐藏事实”。SGR-Bench 把 failure 再拆一层：source discovery 成功后，agent 是否知道如何把 site-specific state 调到正确位置。它因此把 retrieval-state control 从 browser implementation detail 提升成独立能力。

## 分数边界

更高 item/row F1 支持 agent 在给定 browser tool、site snapshot 与 harness 下完成 state-gated retrieval；它不能直接证明 general web research 更强，因为任务集中在特定 portal/data ecosystems，且 site drift 会改变操作路径。

## 公平比较条件

锁定 browser/tool interface、网站版本、task constraints、agent harness 与 allowed actions。页面结构或 filter API 改版后的结果应使用新的 protocol snapshot。

## 下一步评测坐标

下一步应将 state-gated retrieval 与跨站证据组合、freshness 和失败恢复连接起来：错误 filter state 是否能被诊断并重新规划，而不是只看最终 F1。
