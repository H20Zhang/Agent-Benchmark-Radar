# RAGCap-Bench：把 Agentic RAG 的中间能力单独测出来

**中文** | [English](ragcap-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2510.13910)

## 它到底测什么

RAGCap-Bench 不只看最终答案，而是评估 Agentic RAG workflow 中反复出现的 **intermediate task / capability**。taxonomy 来自真实系统输出、常见任务和 failure pattern，希望把黑盒 end-to-end failure 分解成更具体能力。

## 相比此前评测多测了什么

传统 end-to-end RAG score 把 planning、retrieval、reasoning 和中间决策错误压成一个数。RAGCap-Bench 让这些 latent ability 显式可测，使失败可以对应到 capability class，而不是从最终答案倒猜。

## 决定性证据

论文发现，在 RAGCap 上表现更强的 slow-thinking model，end-to-end Agentic RAG 结果也更好。这个相关性说明所选 intermediate task 至少捕捉到了一部分真实有用的能力，而不是任意 micro-benchmark。

## 这个分数能证明什么

capability score 能用于诊断 standardized micro-task 下的 weakness，但不能证明“把某个 capability 提高就一定会改善部署系统”；interface、tool 与 orchestration 决定能力能否在真实 trajectory 里被兑现。

## 公平比较契约

应固定 prompt/harness、backbone version、tool description 与 task budget。把 RAGCap 和 end-to-end 关联时，还要用 matched system / resource budget，否则更大的 scaffold 可能同时把两个分数都抬高。

## 还没有测什么

capability decomposition 可能漏掉 emergent coordination effect；micro-task 也可能比真实 trajectory 的 messy state 简单。cost、stopping 与 error recovery 仍是系统层属性。

## 下一步最有判别力的验证

只干预一个弱 capability，保持其他 agent 组件不变，检查预测的 end-to-end failure 是否真的下降，从 correlation 推进到 causal diagnostic value。

## 演化位置

`final RAG score → capability decomposition → intervention-based agent diagnosis`

它是否重要，取决于这些中间坐标能不能真的告诉研究者“下一步该修哪里”。