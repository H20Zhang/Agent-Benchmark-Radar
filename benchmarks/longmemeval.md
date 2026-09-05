# LongMemEval：把“记得”拆成五种长期能力

**中文** | [English](longmemeval.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2410.10813) · [代码](https://github.com/xiaowu0162/LongMemEval)

## 它在测什么

LongMemEval 用 500 个高质量问题和可扩展、带时间戳的 user-assistant histories，分别测试 information extraction、multi-session reasoning、knowledge update、temporal reasoning 与 abstention。与一次性把长文本塞给模型不同，协议强调历史是随交互逐步出现的，系统需要在线吸收，再在之后回答问题。

## 相比什么前进了

LoCoMo 已证明很长的多 session 对话会让模型失效；LongMemEval 的关键增量是把“长期记忆”进一步拆成 update 与 abstention 等能力，并用属性控制的历史构造让上下文长度可以扩展。因此一个系统在 factual recall 上高分，不再足以说明它能正确处理事实更新或知道何时不回答。

## 决定性证据与分数边界

官方仓库在 2025 年还专门清理 history sessions，以减少历史构造对答案正确性的干扰；这本身说明 benchmark version 是 load-bearing variable。当前网页不把第三方 LongMemEval 成绩直接混为官方榜单，因为 answerer、retrieval top-k、judge 和数据版本经常不同。这里的分数能支持“在给定历史版本和 reader 下，系统提供了多少可用长期证据”，不能单独定位 memory write/retrieval 的因果贡献。

## 公平比较条件

必须锁定数据版本、history construction、reader/answerer、retrieval budget 与 grader。尤其要区分 full-history、retrieval-only 与外部 memory system；如果 reader 或 top-k 同时变化，端到端 accuracy 只能当 packaged-system evidence。

## 下一步评测坐标

LongMemEval 仍以历史 QA 为终点。LongMemEval-V2 随后把对象推进到 agent-environment trajectories、workflow knowledge 与 latency；更进一步还要直接测 remembered experience 是否改善未来行动。

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究‘记得住但用错版本’这类长期助手问题。它的价值在于把更新、时间推理和弃答拆开，而非用一个总体准确率替代所有记忆能力；报告分项通常比再加一个平均分更有诊断价值。

### 一个具体任务长什么样

示意任务：用户先给出旧偏好，数次会话后明确修改，随后询问当前应采用哪项安排。系统必须识别更新关系，而不是在两个相似片段中挑一个；没有充分历史证据时还应避免猜测。

### 最有判别力的实验

让旧事实和新事实都进入检索结果，再与仅给当前有效事实的条件比较。若前者仍失败，瓶颈已不只是召回率，而是冲突消解或时态解释；另报没有答案的问题，防止通过一律作答抬高部分题型成绩。

### 建议搭配

[statemembench](statemembench.md) · [scale-qa](scale-qa.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
