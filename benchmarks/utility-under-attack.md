# Utility Under Attack

## 它到底测什么

Utility Under Attack 把 memory security 的问题从“攻击能不能成功”改成 **少量恶意记忆进入系统后，正常长期记忆 utility 会损失多少，以及防御为了阻止攻击会误伤多少正常证据**。它使用 LongMemEval 风格的良性任务，把 false-fact poisoning、write-time filtering 与 provenance-based retrieval 放进同一个 security–utility contract。

## 相比前身多测了什么

MPBench 建立了 persistent poisoning 的宽攻击 taxonomy，但主要关注攻击暴露与成功率。这个工作深入其中相对简单的 false-fact 类，将 **retained benign utility** 设为主结果，因此可以识别两类此前容易被掩盖的失败：攻击成功率不高但 utility 已大幅下降，以及防御降低攻击的同时也让正常答案不可达。

## 决定性证据

在仅 **1.2% 语料被投毒**时，accuracy 从 **0.850 降到 0.300**。所测 write-time pipeline 对 **360 条毒记忆拒绝 0 条**；强 provenance 权重可以恢复部分结果，但会把 untrusted answer evidence 的 recall 降到 **0**。这说明 content-only screening 与简单 additive provenance 在该相似度分布下存在明显 structural trade-off。

## 这个分数支持什么判断

结果支持“在这套 memory stack、retriever、embedder 与 reader 下，少量 false fact 足以造成显著 utility degradation，且所测简单防御存在安全—效用冲突”。它不支持“所有防御都失败”，也不能把残余 utility 单纯归因于 retrieval，因为 reader 的 abstention 行为同样影响最终 accuracy。

## 公平比较条件

需要固定 memory stack、embedder、retrieval top-k、reader、attack rate、poison similarity distribution 和 provenance prior。任何防御都应该同时报告 poisoned-record exposure、benign recall、answer accuracy 与 abstention，而不能只给 attack rejection rate。若 provenance 来源质量分布不同，ranking 权重也不再可直接比较。

## 研究上怎么用

这个 benchmark 很适合检验新的 memory defense 是否只是“更激进地拒绝信息”。对于 admission filter、provenance ranking、conflict resolution、memory consolidation 等方法，应画出 **security–utility frontier**，并说明提升来自减少 poison exposure、保留可信 evidence，还是让 reader 更会 abstain。

## 下一步最有价值的验证

当前缺口是自适应攻击、真实 provenance 分布、更多 memory stack，以及作者提出的 occupancy gate。最高杠杆的下一步不是再添加一个静态 filter，而是比较不同 defense 在相同 benign workload 和 adaptive attacker 下的 Pareto frontier，验证是否存在真正支配 baseline 的方法。

## 谱系位置

它把 memory attack 评价从攻击成功率推进到安全—效用共同测量；`map_delta=reinforces`。与 MPBench / InjecMEM 配合，它让 memory security 开始覆盖 **write exposure、retrieval exposure、generation success 和 benign utility** 四个不同坐标。

Primary: https://arxiv.org/abs/2608.21230
