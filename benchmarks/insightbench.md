# InsightBench：从“回答一个 query”走向“自己发现 business insight”

**中文** | [English](insightbench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2407.06423) · [代码](https://github.com/ServiceNow/insight-bench)

## 它到底测什么

InsightBench 评估 **end-to-end business analytics**：自己提出值得分析的问题、执行分析、解释结果、综合 insight、给出 actionable next step。100 个 dataset 覆盖 finance、incident management 等 business use case，每个都有人为 curated planted insight。

## 相比此前评测多测了什么

多数 data-analysis benchmark 已经把 query 写得很明确。InsightBench 把 agency 前移：agent 需要决定“什么值得查”，并最终交付一组 coherent finding，而不是只计算用户指定的 statistic。

## 决定性证据

open-ended insight 没有唯一 deterministic answer，因此 benchmark 设计 two-way LLaMA-3 evaluator，并对数据做较严格 quality assurance。提出的 AgentPoirot end-to-end baseline 优于主要解决单 query 的 Pandas Agent 等方案。

## 这个分数能证明什么

它能支持 agent 是否发现 benchmark 作者定义的 business insight 并组织成分析；但对 truly novel / decision-useful discovery 的证明较弱，因为 planted-insight set 预先定义了“什么算重要”，且 credit 经过 evaluator judge。

## 公平比较契约

应固定 dataset、agent starting prompt、toolset、exploration budget、evaluator model/version 与 report format，并把 planted-insight coverage 和 presentation quality 分开；否则流畅 summary 会掩盖 evidence 漏失。

## 还没有测什么

真实 business insight 取决于 stakeholder objective、causal validity、opportunity cost，以及 recommendation 是否真的改变决策。某个 planted insight 即使统计上能找出来，也可能经济上并不重要。

## 下一步最有判别力的验证

加入 blinded domain expert 对 checklist 外新 insight 的评分，再接 downstream decision task。真正应该测的是“是否找到值得行动的东西”，而不是只复现 benchmark 设计者预埋的发现。

## 演化位置

`answer a data query → discover a set of insights → decision-oriented business analysis`

InsightBench 把 data agent 从执行推进到 analytical agenda setting。