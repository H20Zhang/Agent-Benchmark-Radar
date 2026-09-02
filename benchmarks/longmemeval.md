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
