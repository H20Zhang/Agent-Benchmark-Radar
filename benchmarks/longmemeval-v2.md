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

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究从大量网页操作经历中积累环境知识，例如工作流规则和容易踩到的限制。它与长对话记忆的差别主要是经验来源和知识对象；最终仍是问答，因此不应把检索质量直接包装为网页行动能力。

### 一个具体任务长什么样

示意任务：历史轨迹显示某类操作必须经过特定页面状态，当前问题要求解释如何完成该流程。系统要从分散的视觉和工具记录中恢复可复用步骤，而不只是记住一次页面上的文字。

### 最有判别力的实验

按环境留出测试，而不是随机拆分同一网站的轨迹；同时比较有无历史经验和证据直接给定条件。记录检索延迟，再增加真实执行检查，分别识别环境记忆的可访问性、可迁移性与行动效用。

### 建议搭配

[ama-bench](ama-bench.md) · [memoryarena](memoryarena.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`long chat history → agent trajectory archive → compressed reusable environment knowledge`

V2 让 memory 开始和“重新获取经验”在超大历史上正面竞争。