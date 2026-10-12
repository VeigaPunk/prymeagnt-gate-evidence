# Round 11 — gate-evidence timestamp syntax

Base: `4df340d50a52c36dafa5872487f6e4562ff3cbce`. Work commit: `ce77e0358d8d58311e78fd8eb3cba8d0b95e258b`.

The parser previously delegated lexical acceptance to `datetime.fromisoformat`, which accepts non-RFC3339 space separators and basic/short offsets. Added a compact RFC3339 shape check requiring `T`, `Z` or colonized `±HH:MM`, and optional 1–6 digit fractional seconds, then retained datetime semantic validation and existing UTC semantics. Synthetic corpus contains exact baseline-accepted/candidate-rejected examples for space separator, `+0000`, and `+00`. Native-process checker passed, including accepted Z/+00:00 and six-digit fraction controls and existing rejection controls (-00:00, >6 digits, non-UTC); existing table fixture checker passed; `git diff --check` passed.

Limitation: Python datetime rejects leap seconds, a separate RFC3339 false reject. This does not claim full RFC3339 compliance. No host autonomous-gate evidence or mission-goal inference.

Proposed one-axis calibration: **improved narrowly**, three demonstrated false accepts now rejected with controls preserved. Coverage: **unchanged**, no policy branch/category added.
