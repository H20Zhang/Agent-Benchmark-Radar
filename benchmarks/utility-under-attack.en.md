# Utility Under Attack

- **Measurement object:** How much benign LongMemEval utility survives a small dose of plain false memories, and how much valid evidence is lost to screening or provenance ranking.
- **Closest predecessor:** MPBench establishes six persistent-poisoning classes; this work deepens its weakest false-fact class and makes retained utility, not ASR, primary.
- **Decisive evidence:** Poisoning 1.2% of the corpus drops accuracy from .850 to .300; write-time screening rejects 0/360 poisoned memories; stronger provenance weighting can recover some utility but drives recall of untrusted answer evidence to zero.
- **Score ceiling:** The result establishes a structural trade-off for content screening and additive provenance under the measured similarity regime, not failure of every defense.
- **Strongest confounder:** One memory stack, retriever, embedder, and reader; residual utility also depends on reader abstention.
- **Remaining gap:** Adaptive attacks, real provenance distributions, other stacks, and an implemented occupancy gate.
- **Genealogy:** It moves memory-attack evaluation from attack success to joint safety–utility measurement; `map_delta=reinforces`.

Primary: https://arxiv.org/abs/2608.21230

