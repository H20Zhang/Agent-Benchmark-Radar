# CUE-Mem：从反复出现的背景线索形成记忆

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-09-26<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2609.32574v1)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

**中文** · [English](cue-mem.en.md) · [基准库](../library/README.md)

<!-- EVIDENCE:reading:START -->
## 阅读范围
已阅读全文第1–6节与附录A–G，核对方法、设置、关键结果及局限；未独立复现实验。
[arXiv:2609.32574v1](https://arxiv.org/html/2609.32574v1)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:method:START -->
## 测量对象与前身
与 Mem-Gallery、MemLens 的多模态历史相比，CUE-Mem 把反复出现在背景中的物体与环境声音作为记忆证据，例如多段语音背后的猫叫。合成用户档案经脚本、媒体生成及人工检查形成历史，再以四选一问题测回忆、长期规律、个性化推荐和拒答。20名合成用户、648个会话共有2674题；显式与隐式条件并非一一配对。
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## 公平比较条件
基准使用中文合成历史。默认使用 GPT-5.4 的 Medium 图像描述和 Gemini 3.1 Pro 的 Hint 声音描述。RQ1/RQ2 为温度0、输出上限1024词元；全局种子42仅对兼容Qwen的API传入，Qwen关闭思考。两个受测骨干各进行三次无历史答题，六次全对才过滤该非拒答题。Full Memory 也有4096词的回忆上限。表2的记忆均分按三个非拒答任务等权平均，不能把全部题数作为每个隐式单元格的分母。
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## 关键结果及解释边界
表2；隐式 Memory Avg.，准确率百分比，三个非拒答任务的宏平均；同一骨干内比较。Oracle 直接提供合成线索的源文本。

| 骨干 | 最强非Oracle方法 | 非Oracle（%） | Oracle（%） |
|---|---|---|---|
| Qwen3.6-35B-A3B | MemGPT | 38.5 | 80.8 |
| GPT-5.4-mini | Reflexion | 41.9 | 78.4 |

来源：[表2、附录C–D](https://arxiv.org/html/2609.32574v1)。差距同时包含表征、检索与使用证据的影响，不能归因于记忆策略一项。图5还显示更细描述带来额外输入成本；其与附录D.2成本统计的对应口径尚未核实，不拼接比较。尚未建立可跨实现比较的标准化结果轨道。
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:limitations:START -->
## 最强混杂与下一步
声音 Split 直接使用干净的合成背景音轨，不是对混合录音完成源分离；图像描述干预也改变选项描述。三次运行的显著性审计仅覆盖五个固定用户，不能称全部结果均为三次均值。合成、四选一和模型参与筛题限制外推；还没有覆盖偏好变化、矛盾修复与遗忘。下一步应配平输入及选项表征，在真实混合声音和未见用户上验证。

谱系上，这是背景线索记忆的早期信号，不足以改写整个领域的长期结论。[官方实现](https://github.com/yulinlp/CUE-MEM)与[数据](https://huggingface.co/datasets/Kkryptonite/CUE-Mem)已定位；示例配置不保证复现论文设置。
<!-- EVIDENCE:limitations:END -->
