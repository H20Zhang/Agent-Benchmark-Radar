# MPBench

## 测量对象

MPBench 测的是 **persistent-memory poisoning 的完整跨会话链路**：六类恶意内容通过四种写入渠道进入持久记忆后，系统是否会把它们真正写入；之后在另一次会话中出现相关查询时，恶意记录是否会被检索并影响输出。关键点是把攻击拆成 `write → persist → retrieve → respond`，而不是只看一次 prompt injection 是否即时劫持 agent。

## 相比前身多测了什么

LoCoMo / LongMemEval 主要测良性 memory fidelity；AgentDojo / InjecAgent 更偏同会话 hijacking。MPBench 将写入阶段与未来触发阶段分离，因此能区分“恶意内容能进入 store”与“它后来真的能被相关查询重新激活”两个失败面。这也是为什么 ASR 和 conditional RSR 需要同时看。

## 决定性证据

公开结果中，OpenClaw 的平均 **ASR / conditional RSR 为 34.25% / 17.40%**，HERMES 为 **66.67% / 64.70%**。PromptArmor 在 **1% FPR** 下的最佳 TPR 只有 **67.67%**。这些数字说明风险不只存在于写入：对部分系统，恶意记忆一旦留下，后续 retrieval 仍有很高机会把它重新暴露给 agent。

## 这个分数支持什么判断

MPBench 的 headline score 描述的是 **system + harness 的 persistent-poisoning exposure**。它不能单独回答“基础模型是否容易被毒化”或“某个 memory retriever 是否有漏洞”，因为两个 agent 的写入、存储和检索策略不同，部分攻击渠道还依赖静态标注上下文。

## 公平比较条件

- 固定 backbone、写入渠道与 memory admission policy。
- 对齐 retrieval top-k / ranking、触发查询与攻击预算。
- 使用相同 evaluator，并同时报告 security 与 benign utility；只降低 RSR 但大量拒绝正常写入，并不构成更好的 memory system。

## 研究上怎么用

如果一个 memory 方法声称“长期安全”或“能抵御 prompt injection”，MPBench 适合验证其持久化攻击面，但它最好与正常 utility benchmark 配对。尤其值得分开报告：write acceptance、retrieval exposure、conditional ASR 和 end-to-end joint success，这样才能定位防御到底卡在哪个生命周期阶段。

## 下一步最有价值的验证

当前最关键的缺口是更多 backbone、完全可执行的 delivery channel、自然 memory drift，以及 security–utility 曲线。最有判别力的实验是让不同 memory store 在相同 backbone、相同攻击和相同 utility workload 下比较，而不是把两个完整 agent 产品直接横比。

## 谱系位置

MPBench 补上了 memory safety 从良性 fidelity 到 persistent poisoning 的关键过渡；`map_delta=splits`。它把“记忆是否正确”拆成新的安全坐标：**记忆能否被恶意写入，以及未来是否会被重新激活。**

Primary: https://arxiv.org/abs/2606.04329

<!-- RESEARCH-DECISION:START -->

## 研究决策卡

### 什么时候值得用

适合研究不同写入渠道中的跨会话记忆污染。它与同一会话的提示注入不同，必须先证明内容进入持久记忆，再观察后续任务；渠道和写入策略不同的系统不应被直接解释为模型安全性差异。

### 一个具体任务长什么样

示意任务：外部上下文或工具反馈进入写入会话，查询会话则重新启动并处理正常任务。记录在后一个会话中再次出现，才说明影响跨越了会话边界；同一上下文的延续不能替代这个控制。

### 最有判别力的实验

对不同渠道采用相同内容与预算，分别统计写入接受、后续检索和最终偏移，并增加持久记忆关闭条件。正常任务效用必须和安全指标一起报告，才能分清安全写入策略与不使用记忆造成的表面优势。

### 建议搭配

[injecmem](injecmem.md) · [gatemem](gatemem.md)

> **读分数的原则：** 先对齐 task / split、模型与 harness、工具与环境版本、资源预算、停止与重试规则以及 evaluator。协议不同的总分首先是系统级证据；没有 matched intervention / ablation 时，不把差异直接归因给单个组件。

<!-- RESEARCH-DECISION:END -->
