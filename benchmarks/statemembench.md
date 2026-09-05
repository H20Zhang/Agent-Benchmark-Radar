# StateMemBench

## 它到底测什么

StateMemBench 测的是 **跨会话修订后当前 operative state 的维护能力**。事实、约束与决定会持续新增、覆盖或依赖彼此；最终回答必须基于当前仍有效的状态，而不是只要能召回某条历史记录就算成功。它关注的是“系统此刻相信什么、哪些规则仍生效”，而不仅是 old/new fact ranking。

## 相比前身多测了什么

LongMemEval / MemoryAgentBench 已经包含 knowledge update，但 update 往往和 retrieval、长上下文理解及一般 reasoning 混在一起。StateMemBench 使用 symbolic event program、deterministic replay 与 closed-pool grader，显式生成状态依赖和修订轨迹，因此更直接地隔离 **state drift**：错误答案可以区分为采用 current state、命中 targeted superseded state，还是其他失败。

## 决定性证据

benchmark 包含 **234 个多会话场景、322 个 probe**。grader 区分 current、targeted-superseded 与 other outcome。论文报告 StateMem 在相同 DeepSeek backbone 下将分数从 **0.205 提到 0.363**；即使做 length/cost-matched control，仍保留约 **+15–32 point** 的结构收益。最重要的证据是：收益并不完全由更长 context 或更多 token 解释。

## 这个分数支持什么判断

结果支持“在显式依赖、受控修订的协议下，结构化维护当前状态能改善 operative-state correctness”。它不等价于一般 memory quality，也不能直接证明真实 agent 在开放环境中因此行动得更好，因为 benchmark 的依赖关系、修订方式和最终 probe 都被严格构造。

## 公平比较条件

比较方法时必须固定 backbone、event program、可见历史、state representation budget、token/cost budget、replay policy 和 grader。尤其要保留 length/cost-matched control，否则结构化 state 方法可能因为保留更多显式信息而天然占优。还应分别报告 current accuracy 与 targeted-superseded error rate，避免平均分隐藏“旧状态泄漏”。

## 研究上怎么用

StateMemBench 适合测试 **state store、versioned memory、dependency-aware update、structured consolidation** 等机制。它与 staleness benchmark 应组合使用：前者验证多步修订后能否恢复完整当前状态，后者更像局部 retrieval/ranking unit test。对于 agent memory paper，这种组合比单独 LongMemEval QA 更能定位 update mechanism 的真实作用。

## 下一步最有价值的验证

当前缺口包括潜在关系发现、真实用户/环境漂移、隐私治理，以及 state tracking 是否改善后续 closed-loop action。最高杠杆的下一步是去掉显式 dependency annotation，让 agent 自己从自然交互中发现哪些事实互相覆盖或约束，并把 state correctness 与未来 tool/action success 连接起来。

## 谱系位置

`map_delta=early_signal`。它把 update evaluation 从“新旧事实是否都存着”推进到“**当前 operative state 是什么**”。这个 coordinate 与 staleness、applicability 互补，但目前仍缺少独立自然数据证据，因此 durable Benchmark Map 暂不改。

Primary: https://arxiv.org/abs/2608.19652

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合把‘用了旧状态’从一般回答错误中拆出来，尤其适合状态维护和依赖更新研究。它的核心价值在于错误类型可解释；若所有错误都汇总为不正确，就丢掉了这一设计相对普通问答的增量。

### 一个具体任务长什么样

示意任务：一个计划中的数值被修订，依赖该数值的后续安排也需要同步改变。系统检索到旧计划和新事件后，必须恢复当前有效状态，而不是只选择出现次数最多的描述。

### 最有判别力的实验

使用相同事件流，加入完整证据可见与正确当前状态给定的对照，分别统计旧状态错误和其他错误。改变修订依赖的深度时固定文本长度，从而区分依赖传播难度与长上下文干扰。

### 建议搭配

[longmemeval](longmemeval.md) · [membench-staleness](membench-staleness.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
