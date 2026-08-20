# Research Compactions

This directory stores closed-period benchmark synthesis rather than benchmark-by-benchmark summaries. The root README owns rolling, inclusive 7-day and 30-day windows; those sections may change on any material Daily Agent run and are not immutable digests.

- `weekly/YYYY-Www.md`: new benchmark releases, protocol changes, validity findings, and the 1–3 evaluation shifts that matter that week.
- `monthly/YYYY-MM.md`: which capabilities are becoming well measured, where benchmark families converge or conflict, and which apparent progress is mostly harness/model drift.
- `yearly/YYYY.md`: durable changes in evaluation targets, field-defining benchmark families, weakened assumptions, and the most important remaining measurement gaps.

Compactions should always re-ground load-bearing claims in the canonical registry and primary benchmark sources. A trend requires more than multiple papers using similar language.

The Daily Agent is the only boundary writer:

- on the first successful run after Monday 00:00 in the repository's configured local timezone, it creates the previous complete ISO-week digest if that period identity does not already exist;
- on the first successful run of a new month, it creates the previous complete calendar-month digest if absent;
- monthly synthesis re-reads canonical records and deep notes for the month and never summarizes weekly prose;
- a retry uses the same period identity and cannot create a duplicate file;
- an incomplete current week or month remains represented only by the rolling root windows.

Each closed digest states its exact inclusive start/end dates, synthesis time, supporting accepted identities, confidence, and implications for research design. Candidate, blocked, deferred, rejected, and abstract-only work remains private. Separate weekly/monthly schedulers stay disabled so boundary publication is part of the Daily Agent's one atomic transaction.
