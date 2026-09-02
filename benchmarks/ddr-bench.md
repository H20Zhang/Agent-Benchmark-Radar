# DDR-Bench：data agent 能不能自己决定“什么值得查”

**中文** | [English](ddr-bench.en.md) · [返回 Radar](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://arxiv.org/abs/2602.02039) · [代码](https://github.com/thinkwee/DDR_Bench)

## 它到底测什么

DDR-Bench 测 **investigatory intelligence**：agent 拿到 data/entity context，但没有预定义 analytical question，需要自己设 goal、探索并发现可验证 insight。这和用户已经告诉你“请做什么分析”的 executional intelligence 不同。

## 相比此前评测多测了什么

大多数 data-agent benchmark 都从 well-formed task 开始，而真实 analyst 经常从“这里到底发生了什么？”开始。DDR 把 problem formulation 放进 agent loop，并用 checklist-based evaluation 让 open-ended discovery 仍有部分可验证 ground truth。

## 决定性证据

benchmark 覆盖 healthcare record、SEC 10-K/XBRL financial data 与 behavioral data 等真实 domain。论文发现 frontier model 已出现一定 autonomous exploration 能力，但 long-horizon exploration 仍困难，而且表现不只由 scaffold 大小或模型规模决定，还依赖 agent 本身的探索策略。

## 这个分数能证明什么

DDR-Bench 能支持 checklist 范围内 autonomous exploration 的判断，但不能等价于真正 novel discovery：任何 checklist 都预先定义了一组期待发现，open-ended credit 也会受到 evaluator/judge 影响。

## 公平比较契约

应固定 data snapshot、starting metadata、toolset、model、exploration budget 与 evaluator。不能给一边额外 candidate goal/schema interpretation，并要同时报告 insight coverage、成本和 exploration depth。

## 还没有测什么

business value、causal validity、checklist 外 novelty 与 stakeholder relevance 没有被完整测量；真实 investigation 还需要交互 clarification 和“证据什么时候已经够了”的 stopping judgment。

## 下一步最有判别力的验证

混合 planted verifiable insight 与真正 unlabeled dataset，再由 blinded domain expert 评 novelty。关键是区分 agent 会不会寻找 important unknown，而不是只会找回 benchmark 作者预埋的 checklist item。

## 演化位置

`answer a specified query → choose analytical subgoals → autonomous data investigation`

它把 agency 从执行阶段前移到了“决定要分析什么”。