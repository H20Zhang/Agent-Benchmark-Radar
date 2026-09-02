# SGR-Bench：找到正确网站还不够，还要建立正确 retrieval state

**中文** | [English](sgr-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.22219) · [数据](https://huggingface.co/datasets/PKUAIWeb/SGR-BENCH)

## 它到底测什么

SGR-Bench 评估 **state-gated retrieval**：agent 即使到了正确专业网站，只有把 filter、hierarchy、scope、view 配成正确状态，answer-bearing evidence 才会出现。因此 retrieval-state control 本身就是任务，而不是 source discovery 后的 UI 细节。

## 相比此前评测多测了什么

很多 web benchmark 把“找到相关 source”当作主要进展；SGR-Bench 说明 specialized data portal 更像 interactive query interface：同一个网站在不同 state 下会给完全不同的数据 slice。

## 决定性证据

benchmark 有 100 个专家任务，覆盖 6 类 source family、12 个公开 data ecosystem，并对同一问题提供 constraint-guided 与 goal-oriented 两种 formulation。最强系统 item-level F1 只有 66.18%，row-level F1 更低。对 156 条可分析失败 trajectory，retrieval-scope drift 占 37.2%，criterion mismatch 27.6%，最终 answer composition 只有 10.3%。

## 这个分数能证明什么

这是很强的证据：source discovery 与 retrieval-state control 是不同能力。但结果仍依赖 browser/harness，因为如何操作网站控件本身就在 measurement object 里。

## 公平比较契约

应固定 site snapshot/time、browser/tool interface、agent model、action budget 与 task formulation，同时报告 item/row F1，并保留 constraint-guided 与 goal-oriented 的区分；prompt 里直接给 filter 会显著降低 planning 难度。

## 还没有测什么

这个 setting 比 general deep research 窄，也容易受到公开网站 UI drift 影响；authentication、private enterprise tool、write operation 和任意文档 retrieval 都不在核心 protocol。

## 下一步最有判别力的验证

为同一数据提供 canonical structured API，与 browser interaction 做 paired comparison，直接量化 semantic query planning 与 GUI/interface grounding 各自贡献了多少失败。

## 演化位置

`find the source → configure retrieval state → execute semantic data query`

它把 search-agent benchmark 和 semantic query processing 直接连了起来。