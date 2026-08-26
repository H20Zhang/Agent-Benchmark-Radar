# RAG Collapse

- **测量对象：** 固定模型在递归检索循环中反复遇到自身生成的来源时，独立来源是否被逐轮挤出。
- **最近前身：** model collapse 研究递归训练；这里保持模型权重不变，把 feedback loop 移到 retrieval context。
- **决定性证据：** 1,528 次 simulation 中总体 collapse 率为 79.6%；Replace-All、Replace-One 与 Search 三类协议均出现高比例 collapse。
- **结论上限：** 证明 synthetic retrieval loop 可造成 self-source feedback，不证明 live web 已发生同样崩塌。
- **最强混淆：** 同一模型家族反复生成和读取、初始 prompt 多为单次运行、collapse/quality 依赖模型 judge。
- **未覆盖：** live-web longitudinal evidence、cross-model authorship、style/content 分离与人工标签。
- **谱系：** 把 corpus provenance 与反馈动态变成 RAG validity coordinate；`map_delta=reinforces`。

Primary: https://arxiv.org/abs/2608.22118

