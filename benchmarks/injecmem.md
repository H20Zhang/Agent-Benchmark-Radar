# InjecMEM

## 它到底测什么

InjecMEM 测的是 **targeted persistent-memory injection**：攻击者只通过一次看似普通的交互把恶意记录写进持久记忆；在之后的独立会话里，当出现与该 topic 相关的查询时，系统是否会把这条记录重新检索出来，并进一步生成攻击者预设的目标内容。测量对象因此覆盖 `write → memory drift/persistence → retrieve → generate` 的完整轨迹。

## 相比前身多测了什么

AgentPoison / MINJA 更偏攻击方法本身，MPBench 则给出更宽的 persistent-poisoning taxonomy。InjecMEM 的增量是把问题收窄到 **topic-conditioned targeted generation**，并显式区分 retrieval success、在成功检索条件下的 attack success，以及最终 joint success。这样可以看到攻击失败究竟发生在 store/retrieval 还是 generation 阶段。

## 决定性证据

Multi-GCG 在 MemoryOS 上报告 **46.5% RSR、76.6% conditional ASR、35.6% joint ASR**；多个通用 filter 几乎不降低 conditional ASR。这个组合比只看 ASR 更重要：它表明一旦恶意记录被检索，generation 端仍可能高概率服从攻击目标，而整体攻击率还受到 retrieval exposure 的限制。

## 这个分数支持什么判断

结果支持“在所测 memory stack 与白盒优化条件下，攻击可以穿过持久化、检索与生成链路”。它不支持对未见模型家族的通用黑盒迁移结论，也不能直接归因给 MemoryOS 的某一个内部组件，因为最强攻击需要 backbone 白盒访问和 fused prompt 知识。

## 公平比较条件

比较攻击或防御时，应固定 backbone、memory write policy、store/rewrite mechanism、retrieval top-k、trigger query、攻击 token/optimization budget 与 generation prompt。RSR、conditional ASR 和 joint ASR 必须一起报告，否则可能把“防御只是让攻击更难被检索”误读成“模型生成端已变安全”。

## 研究上怎么用

InjecMEM 适合检验声称具备 memory security 的系统是否只在 write-time 做过滤，还是能够在生命周期后段继续控制风险。对于新的 memory architecture，最有信息量的 ablation 是分别替换 admission、rewrite/consolidation、retrieval 与 generation defense，观察哪一阶段真正降低 joint success，同时保留 benign retrieval utility。

## 下一步最有价值的验证

当前缺口是 rewrite-heavy store、真实部署、adaptive defense，以及完整的 security–utility curve。最有判别力的下一步是测试攻击在不同 backbone、不同 memory rewrite policy 和黑盒访问条件下是否仍能保持高 conditional ASR，而不是继续只优化同一个白盒攻击目标。

## 谱系位置

它把 memory security 从“恶意内容是否能写进去”推进到 **write → drift → retrieve → generate** 的端到端轨迹；`map_delta=reinforces`。与 MPBench 配合时，MPBench 提供宽攻击面，InjecMEM 提供更细的 targeted-generation attribution。

Primary: https://arxiv.org/abs/2608.23471

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合诊断一次低权限交互如何通过持久记忆影响后续回答。写入成功、被检索到和最终行为被改变是不同事件；只报告被检索之后的条件攻击成功率，会高估真实端到端风险。

### 一个具体任务长什么样

示意任务：一条外来记录试图把来源中的指令混入长期记忆，之后正常查询再次触发它。防御需要维持内容与指令的信任边界，同时不能阻止合法事实被正常写入和调用。

### 最有判别力的实验

分别记录写入、检索、条件行为偏移与联合成功率，并对同一防御报告正常任务阻断。更换写入模型、回答模型和摘要策略检验迁移，避免把白盒优化下的一组结果当作所有部署的风险上界。

### 建议搭配

[mpbench](mpbench.md) · [utility-under-attack](utility-under-attack.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
