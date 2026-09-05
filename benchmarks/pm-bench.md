# PM-Bench：Agent Memory 不只是记住过去，也要记得未来要做什么

**中文** | [English](pm-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2607.12385)

## 它到底测什么

PM-Bench 测 **prospective memory**：智能体在继续执行其他活动时，能否保留用户的延迟意图，并在正确未来时间、cue 或环境状态出现时执行，而不是等用户再次提醒。任务受到认知科学 Virtual Week 范式启发，运行在模拟七天的文本环境中。

## 相比此前评测多测了什么

LoCoMo、LongMemEval 等长期记忆基准主要问“过去发生了什么 / 当前状态是什么”；PM-Bench 把时间方向翻转成“未来条件满足时要记得做什么”，从 retrospective recall 推到 intention maintenance + cue monitoring + timely execution。

## 决定性证据

论文比较 8 个 LLM、8 种 agent configuration；最好的 GPT-5.4 agent 也只有 65.1% F1，而且没有一种改善 prospective memory 的策略跨模型稳定占优。

## 这个分数能证明什么

它支持受控模拟环境中的 delayed-intention maintenance 与 cue-triggered execution。它不证明现实日历、异步通知、工具失败或高风险动作下的长期可靠性。

## 公平比较契约

固定 backbone、agent configuration、时间表示、cue 可见性、ongoing-task policy 与评分规则；如果一方拥有显式 scheduler/notification tool 而另一方只能靠上下文记忆，必须分轨道报告。

## 还没有测什么

真实数天/月时长、外部工具与通知系统、多个相互冲突或撤销的未来意图，以及执行错误的安全代价。

## 下一步最有判别力的验证

将同一 intention 分别设置为 time-based、event-based、更新、取消与冲突条件；配对比较纯上下文、外部持久记忆、显式 scheduler，并按首次正确触发、漏触发与误触发分开评分。

<!-- RESEARCH-DECISION:START -->
## 研究决策卡
### 什么时候值得用
当你的 memory claim 是“未来需要的时候会主动做对事”，而不是“现在问它能不能复述旧事实”时，PM-Bench 是直接坐标。
### 一个具体任务长什么样
示意任务：用户周一提出“周四出现某个环境 cue 时完成 X”，智能体随后持续处理无关活动；到 cue 真正出现时必须首次正确触发，同时不应提前执行。
### 最有判别力的实验
对相同 intention 配对 time cue、event cue、更新、取消与冲突，并比较 context-only、persistent memory 与 scheduler。
### 建议搭配
[LongMemEval](longmemeval.md) · [MemoryArena](memoryarena.md) · [Mem2ActBench](mem2actbench.md)
> **读分数的原则：** prospective-memory F1 不等于现实自动化的端到端安全可靠性。
<!-- RESEARCH-DECISION:END -->

## 演化位置
`past-event recall → current-state tracking → future-intention execution`
