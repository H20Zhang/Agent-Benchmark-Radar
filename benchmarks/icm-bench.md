# ICM-Bench

<!-- RELEASE-REFERENCE:START -->
> **发布时最佳结果（待核验）** · 基准记录日期：2026-09-03<br>
> 尚未核验原始发布版本中可定位到模型、指标和协议的最佳成绩。 [原始来源](https://arxiv.org/abs/2609.04438)<br>
> 不以最新榜单、单条基线或后续论文成绩代替；未知不代表零分或原作者未报告。
<!-- RELEASE-REFERENCE:END -->

## 测量对象

在合成多模态生活相册中，测围绕同一人物的记忆召回、跨片段身份关联与长期画像推断。

## 相比前身改变了什么

相较一般多模态召回，将长期时间线上的重复人物关联及画像证据单独考察。

## 协议与比较条件

Recall/Retrieval 只使用 before_clip 及以前的视频，Profile 使用完整时间线；视频设置共用校准片段。人物 ID、证据和带说话人标签的转录属于评测端资源，不应泄露给回答器。

## 决定性证据与结论上限

官方公开视频生成及 M3-Agent、Vgent、HippoRAG2 适配，但明确没有发布直接 caption-memory 基线实现。这限制了对该重要比较的直接复现。

## 最强混淆与限制

不同系统的视频采样、转录、描述与回答器配置不同，总分差不能直接归因于记忆架构；额外的小型生成试验也不是第二个评测领域。

## 未覆盖与下一步实验

单组合成人物，尚不覆盖真实人群差异、长期外观变化及记忆驱动的后续行动。

固定感知前端与回答模型，对比完整描述历史和显式人物—事件关系；再做身份置换及证据移除，确保不暴露标准标签。

## 谱系与使用建议

[MemEye](memeye.md) · [Mem-Gallery](mem-gallery.md) · [LifeSide](lifeside.md)

本条为 `early_signal`：接受一个有用的测量对象，不据单篇结果改写长期稳定的领域地图。

## 一手来源与版本

[论文](https://arxiv.org/abs/2609.04438) · [已核全文](https://arxiv.org/html/2609.04438v2)

[code](https://github.com/Shidu-Ren/ICM-Bench)

[data](https://huggingface.co/datasets/ryanren0330/ICM-Bench)

首发：**2026-09-03**；核验：**2026-09-17**。首发日期与本次收录日期分开。

[English](icm-bench.en.md) · [返回完整索引](../library/README.md)
