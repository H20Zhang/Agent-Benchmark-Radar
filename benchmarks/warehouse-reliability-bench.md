# WarehouseReliabilityBench：SQL 能执行，不代表 business truth 是对的

**中文** | [English](warehouse-reliability-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2608.09254)

## 它到底测什么

WarehouseReliabilityBench (WRB) 评估 analytics agent 在 standard、ambiguous、unanswerable、schema-drift、adversarial question 下能不能给 **business-correct behavior**。两个 synthetic warehouse 共 400 个 frozen task，其中大约一半根本没有正确 SQL，正确行为应是 clarification、abstention 或 refusal。

## 相比此前评测多测了什么

execution-match 默认每个问题都应该映射到 query；生产 analytics 的失败往往更早发生：“revenue”有两个合法定义、warehouse 根本算不出某个指标，或者 deprecated column 仍能执行但 business meaning 已错。WRB 因此测 semantic behavior contract 与 false success，而不只测 syntax。

## 决定性证据

80-task frozen test split 上，QueryProof 相比 direct-prompted 32B baseline 的 Business Truth Rate 高 +0.237，论文给出的 95% 区间是 [+0.112, +0.375]；False Success Rate 从 0.754 降到 0.351。但论文主动承认这个比较被 scaffold confound，按 template family 重采样后区间会包含 0，因此“方向”比“具体 effect size”更可信。

## 这个分数能证明什么

WRB 很强地支持一个 benchmark claim：**成功执行 SQL ≠ business correctness**。QueryProof 结果支持 deterministic semantic/rule gating 这一系统方向，但不能推出“7B 模型胜过 32B”，也不能说某个单一 component 导致了提升。

## 公平比较契约

必须固定 warehouse seed/snapshot、semantic-layer definition、physical catalog、task split、model、scaffold 与成本核算，并分别报告 Business Truth Rate、False Success Rate、coverage、abstention/clarification 与 cost。scaffold 不同的时候禁止做 model-size 因果结论。

## 还没有测什么

证据基座很窄：两个 synthetic domain、一个 seed、一个 model family、一个 SQL dialect，而且 test exposure 已被披露；对 BIRD/Spider 或真实 warehouse 的 transfer 未被证明。

## 下一步最有判别力的验证

在全新 unseen warehouse family 上，把同一个 semantic/rule scaffold 加到更大的 baseline model，再分别 ablate semantic resolution 与 post-execution check，这才是做 causal attribution 所需的实验。

## 演化位置

`SQL execution correctness → semantic business truth → reliability-aware analytics agent`

它把评测提升到 query language 之上：有时正确的 data-agent 输出就是“不应该执行 SQL”。