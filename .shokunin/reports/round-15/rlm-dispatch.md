# Round 15 — RLM dispatch JSON constants

- Base: `2eecc8c` (`R15 isolated`); scope limited to `.shokunin/rlm-dispatch/**` and this report.
- Change: shared `parse_json()` rejects Python decoder extensions `NaN`, `Infinity`, and `-Infinity` using `parse_constant`. The dedicated rejection maps to the existing generic malformed JSON failure at registry, session JSONL, and settlement boundaries.
- Evidence: three independent native-Python local fixtures each contain one ignored nonfinite constant. Baseline false-PASS exit 0 at registry/session/settlement; current generic `FAIL: input contains malformed JSON syntax`, exit 1 at each. Locality-rewritten copied good positive: baseline/current PASS, 0/0. Fixture files are under `corpus/verification/fixtures/nonfinite-*`.
- Regression: original nine controls current exits `0/1/0/1/1/0/1/1/1`; R10 isolated duplicate pathways/positive `1/1/1/0`; R11 four shape negatives and positive `1/1/1/1/0`; R12 syntax negatives `1/1/1`; R14 UTF-8 negatives and positive `1/1/1/0`. Verifier CLI check ran against these fixture groups.
- Axis verdict: calibration improved narrowly for non-JSON token rejection; operability unchanged. No provider/usage inference and no claim of semantic receipt authenticity. Synthetic local fixtures only; no provider or daemon calls.
- Constraints: no manifest/global harness/provider/daemon/merge/push changes.
