"""Scheduled citation refresh: retain the last verified snapshot on API outages.

The updater saves the registry only after its network phase completes. Transient
network failure therefore leaves every file and verification date untouched.
Malformed responses, authentication errors and publication failures still fail.
"""
from __future__ import annotations

import sys
from urllib.error import HTTPError, URLError

import update_citations as updater

TRANSIENT_STATUS = {429, 500, 502, 503, 504}


def run() -> int:
    try:
        return updater.main()
    except HTTPError as exc:
        if exc.code not in TRANSIENT_STATUS:
            raise
        reason = f"citation provider returned HTTP {exc.code}"
    except (URLError, TimeoutError) as exc:
        reason = f"citation provider unavailable ({type(exc).__name__})"
    # No replacement count, freshness bump or partial publication is fabricated.
    print(
        "::warning::Citation refresh deferred: " + reason
        + ". Existing counts and verification dates were retained; no refresh completed.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
