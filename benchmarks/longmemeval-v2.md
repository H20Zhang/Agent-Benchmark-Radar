# LongMemEval-V2：在超大 agent history 上压缩可复用经验

**中文** | [English](longmemeval-v2.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.12493) · [项目页](https://xiaowu0162.github.io/longmemeval-v2/) · [代码](https://github.com/xiaowu0162/LongMemEval-V2)

## 它到底测什么

LongMemEval-V2 测 memory system 能否把巨量 **web-agent / enterprise trajectory** 压缩成之后推理可用的 compact evidence。能力覆盖 static state recall、dynamic state tracking、workflow knowledge、environment gotcha 与 premise awareness，不再只是对话事实。

## 相比此前评测多测了什么

LongMemEval V1 已经把 history 拉长并显式评估 update/temporal reasoning；V2 同时改变 experience 来源与尺度：历史可达到 500 条 trajectory、115M token，有用知识包括 action 中学到的 procedure 与环境特性。memory 的角色由 chat retriever 变成 experience compressor。

## 决定性证据

benchmark 有 451 个手工 curated question，覆盖 web / enterprise 场景和 5 类能力。AgentRunbook-C 平均 accuracy 72.5，对比论文中最强 RAG baseline 的 48.5，以及 off-the-shelf coding-agent memory 的 69.3。后者同时付出明显更高 latency，因此 accuracy–latency frontier 本身就是结果的一部分。

## 这个分数能证明什么

它能支持“系统会不会从超大 trajectory archive 中提取可复用 knowledge”的判断，并说明 active agentic retrieval 可能以更高成本超过 passive RAG。但如果 agentic retrieval 同时改变 search depth、reasoning 与 tool use，就不能把增益单独归给 memory component。

## 公平比较契约

应固定 history snapshot、backbone、最大返回 evidence、retrieval/tool-call budget 与 answer evaluator，并把 latency、token/tool cost、evidence volume 和 accuracy 一起报告。拿 fixed top-k RAG 和不受限 iterative search 直接比，回答的是两个不同问题。

## 还没有测什么

最终任务仍然是 context-gathering QA，而不是未来 closed-loop task success。trajectory 持续到来时的 write/update cost、过时 procedure 的维护，以及破坏性 environment change 仍缺少评测。

## 下一步最有判别力的验证

把五类 knowledge 转成 future executable task，在 equal-cost 下比较 passive retrieval、compiled runbook 与 agentic reacquisition。真正的系统 trade-off 是：哪些 experience 值得长期保留，哪些应该便宜地重新获取。

## 演化位置

`long chat history → agent trajectory archive → compressed reusable environment knowledge`

V2 让 memory 开始和“重新获取经验”在超大历史上正面竞争。