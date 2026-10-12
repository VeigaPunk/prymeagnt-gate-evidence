# Round 12 — RFC3339 lowercase marker calibration

## Scope and cited rule

This round tests one parser-calibration correction in the parent-supplied redacted status comparator. RFC 3339 §5.6 NOTE states that the `T` and `Z` characters may alternatively be lowercase `t` and `z` (per ABNF and ISO 8601). Source: [RFC 3339, §5.6](https://www.rfc-editor.org/rfc/rfc3339#section-5.6) (published text: https://www.rfc-editor.org/rfc/rfc3339.txt).

At baseline `cd16fdf789fdcd64835279fb37606b1c38997122`, independently loading the baseline parser and supplying `2026-10-11t00:00:00z` and `2026-10-11T00:00:00z` returned `REJECT` for each (`invalid UTC timestamp syntax`). The baseline is a concrete false rejection of syntax expressly allowed by the RFC note.

## Change and verification

Work commit: `626f2df8f719223ae848cd751871e41fe31595e9`. The lexical gate now admits either case for `T` and `Z`; conversion maps a terminal `Z` or `z` to `+00:00` for `datetime` validation. The returned `observed_utc` remains the original caller string; both new native-process fixtures assert exact preservation. No other timestamp is normalized in the saved projection.

`python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` passed. Each accepted fixture launches the comparator as a separate native process and its accepted path runs the pinned read-only Git `diff --check` process (exit 0). Existing controls remain: RFC3339 uppercase `Z` and `+00:00` positives; reject space separator, `+0000`, `+00`, non-UTC `+01:00`, unknown `-00:00`, and >6 fractional digits; exact microseconds preserve the input; secret/objective input yields no receipt. The Git stdin whitespace negative control fails as expected. `git diff --check` passed before commit.

No full RFC3339 claim: Python `datetime` still does not support leap seconds, and fractions longer than six digits remain intentionally rejected. Scope is limited to lowercase-equivalent `T`/`Z` for this UTC projection.

## Proposed axis judgment (L1 decision pending)

- **Calibration: improved narrowly.** Two independently baseline-reproduced false rejects now pass through native-process fixtures, retain the caller's exact timestamp in the output, and preserve existing rejection controls. This is parser-contract evidence, not host autonomous-gate or mission evidence.
- **Coverage: unchanged.** This fixes accepted spelling of the existing UTC timestamp field; it adds no policy branch or gate category.

No global harness edit, MANIFEST change, push, gate mutation, goal completion, host autonomous status, acceptance, mission-goal success, or loop-stop claim. SHONEN/autonomous state is unchanged and unassessed.
