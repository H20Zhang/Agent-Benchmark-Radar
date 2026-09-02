# AgenticRAGTracer：final answer 错了之后，必须知道是哪一 hop 先坏掉

**中文** | [English](agenticragtracer.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.19127) · [代码](https://github.com/YqjMartin/AgenticRAGTracer)

## 它在测什么

AgenticRAGTracer 提供 1,305 个 multi-domain instances，并为 multi-step agentic RAG 提供 hop-level intermediate validation。evaluation object 不只是 final exact match，而是每一步 retrieval/reasoning chain 是否沿着可验证的中间状态推进。

## 相比什么前进了

普通 multi-hop QA 只知道最后答错；RAGCap-Bench 等能力测试又可能脱离真实 trajectory。AgenticRAGTracer 把 validation 放回实际 chain，使“第一 hop 没搜到”“hop allocation 不合理”“后续 reasoning 基于错误 evidence”可以被分开观察。

## 分数边界

hop-level correctness 支持定位在 benchmark 定义的 chain 上哪里发生偏离；它不等于真实 agent 的唯一 causal trace。自动生成的 hop structure 可能只是一条可行路径，模型用另一条有效路径也可能被判 deviation，因此不能把 hop agreement 当作 universal planning quality。

## 公平比较条件

锁定 hop definition、instance version、retrieval interface、backbone 与 final evaluator。若允许不同工具或 alternative valid trajectories，应单独建立 tolerant track，而非直接和 strict-hop 分数混排。

## 下一步评测坐标

下一步应从 gold-hop tracing 推进到 counterfactual repair：替换某一步 evidence 或 decision 后，最终 success 是否恢复，从而验证真正 load-bearing 的 failure point。
