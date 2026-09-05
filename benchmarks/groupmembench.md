# GroupMemBench：多人对话中的 memory 不是把多个单人历史拼起来

**中文** | [English](groupmembench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2605.14498)

## 它到底测什么

GroupMemBench 评估 **multi-party conversation memory**：身份与 audience 会改变信息含义。它重点测 group dynamics、speaker-grounded belief 与 audience-adapted language，因此同一个术语或观点，取决于“谁说的、谁在问”。

## 相比此前评测多测了什么

大多数 agent-memory system/benchmark 都是假设一个 user 对一个 agent。把多个一对一 history 直接拼起来，会丢失 reply structure、per-speaker belief、shared/private context 和 Theory-of-Mind 变化。GroupMemBench 用 graph-grounded conversation，并把每个 adversarial query 绑定到具体 asker。

## 决定性证据

benchmark 覆盖 multi-hop reasoning、knowledge update、term ambiguity、user-implicit reasoning、temporal reasoning、abstention 六类 query。当前最强被测 memory system 平均只有 46.0%，其中 knowledge update 27.1%、term ambiguity 37.7%；简单 BM25 还能匹配或超过多数 agent memory。这说明当前 ingestion pipeline 可能在摘要/结构化过程中丢掉 group memory 所需的 lexical 与 relational signal。

## 这个分数能证明什么

这是很强的证据：**speaker/audience structure 不是可有可无的 metadata**。但数据仍是合成的，也没有直接区分失败来自 ingestion、indexing、retrieval，还是最终 Theory-of-Mind reasoning。

## 公平比较契约

应固定 conversation graph、speaker identity、asker identity、backbone、retrieval budget 与 audience metadata。比较 ingestion scheme 时还要保留原始 lexical form；如果某个系统先做更激进 summary，可能直接把 benchmark 要测的 ambiguity cue 压掉。

## 还没有测什么

真实群体空间还有 permission、private thread、成员变动、moderation、跨 channel identity；把一个人的 belief 暴露给另一个人的社会后果属于 governance，而不是 answer accuracy 能覆盖的。

## 下一步最有判别力的验证

加入 oracle speaker-aware retrieval，在相同 answer model 下比较 raw-message、per-user、thread、graph memory，判断主要损失发生在 write 阶段，还是已经取对 social state 后的 reasoning 阶段。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究多人交流中的发言者、信念和受众条件。把全部聊天当成一个统一用户的记忆库会抹掉最重要的变量；回答内容真实，也可能因归属错误或使用了错误角色的术语而失败。

### 一个具体任务长什么样

示意任务：不同成员对同一计划持有不同观点，某个术语在不同团队中也有不同含义。当前提问者的身份决定应如何解释问题；系统需要把内容与说话者、回复关系和目标受众一起检索。

### 最有判别力的实验

在相同对话文本上保留、隐藏或打乱角色与回复结构，按提问者分别评分。若正确元数据给定后仍失败，再检查信念推理；若只有人工角色标签有效，则不能直接宣称系统能自主建立群体记忆。

### 建议搭配

[gatemem](gatemem.md) · [came-bench](came-bench.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->

## 演化位置

`single-user memory → speaker-grounded group memory → socially governed shared state`

它说明多人 memory 不是“更多文本”，而是一种 relational state。