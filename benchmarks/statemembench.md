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
