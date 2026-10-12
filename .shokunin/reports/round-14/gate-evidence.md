# Gate-evidence round 14 — duplicate JSON object keys

## Change
`compare_parent_receipt.py` now supplies an `object_pairs_hook` that rejects duplicate member names at every JSON object depth. The parser raises a generic `ValueError`; the CLI retains its generic failure message and returns 2 before resolving revisions or running the read-only Git diff gate.

## Evidence
The native contract checker accepts the exact unique-key projection (including the null-goal control) and still runs the pinned read-only Git gate successfully. A raw-string helper tests duplicate `observed_utc` at top level and duplicate nested `status`; both return 2 with no stdout and only the generic error, before gate invocation. Existing strict timestamp positives/negatives, secret-injection control, and whitespace negative control passed. `check_gate_cases.py`, `check_autonomous_cases.py`, Python compilation, and `git diff --check` passed.

## Proposed axis judgment
**Calibration improved narrowly; coverage unchanged**, conditional on these controls holding. Duplicate keys previously allowed Python JSON decoding to silently retain the last value, undermining the exact-key-set contract; they are now rejected at every depth. No new policy branch was added. This is synthetic parser/process evidence only—not host autonomous-mode acceptance, stop evidence, or a completion claim.
