# SciValidityBench: 记忆使用的科学约束

<!-- RELEASE-REFERENCE:START -->
> **发布时诊断结果（历史参考）** · 首版：2026-10-26<br>
> **Qwen3-14B / Flat SSG — Scientific-use-valid decision rate: 0.991**；**Qwen3-14B / SVL — Scientific-use-valid decision rate: 0.981**<br>
> 表3，Qwen3-14B，温度0；64个TaskSpec各10个seed的科学有效决策率，按TaskSpec等权。非跨系统最佳声明。 [原始来源](https://arxiv.org/html/2610.34767v1)<br>
> 短合成历史与确定性编译状态；不能推导图序列化普遍更优或真实科学长程记忆能力。
<!-- RELEASE-REFERENCE:END -->

**中文** · [English](scivaliditybench.en.md) · [Library](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围
已阅读正文及附录A–I中的协议、控制、结果与限制，并核对官方仓库文件清单；未复现实验，也未独立检查图表像素。
[arXiv:2610.34767v1](https://arxiv.org/html/2610.34767v1) · [Official code](https://github.com/SciValidityBench/SciValidityBench)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象改变在哪里
记住的事实可以完全正确，却不适合用于当前决策。SciValidityBench 将预注册、选择偏差、停止规则、构念定义、有信息的缺失与沉没成本显式化。五个模块包含24个 Inferential Ledger、8个 Blind Memory、12个 Construct Drift、12个 Absence Algebra 与8个 Sunk Cost TaskSpec，覆盖六种合成科学领域。相较 MemCalib 与 The Memory Trust Gap，它新增可执行的科学使用约束，而非再做一次召回测试；这是早期诊断信号，不据此改写长期地图。

TaskSpec 定义世界生成器、确定性状态编译器、合法动作、oracle 与干预。SciStateForge 从公开事件推导 Selected_From、Stopped_After、Sealed_Until 等关系；Flat SSG 与 typed SVL 提供相同派生状态。reader 看不到隐藏oracle，但编译器与oracle共享人工设计的任务本体。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 协议与公平比较
640个world共1,920条公开事件，是短结构化历史，不是长上下文压力测试。主比较有12,800次原始决策及5,120次配对伴随决策；六个矩阵共68,320次决策不等于独立world数。对比Raw全历史、BM25 top-5块、通用事件图、Flat SSG与typed SVL，reader为Qwen3-14B、Gemma-3-12B-IT、Mistral-7B-Instruct-v0.3、Phi-3.5-mini-instruct。

程序依据TaskSpec oracle判断动作在当前科学状态下是否有效，不使用LLM judge。无效JSON、拒绝、非法或无法解析动作均判错，不按结果重试。先在TaskSpec内汇总seed配对差，再对64项等权平均；置信区间用20,000次TaskSpec bootstrap。反事实翻转/不变性与两次均正确必须分开，一贯选错也可能满足关系条件。破坏及精确逆修复与等大小无关修复比较。官方仓库含生成器、编译器、reader接口、破坏操作、评分与测试；本轮只核可用性，未运行。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 选取的主要证据
表3：四个固定reader，温度0，各比较内请求及有限合法动作相同；64个TaskSpec各10个seed，按TaskSpec等权汇总科学有效决策率。

| Reader | Raw科学有效决策率 | Event Graph科学有效决策率 | Flat SSG科学有效决策率 | SVL科学有效决策率 |
|---|---|---|---|---|
| Qwen3-14B | 0.798 | 0.794 | 0.991 | 0.981 |
| Gemma-3-12B-IT | 0.733 | 0.719 | 0.903 | 0.902 |
| Mistral-7B-Instruct-v0.3 | 0.556 | 0.566 | 0.692 | 0.678 |
| Phi-3.5-mini-instruct | 0.480 | 0.478 | 0.609 | 0.570 |

[表3；附录D/G/I](https://arxiv.org/html/2610.34767v1)。主表每行Flat SSG都高于typed SVL，不能写成图结构普遍更优。另一组按任务族平衡、匹配token的源事实控制中，Flat减matched source对Qwen为+0.194、Mistral为+0.193、Gemma为+0.011（区间跨零）、Phi为−0.295；这是不同子集和控制，不能替换主表。去掉状态值与动作字面重叠的22项后，余下42项的SVL–Event Graph差仍为正，但并未排除更广泛的合成模板捷径。
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 边界与下一坐标
编译器提前算出决策所需关系，测的是状态编译加阅读，而非自主实验室中的学习型记忆写入/检索。有限动作、短历史、合成世界与共享任务本体限制泛化。更显式的状态在Sunk Cost上也会伤害Qwen/Gemma，精确修复并非对所有reader有效；单格接近满分不等于科学推理饱和或真实世界有效性保证。

下一步应使用独立生成的长历史、未见科学流程、带误差核算的学习型编译器，并匹配各表示中的事实、token与接口。保留reader特异退化和反事实两次均正确指标。最稳妥结论是科学使用约束可被受控测量，而非图记忆普遍最好。
<!-- EVIDENCE:limitations:END -->
