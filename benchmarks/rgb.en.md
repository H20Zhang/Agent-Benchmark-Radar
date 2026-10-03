# RGB: decomposing how a generator uses retrieved context into four failure modes

<!-- RELEASE-REFERENCE:START -->
> **Best at release (not yet verified)** · Benchmark recorded date: 2023-09<br>
> A best result tied to a model, metric, and protocol in the initial release has not yet been verified. [Original source](https://arxiv.org/abs/2309.01431)<br>
> No substitution from a live board, a single baseline, or a later paper; unknown is neither zero nor a claim that the authors reported no results.
<!-- RELEASE-REFERENCE:END -->

[中文](rgb.md) | **English** · [Benchmark Library](../library/README.en.md)

<!-- EVIDENCE:reading:START -->
## Reading scope and version

Reviewed the stated primary paper in full for methods, experimental setup, results and limitations; no independent reproduction.

all main sections, construction, evaluation, error analyses, conclusion; no separate appendix in this PDF; Tables 1–7; Tables 5,7 visually verified

[v1,2023-09-04](https://arxiv.org/pdf/2309.01431v1)

Additional release-evaluator inspection: [d2293eec8c76467c1572b3ebedcaca4e9b4e82f4](https://github.com/chen700564/RGB/blob/d2293eec8c76467c1572b3ebedcaca4e9b4e82f4/evalue.py)
<!-- EVIDENCE:reading:END -->

<!-- EVIDENCE:placement:START -->
## What changes relative to nearby evaluations

The following is an editorial protocol comparison, not an assertion of direct inheritance unless stated.

Unlike primarily ranking-focused retrieval benchmarks, RGB manipulates supplied context to diagnose generator evidence use. It provides axes for abstention, conflict and integration evaluation without measuring a real search process.
<!-- EVIDENCE:placement:END -->

<!-- EVIDENCE:method:START -->
## Task and evidence construction

Human-checked news questions retrieve ten Google pages, split into≤300-token passages and reranked. A nominal five-document setting controls noise, answer absence, integration and counterfactuals; the target is generator evidence use.
<!-- EVIDENCE:method:END -->

<!-- EVIDENCE:setup:START -->
## Conditions needed to interpret the results

Base questions number 300 per language; integration and counterfactual tests each use 100 per language. ChatGPT means gpt-3.5-turbo without a specified dated snapshot. Accuracy uses answer-substring matching and does not establish that the whole response is contradiction-free. Rej checks a designated refusal string; Rej* uses ChatGPT for semantic refusal judgments. Counterfactual testing includes only models above 70% closed-book accuracy and explicitly warns them about erroneous documents.
<!-- EVIDENCE:setup:END -->

<!-- EVIDENCE:result-1:START -->
## ChatGPT evidence-use diagnostics

ChatGPT percentages; declared testbeds: noise/rejection 300 per language, integration/counterfactual 100 per language; scored-denominator logs unavailable. Noise ratios are nominal; accuracy uses substring matching, Rej a specified string, Rej* semantic judgment.

| Measure/condition | English | Chinese |
|---|---|---|
| Noise 0 accuracy | 96.33 | 95.67 |
| Noise.8 accuracy | 76.0 | 70.67 |
| Integration noise 0 accuracy | 55 | 63 |
| Integration noise.4 accuracy | 34 | 47 |
| Only-noise Rej | 24.67 | 5.33 |
| Only-noise Rej* | 45 | 43.33 |
| Counterfactual closed-book accuracy | 89 | 91 |
| Counterfactual documents accuracy | 9 | 17 |

Source: Tables 1,3,5,7 · [Paper](https://arxiv.org/pdf/2309.01431v1)
<!-- EVIDENCE:result-1:END -->

<!-- EVIDENCE:interpretation:START -->
## What the comparisons establish

Low exact rejection mixes evidence failure with formatting; retain Rej/Rej*. Counterfactual tasks select known facts and do not generalize directly to unfamiliar knowledge.
<!-- EVIDENCE:interpretation:END -->

<!-- EVIDENCE:limitations:START -->
## Limits, source discrepancies and next test

Prompts explicitly warn about errors; substring hits can coexist with contradictions. Next: independently audit answers, abstention and repair in real retrieval trajectories.

No material selected-cell conflict. Counterfactual correction-rate denominator is insufficiently explicit; omitted from table rather than guessed.

The [release evaluator](https://github.com/chen700564/RGB/blob/d2293eec8c76467c1572b3ebedcaca4e9b4e82f4/evalue.py) adjusts passage composition when candidates are insufficient and skips exceptions: 300 is the declared testbed size, with no published exclusion log. Noise ratios are nominal. Decoding settings remain unknown; code defaults and example commands differ.
<!-- EVIDENCE:limitations:END -->

Related benchmarks: [ragtruth](ragtruth.en.md) · [lit-ragbench](lit-ragbench.en.md)
