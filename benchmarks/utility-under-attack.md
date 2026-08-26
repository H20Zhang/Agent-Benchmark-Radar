# Utility Under Attack

- **测量对象：** 少量普通虚假陈述进入持久记忆后，良性 LongMemEval utility 会损失多少，筛查和 provenance ranking 又会牺牲多少正常证据。
- **最近前身：** MPBench 建立六类 persistent poisoning；本工作深入其中最弱的 false-fact 类，并把 retained utility 而非 ASR 设为主结果。
- **决定性证据：** 1.2% 语料被投毒时 accuracy 从 .850 降到 .300；write-time pipeline 拒绝 0/360 条毒记忆；强 provenance 权重虽可恢复部分结果，却把 untrusted answer evidence 的 recall 降为 0。
- **结论上限：** 支持 content-only screening 与 additive provenance 在该相似度分布下存在结构性 trade-off，不证明所有防御都失败。
- **最强混淆：** 单一 memory stack、retriever、embedder 与 reader；残余 utility 也受 reader abstention 影响。
- **未覆盖：** 自适应攻击、真实 provenance 分布、其他 memory stack 与 proposed occupancy gate。
- **谱系：** 把 memory attack 评价从攻击成功率推进到安全—效用共同测量；`map_delta=reinforces`。

Primary: https://arxiv.org/abs/2608.21230

