# KBGym / Training a Knowledge Base

- **Measurement object:** Whether a persistent store edited by a supervised curator lets an independent reader answer trained and coverage-stratified unseen questions with fewer actions after the store is frozen.
- **Closest predecessor:** HippoRAG-style offline structuring indexes the whole corpus without supervision; this work treats `(question, answer)` pairs as training labels and measures structural coverage.
- **Decisive evidence:** v2 corrects trained-question performance to 25% action saving and +.294 F1; unseen both-key questions gain +.176, one-key +.059, and neither-key questions gain nothing.
- **Score ceiling:** Gains are coverage-conditioned; only 27.6% of the corpus is covered, so the result does not establish general store improvement.
- **Strongest confounder:** One seed, the same curator/reader model family, synthetic atomic documents, and adapted baselines.
- **Remaining gap:** Cross-model transfer, multiple seeds, natural corpora, and online/prequential evaluation.
- **Genealogy:** It turns the corpus from a static input into trainable, freeze-auditable state; `map_delta=early_signal`.

Primary: https://arxiv.org/abs/2608.21829

