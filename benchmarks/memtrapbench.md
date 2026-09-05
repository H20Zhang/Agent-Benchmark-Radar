# MemTrapBench

## 它到底测什么

MemTrapBench 测的是 **memory applicability judgment**：即使一段历史记忆被正确保存、也与当前问题语义相关，agent 能否判断它现在是否仍应该参与推理，而不是因为“retrieval 相关”就机械复用。它把长期记忆的失败模式从“忘了什么”推进到“记得没错，但用错了”。

## 相比前身多测了什么

LoCoMo / LongMemEval 一类评测主要问历史信息能否被召回并支持 QA；staleness benchmark 又更多问新旧事实冲突时能否排对版本。MemTrapBench 的增量在于：历史内容本身可以依然真实、也可以语义相关，但**当前任务的条件已经变化，使这段记忆不再是有效先验**。因此 retrieval relevance 与 decision relevance 被显式拆开。

## 决定性证据

benchmark 对同一当前任务构造 memory 与 no-memory 配对条件，四个子集共 **1,050 个多轮样例**，覆盖 reasoning fixation 与 belief distortion。作者报告所有受测 memory strategy 都低于 no-memory，最大下降超过 **10 个百分点**。重要信号不是“memory 总体有害”，而是 planted prior 在 context shift 后仍会被 agent 过度采用。

## 这个分数支持什么判断

它支持“在刻意构造的 context shift 中，相关但当前无效的历史记忆会产生可测负效应”。它不支持“长期记忆平均而言不如 no-memory”，因为最终问题被设计成不依赖历史也能作答，no-memory 条件天然规避了 planted prior；真实工作负载中旧经验有时恰恰是必要信息。

## 公平比较条件

比较 memory strategy 时应固定 backbone、当前任务、历史内容、memory visibility、retrieval policy、prompt、judge 和 no-memory baseline。最好进一步区分三种失败：错误检索了不相关记忆、正确检索但错误采用、正确采用但推理失败。否则只看最终 accuracy 无法判断 applicability mechanism 是否真的工作。

## 研究上怎么用

MemTrapBench 很适合验证 **retrieve-then-decide、memory gating、contextual validity classifier、confidence-aware memory use** 等机制。一个 memory system 如果只优化 recall/precision，可能反而增加 harmful exposure；研究者应该同时报告 recall utility 与 harmful-reuse rate，形成“accessibility × applicability”二维评测。

## 下一步最有价值的验证

当前最大缺口是自然工作流中 harmful reuse 的真实发生率，以及开放环境里 agent 是否能自主推断记忆的适用边界。最高杠杆实验是从真实 coding/data-agent/personal-assistant trajectory 中构造自然 context shift，比较显式 gating、temporal/version metadata 与纯 LLM judgment，验证收益是否超出人工 planted trap。

## 谱系位置

`map_delta=early_signal`。它与 staleness/update benchmark 共同支持“**memory validity before use**”这一方向，但测量对象不同：staleness 关注哪个版本当前有效，MemTrapBench 关注即使记忆是真的、它是否适用于当前决策。单篇工作仍不足以改写 durable Benchmark Map。

Primary: https://arxiv.org/abs/2608.20202

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究何时不该使用看起来相关的记忆。它直接挑战‘正确保存、正确检索就一定有益’；但人为设置的陷阱主要证明这种失效可能发生，不能据此估计自然任务中的发生频率。

### 一个具体任务长什么样

示意任务：旧任务形成了某种解题习惯或判断，新任务的条件已经变化，但措辞仍相似。系统若执着套用过去的经验，会比没有旧记忆时表现更差；错误发生在使用边界而非事实是否保存。

### 最有判别力的实验

对相同当前任务比较无记忆、有效相关记忆和应拒绝的相似记忆，固定总上下文预算。报告正迁移与负迁移两侧，而不是只优化拒绝率；一个一律不用记忆的系统并没有解决选择性使用问题。

### 建议搭配

[locomo-plus](locomo-plus.md) · [statemembench](statemembench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
