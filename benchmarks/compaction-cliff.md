# The Compaction Cliff

## 它到底测什么

The Compaction Cliff 测的是 **安全约束在有限上下文管理过程中的存活率**。当 agent 反复做压缩、分解或检索时，原本明确的规则能否被完整保留，并继续约束后续行动。它把“记忆有没有保留信息”拆成更严格的问题：不同类型的信息是否需要不同 retention contract，尤其是不能被近似摘要掉的 safety constraints。

## 相比前身多测了什么

MaRS 等工作引入 typed memory，但常用统一效用指标；LLMLingua-2 与生产 compactor 更关注压缩质量/长度，通常不会把 constraint preservation 当作单独 hard metric。本工作把 exact constraint preservation 扩展到 compact、decompose、retrieve 三类 context-management operator，因此能直接比较不同状态管理策略对安全规则的破坏方式。

## 决定性证据

Sonnet `/compact` 的约束保留率在五轮后从 **0.53 降到 0.10**；TypeCompact 稳定在 **0.96**。TypeDecompose 报告 **0% locality violation**，TypeRetrieve 的 **recall@50 为 100%**。这组结果最重要的含义是：统一语义压缩即使“总体信息还像”，也可能系统性丢掉不可软化的 constraint，而 typed operator 可以显著改善所测协议中的保留。

## 这个分数支持什么判断

结果支持“在论文设置下，typed retention 更能保留安全约束”。它不支持“所有长期 agent 因此更安全”，因为行为实验没有严格 token-match，TypeCompact 往往保留更多上下文，而且整体安全保证仍依赖前置 classifier 正确识别哪些信息属于 constraint。

## 公平比较条件

必须固定原始 context、constraint set、压缩轮数、token budget、模型、classifier、retrieval k 与后续行为任务。若一个方法允许保留显著更多 token，就应该报告 **constraint retention vs. retained-token budget**，而不是只比较 retention rate。typed 方法还应单独报告 classifier false negative，因为漏标的约束不会进入受保护路径。

## 研究上怎么用

这个 benchmark 很适合研究 agent memory/context compression 的 **information-type-aware policy**。如果一个方法声称可以安全压缩 long-running agent state，应把 factual recall、preference retention、procedural state 与 hard constraints 分开测量；否则平均 semantic similarity 会掩盖少量但高影响的规则丢失。

## 下一步最有价值的验证

当前缺口是在线约束识别、企业/真实交互分布、跨 agent 共享记忆，以及严格 token-matched behavior。最高杠杆实验是把 TypeCompact 与通用 compactor 放在相同 token budget 下，使用未见 constraint 类型和真实后续 actions，验证 retention 提升是否仍能转化为更低的行为违规率。

## 谱系位置

它与 MPBench、InjecMEM、Utility Under Attack 一起把 memory safety 拆到写入、检索、压缩等生命周期阶段；`map_delta=reinforces`。它增加的关键坐标是 **retention policy must depend on information type**，而不只是“压缩后 QA 还答不答得出来”。

Primary: https://arxiv.org/abs/2608.22752
