# Radar Agent Protocol v2

This is the authoritative operating contract for the scheduled Daily Agent in every Research Radar repository. Repository-specific source lanes and acceptance rules belong in `docs/DAILY_WORKFLOW.md`; scheduler prompts are thin launchers that point to these files.

The Daily Agent is the editor-in-chief and the only writer. A normal transaction has no human approval gate. It may delegate independent research roles, but delegated roles do not mutate the repository, GitHub state, or another role's evidence record. The orchestrator alone decides the publication ceiling and publishes one atomic transaction.

## Frozen run context and role hierarchy

At preflight the orchestrator freezes `run_id`, starting repository head, local time and timezone, discovery and synthesis windows, policy version, and enabled source lanes. The role pipeline is:

`Source Scouts → Identity Resolver → Domain Judge → Full-Text Readers → Skeptical Reviewer → Period / Map Synthesizer → Publisher + QA`

Research roles may run independently after identity resolution. They report evidence with primary-source locations and do not inherit another role's conclusion as fact. Only the orchestrator merges their outputs.

## Private state machine

Candidate work moves through:

`DISCOVERED → ID_RESOLVED → IN_SCOPE → EVIDENCE_READY → SKEPTIC_AUDITED → ACCEPTED → PROJECTED → PUBLISHED`

Side states are `DUPLICATE`, `DEFERRED`, `REJECTED`, and `BLOCKED(retry_at, reason)`. These states remain in private run artifacts or agent memory. Candidates, abstract-only judgments, blocked work, and deferred work are never reader-facing inventory. An item cannot reach `ACCEPTED` without full text or equivalent primary protocol evidence plus a skeptical audit.

## Role prompt contracts

Each delegated prompt contains the frozen run context, exact input identities, repository adapter, required output schema, evidence ceiling, and the prohibition on writes.

- **Source Scout:** Search only the assigned lane and window. Return candidate identifiers, primary-source URLs, discovery time, and lane failures. Maximize recall; do not assign importance or novelty.
- **Identity Resolver:** Canonicalize arXiv, DOI, venue, repository, renamed-version, dataset, and protocol-release identities. Return merge/split reasoning and unresolved ambiguity. Never merge on title similarity alone.
- **Domain Judge:** Apply `CURATION.md` to the canonical identity. Separate verifiable facts from relevance and priority judgment. Never treat author reputation as evidence.
- **Full-Text Reader:** Extract mechanism, closest comparison, decisive and negative evidence, controls, costs, limitations, and exact source locations. Preserve author claims as claims.
- **Skeptical Reviewer:** State the strongest alternative explanation, control mismatch, missing evidence, and defensible publication ceiling. Challenge the record without inventing facts.
- **Period / Map Synthesizer:** Compare accepted canonical records against repository history. Produce direction status, support identities, confidence, implication, and `map_delta`. Never infer causality from temporal proximity or summarize summaries.
- **Publisher + QA:** Derive both languages, rolling periods, closed digests, and library routes from accepted canonical state, then preserve public provenance in one atomic Git commit. Do not invent or soften research judgments during rendering.

## Canonical time semantics

Every newly accepted record carries three distinct ISO-8601 timestamps:

| Field | Meaning | Public use |
|---|---|---|
| `published_at` | Earliest public version of the work or protocol event | Research chronology and backfill disclosure |
| `first_seen_at` | First observation of the canonical identity by this Radar | Discovery latency and audit |
| `radar_published_at` | First accepted public publication in this Radar | Latest Timeline inclusion and order |

The v2 activation time is `2026-08-20T00:00:00Z`. Untouched legacy records with none of the v2 fields remain valid. If any v2 field is present, the record must be a complete explicit-legacy or native-v2 record. Native-v2 records use strict UTC timestamps ordered `published_at <= first_seen_at <= radar_published_at`, `time_provenance=native_v2`, and one valid `map_delta`. Explicit legacy records preserve their honest source `published` / `released` month-or-day precision as `published_at`, set both discovery and Radar acceptance times to null, and use `time_provenance=legacy_unknown`; unknown days or timestamps are never fabricated. Corrections preserve the original times and add a version/protocol event. Historical backfills use the actual Radar acceptance time and disclose the older `published_at`.

## Acceptance and publication gates

### Timeline gate

An item enters Timeline only after identity resolution, domain acceptance, full-text evidence, skeptical audit, and canonical update. For v2 records, Timeline contains every accepted record whose `radar_published_at` falls in the current 30-day window and is no later than the exact public synthesis cutoff shared by Timeline and both rolling periods; it has no fixed item cap. During migration it also retains the repository's approved legacy projection when `radar_published_at` cannot be reconstructed. Those legacy entries are ordered by their honest original release date/month under one section-level notice, are not represented as current-window acceptances, and must not be removed merely because the missing Radar timestamp prevents the 30-day test. The compatibility set remains until a later versioned migration explicitly supersedes it. High-volume days may be grouped, but no record may be silently dropped.

Each closed `<details>` summary exposes displayed date, canonical identity/title, area or research problem, and one-sentence delta. Its open body exposes question, smallest real delta and closest control, decisive evidence, strongest caveat, map status, primary source, and local deep note when one exists.

### Period gate

