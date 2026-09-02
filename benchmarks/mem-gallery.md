# Mem-Gallery：多模态 memory 不只是把图片 caption 化

**中文** | [English](mem-gallery.en.md) · [返回入口](../README.md) · [Benchmark Library](../library/README.md)

[论文](https://aclanthology.org/2026.acl-long.1892/) · [代码](https://github.com/YuanchenBei/Mem-Gallery)

## 它在测什么

Mem-Gallery 用 multi-session visual-text conversations，在统一框架下比较 12 个 memory systems，覆盖 memory extraction、test-time adaptation、reasoning、knowledge management 与 multimodal retention，并同时观察效率。

## 相比什么前进了

文本 memory benchmark 可以把图像压成 captions 后继续工作。Mem-Gallery 把 visual retention 和跨模态 reasoning 设为一等能力，使视觉细节在写入或压缩阶段丢失的代价能被观察。

## 分数边界

统一框架支持跨 memory system 的相对比较，但最终 QA/efficiency 仍受到 multimodal backbone、memory harness 与 judge 影响。高分说明 package 在该视觉对话 contract 下更好，不能直接证明某个 compression 或 retrieval component 因果更优。

## 公平比较条件

锁定 multimodal backbone、image encoding/compression、memory budget、answerer 与 judge，并分别报告 capability slices 和 efficiency。

## 下一步评测坐标

下一步应把 visual memory 接到真实环境 action，并验证细粒度 visual evidence 是否改变后续 tool choice 或 state update。
