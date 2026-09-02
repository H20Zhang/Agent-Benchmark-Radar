# LifeSide: long-term user understanding is not the same as factual recall

[中文](lifeside.md) | **English** · [Home](../README.en.md) · [Benchmark Library](../library/README.en.md)

## What it measures

LifeSide scales personal-memory evaluation to 2,000 personas and roughly 111K tasks spanning memory tracking, user understanding, privacy control, and emotional companionship. The target is not only what a user said before, but whether a system forms an appropriate, bounded user model and uses it well over long interaction histories.

## Compared with what

LoCoMo and LongMemEval primarily emphasize conversational facts and reasoning. LifeSide adds persistent user understanding, privacy, and companionship, directly challenging the assumption that saturation on existing memory QA means personalized memory is solved.

## Decisive evidence and score boundary

The work reports that models which saturate prior memory benchmarks still fail substantially on long-horizon user understanding and companionship. This supports a benchmark-coverage gap, not a causal claim that one memory architecture is responsible; backbone capability, persona construction, and the judge all matter.

## Fair comparison conditions

Align persona/history generation, privacy policy, answerer, and judge, and inspect task families separately. Collapsing factual recall with emotional or privacy behavior into one number hides the capability structure.

## Next evaluation coordinate

The next step connects long-term user models to real permissions, deletion, tool-mediated actions, and externally observable consequences of incorrect personalization.
