# Public Run-State Policy

## No public operational run logs

This is a static policy page. The Daily Agent never commits operational or daily-run files under `runs/daily/` or another public path. Private scouting, candidate, lane, retry, and validation traces belong only under ignored `.radar-private/runs/<run_id>.json` or in ephemeral Agent memory.

Public provenance is the canonical registry, its complete bilingual Timeline and rolling-period projection, any due closed digest, and one atomic Git commit. Validator-enforced absence keeps private workflow state out of the reader surface.