Rolling 7-day and 30-day sections state exactly one visible inclusive window and the exact UTC synthesis timestamp shared with the Timeline cutoff. Default window membership is determined only by native `radar_published_at`, and no Timeline member or period support may postdate that cutoff. Explicit or implicit legacy records may supply historical context but never native window support. A separately labeled legacy publication-date migration adapter may use honest legacy publication dates only as contextual `legacy_publication_date` `new_signal`; it must state that this is not Radar acceptance and must never represent legacy context as Radar acceptance, reinforcement, or a durable map edit. The synthesizer re-reads canonical records and deep notes inside each window; it never derives a monthly claim from weekly prose.

Each visible direction block is bound to exactly one stable metadata comment and contains exactly one visible state, ordered canonical supports field, `low` / `medium` / `high` confidence, timing basis, exact UTC synthesis timestamp, research-design implication witness, and prior-map field. Every metadata value has a visible reader-facing witness, and Chinese/English blocks are semantically paired. The repository adapter declares a canonical stable support-direction binding field: every record cited as support under direction key `K` must carry `K` in that field. Merely placing records beneath the same prose heading does not establish a shared direction. `reinforced` requires at least two distinct in-window native supports that carry the exact block key, plus independently cited prior Field Map evidence. A one-record direction can be `new_signal` only when that record has `map_delta=early_signal`; `revised`, `splits`, and `retires` require canonical support plus independently cited prior Field Map evidence, while `no_material_change` requires zero support and `prior=none`. A block with fewer than two distinct native supports cannot claim a trend, reinforcement, or durable result; similar vocabulary or a count of releases is not a trend.

### Field Map gate

Every accepted record receives exactly one `map_delta` status:

`none | early_signal | reinforces | revises | splits | retires`

`early_signal` may change Timeline or period synthesis but does not rewrite a durable node. `reinforces` requires independent evidence beyond one work. `revises`, `splits`, and `retires` require the prior map claim, new claim-level evidence, and the smallest reversible edit. If the gate is not met, preserve the existing map.

## Bilingual projection

Chinese and English are projections of one accepted judgment, not separate editorial decisions. Identity, displayed dates and order, evidence scope, decisive result, caveat, `map_delta`, period windows, and primary/local links must match. Natural phrasing may differ. Every Timeline summary carries paired `timefirst:area` and `timefirst:delta` semantic keys, and every Question, Evidence, and Caveat field carries its paired scope key. Evidence and Caveat keys also name a canonical visible-text witness after `~`; the witness is a bounded phrase with at least three hyphen-separated terms and at least two distinct, non-generic lexical content terms in each language's field. This prevents unchanged hidden keys or boilerplate such as `same-matched-evidence` from masking removal of a load-bearing result or limitation. The keys encode the shared editorial judgment without forcing translated prose to string equality; canonical titles and normalized primary/local link targets are compared directly. Any bilingual drift, missing/duplicate semantic key, unresolved local link, or validation failure aborts publication.

## Transaction, atomicity, and retry

The orchestrator executes:

`preflight → discovery → identity resolution → scope judgment → full-text reading → skeptical audit → acceptance → canonical update → Timeline → periods → closed digest if due → Field Map if gated → bilingual projection → validation → one commit`

Source failures are recorded by lane while independent lanes continue. Partial discovery can succeed only when its gap is visible in the private run report. Unavailable full text, ambiguous identity, or missing decisive evidence moves the candidate to `BLOCKED` or `DEFERRED` with a retry trigger and produces no public candidate entry.

Immediately before publishing, recheck the remote head against the frozen head. If it moved, abort the write transaction, rebase or re-read affected canonical state, re-render, revalidate, and retry once. Never force-push. A failure in any edited projection aborts the whole commit; restore a valid tree before splitting work into a later clean transaction. Publication is exactly one commit containing canonical state, both languages, derived surfaces, and digests if due.

## No public operational run logs

The Daily Agent must not create a committed operational or daily-run file. Accepted outcomes are already projected into canonical data, the complete Timeline, rolling periods, closed digests when due, gated maps, and one atomic Git commit. Private scouting, candidate, lane, retry, and validation traces belong only under ignored `.radar-private/runs/<run_id>.json` or in ephemeral Agent memory. `runs/README.md` is static policy only, and validation rejects any file under `runs/daily/` or another configured public operational-run path.

## Boundary cadence

- **Every successful material run:** update canonical records, Timeline, and rolling periods when evidence changes them; preserve the complete accepted projection in one atomic commit without a public run log.
- **First successful run after Monday 00:00 local time:** ensure an immutable digest exists for the previous complete ISO week.
- **First successful run of a new month:** ensure an immutable digest exists for the previous complete calendar month.
- **Any run:** update Field Map only when the map gate is met.
- **No material change:** validate and exit without a content commit or notification.

Separate weekly or monthly writers remain disabled. The Daily Agent owns boundary detection and uses idempotent period identities so a retry cannot create duplicate digests.

## Completion record

The private run record captures frozen context, lane status, candidate state transitions, evidence locations, dissent and resolution, accepted identities, timestamps, projection/digest decisions, map-gate result, validation commands and output, final head, and notification decision. Public surfaces contain accepted research only, never scheduler internals, candidate state, or operational run logs.
