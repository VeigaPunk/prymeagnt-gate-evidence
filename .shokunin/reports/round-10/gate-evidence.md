# Gate-evidence — round 10

## Bounded calibration move

**Claim:** At baseline `314935acffb768470891be5990741cc149ed5600`, the supplied-projection parser accepted an RFC 3339 `-00:00` timestamp as known UTC because Python `datetime.fromisoformat` gives it a zero UTC offset. This was a false acceptance for the parser's UTC-clock contract. RFC 3339 §4.3 explicitly assigns `-00:00` the meaning “offset to local time is unknown,” distinct from `Z` and `+00:00`, which imply UTC is the preferred reference point: [RFC 3339 §4.3](https://www.rfc-editor.org/rfc/rfc3339.html#section-4.3). This supports rejecting the form as insufficient evidence of a UTC-referenced clock; it makes no host-authentication claim.

**Reproduction and change:** Baseline `parse_status` accepted `{"goal":null,"observed_utc":"2026-10-11T00:00:00-00:00"}` and returned a successful null-goal projection (reproduced with the baseline module). The parser now rejects a timestamp ending in `-00:00` before parsing. Synthetic native-process fixtures retain six-digit `Z` and `+00:00` acceptance; `-00:00` is rejected without a receipt. Existing secret/objective and non-UTC controls remain in the checker.

**Verification:** `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` exited 0: positive and null projections parsed, actual read-only Git `diff --check` exited 0, stdin whitespace negative control failed as expected, and objective/secret plus non-UTC inputs were rejected. New six-digit UTC spellings both pass; unknown-offset spelling rejected. `git diff --check` exited 0. Evidence is synthetic input plus local Git process, not actual parent goal or autonomous-gate telemetry.

**Verdicts:** Calibration **improved** narrowly: a reproduced semantic false pass is fixed, with positive and negative controls. Coverage **unchanged**: no additional policy branch or operational gate was assessed. No host authentication, autonomous gate, acceptance, stop, or mission-goal claim. No SHONEN promotion.
