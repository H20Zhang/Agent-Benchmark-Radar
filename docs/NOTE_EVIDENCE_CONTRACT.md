# Self-contained note evidence

Effective 2026-09-30, a revised paper explanation must let a reader understand its load-bearing evidence without opening the paper. The author must actually read the primary method, experimental settings, relevant results/ablations, and limitations; appendices and official implementations are required when they carry those conditions. An abstract, a previous summary, a table number, a stored score, or a passing validator is not evidence that this reading happened.

## Editorial requirements

- Explain the measured object and method through a concrete process or example, then identify the tested data/split, model, tools/harness, prompts or supplied information, budgets, grader, aggregation and exclusions that affect interpretation.
- When a conclusion depends on numbers, display a concise factual evidence table in both languages. Include the relevant comparison, metric/unit and experimental conditions; explain what the difference supports and its strongest alternative explanation. A table is not needed for a genuinely non-numerical protocol contribution, but the absence of verified empirical results must be explicit.
- Select facts needed for the explanation and reorganize them. Do not reproduce entire copyrighted tables/text unnecessarily or use a fixed number of tables as a quality target.
- Preserve source version, split, denominator, model and metric identity. Do not combine launch results with later revisions, full versus subset evaluation, or different budgets/readers. Unreported values remain unknown, not zero.
- Source discrepancies remain explicit until evidence resolves them. Never invent a rounding, version or experimental-setting explanation to make inconsistent values agree.
- Chinese and English express the same evidence and uncertainty in natural prose. Canonical model/method/dataset identifiers may remain unchanged; ordinary conceptual labels should be translated.
- Correct mistaken existing explanations directly. Adding a caveat after an unchanged wrong central claim is not a repair.
- Frozen historical title references remain a separate source-bounded surface. A new reading of v2/v3 does not silently replace a v1 historical reference.
- Primary-source availability is not experimental reproduction. Say precisely which text/protocol was inspected and what was not rerun.

## Recorded coverage

`data/note-evidence.json` records research-source coverage for accepted notes, not daily operations, candidate logs, or a certificate of truth. A reviewed entry includes:

- `status`: `full-text-reviewed`, `primary-protocol-reviewed`, `partial`, or `unavailable`;
- the actual review date, primary HTTPS source/version and inspected coverage;
- a visible bilingual reading-status statement and, for partial/unavailable coverage, the precise gap;
- method, setup and limitations evidence blocks, with author-chosen headings and organization;
- quantitative blocks only where warranted, identifying source location, visible conditions/metric units, and row-bound values;
- the hashes of the reviewed bilingual notes, so a later change requires a renewed assessment.

The records are editorial assertions supported by actual source inspection. Never manufacture them from headings, word counts, table counts or model output that has not been checked. Full-text status requires reading the paper itself; official-protocol status must not be presented as having read a paper. For a legacy accepted benchmark, unavailable full text may be disclosed honestly while preserving only supported claims. Partial/unavailable evidence cannot admit a new benchmark.

## Migration and backlog

The frozen `legacy_baseline` fingerprints the 147 bilingual pairs at commit `baa003e6b845a5facefe28828f260203c9029e5a`. An unchanged legacy note remains an explicit unreviewed backlog under this stronger standard. That status neither proves that no one ever read its source nor certifies that its current explanation is adequate.

Any new or modified note requires a coverage record. Do not change the baseline hashes to hide a missing review. Existing accepted identities remain in the registry while their explanations are repaired. The backlog is complete only when every pair has actually reviewed coverage and self-contained evidence, or a transparent, specifically unresolved source gap. A few repaired examples do not complete the archive.

## Mechanical guards and their limits

The existing `python scripts/validate_detail_pages.py` calls `note_evidence_contract.py`; all prior validators remain binding. Evidence blocks use paired `EVIDENCE:<id>:START/END` comments solely as stable boundaries. They do not force visible heading names or one essay template.

The checker verifies source/version records, declared coverage, displayed conditions/metric labels, explicit non-numerical gaps, row-bound bilingual numerical agreement, and reviewed-content hashes. Localized non-entity row labels may map to a shared identity. Real zero is valid; missing data is not converted to zero. A reference such as “Table 1” is allowed when the relevant evidence is present. Invisible comments cannot satisfy a displayed evidence requirement.

These checks cannot prove that someone read the paper, that a source is scientifically valid, that the chosen comparison is decisive, or that the interpretation is fair. Independent substantive review must check those questions. Passing structural depth grades or this contract must never be reported as factual certification.

Run the complete publication gate before creating a commit:

```bash
node scripts/render-readme.mjs
node scripts/render-readme.mjs --check
python -m unittest discover -s tests -v
python scripts/validate_reading.py
python scripts/validate_detail_pages.py
python scripts/audit_detail_pages.py
git diff --check
```

Publish each accepted repair batch atomically with both languages, its coverage records, any corrected source-bounded historical references, and affected canonical/derived surfaces. Preserve discovery/citation timestamps unless the corresponding work was actually performed. The website remains retired.
