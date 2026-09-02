# AgenticRAGTracer：定位 retrieval-reasoning chain 到底在哪一跳坏掉

**中文** | [English](agenticragtracer.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.19127) · [代码](https://github.com/YqjMartin/AgenticRAGTracer)

## 它到底测什么

AgenticRAGTracer 给 multi-step retrieval reasoning 增加 **hop-aware intermediate validation**。它不只提供 final question/answer，还给出从 atomic evidence need 逐步连接到最终 query 的 intermediate hop question。

## 相比此前评测多测了什么

multi-hop answer 做错后，传统 benchmark 无法区分 agent 是停得太早、走了多余分支、取错证据，还是取对后推理错。hop label 让 step allocation 与 chain shape 变成可观测对象。

## 决定性证据

benchmark 有 1,305 个自动构造实例，覆盖多个 domain，并与主流 benchmark 去重。最难 subset 上 GPT-5 也只有 22.6% exact match。hop-aware diagnosis 发现很多失败来自 distorted chain：要么过早 collapse，要么无必要地 over-extend。

## 这个分数能证明什么

它能诊断 reasoning-chain allocation 与 intermediate retrieval，但因为大量数据由 LLM 自动构造，annotated hop structure 不应被默认成问题唯一的因果分解。

## 公平比较契约

应固定 model、tool、step/call budget 与 hop evaluator，同时报告 final EM、hop completion 和 chain length。若一种不同但有效的 reasoning path 仅因不符合生成模板就被判错，测到的是 conformity，不是 search competence。

## 还没有测什么

真实 web research 往往有多条可行 decomposition、uncertain subgoal，甚至边搜边发现路径；自动生成的 hop chain 可能带 construction artifact。

## 下一步最有判别力的验证

人工给一部分题标注多个等价 solution graph，检查 diagnostic conclusion 在 alternative path 下是否仍成立，从而验证“wrong chain”是真推理错误，而不是路径不同。

## 演化位置

`multi-hop final answer → hop-level trace → causal diagnosis of search allocation`

它把 reasoning chain 的长度和形状本身变成了评测对象。