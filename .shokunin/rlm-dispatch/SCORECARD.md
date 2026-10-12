# rlm-dispatch scorecard — probation baseline

Owned axes: operability, calibration. Scores are not assigned without a measured craft round.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| operability | improved (proposed) | Round 7 swapped-session fixture old verifier PASS → current reject; seven prior fixture outcomes retained (command/output in round-7 report) | round 7 |
| calibration | improved (proposed) | Baseline accepts synthetic late-forbidden-switch (exit 0); current rejects it (exit 1); two matching routes pass; no live authentication or usage-depletion claim | round 5 |

planned: no axis advance proposed in round 8; preserve the verifier absent a concrete counterexample. L1 judges all owned axes.
retired: none.

## L1 closure appendix — 2026-10-12
- R7: admitted — operability improved; calibration unchanged (independent review: `promotion-and-session-review`, `984a3a6`).
- R8: unchanged — operability unchanged; calibration unchanged; no axis advance (independent review: `R8/R7 independent review`, `80b6ce4`).
- No scalar score assigned. Synthetic verifier evidence only; no live provider authentication or usage/depletion proof.

## Round 9 proposal
- Operability: improved — wrong-type synthetic registry formerly passed, now rejected; eight documented outcomes retained.
- Calibration: improved — exact observed native discriminator enforced; missing `type` is rejected, not accepted as legacy. Synthetic schema tests only; no new live provider authentication evidence.

## Round 9 L1 closure correction — 2026-10-12
The Round 9 two-axis proposal above is superseded by the append-only LOG correction and L1 manifest closure at `2113cef`. The author restored the `linked-good` positive and added a separate ninth wrong-type fixture; the eight earlier outcomes remained `0/1/0/1/1/0/1/1` and the ninth changed baseline PASS (0) to final reject (1). Independent `dispatch-r9-type-review` admitted **calibration improved narrowly; operability unchanged**. This correction changes bookkeeping only; no new test, axis move, promotion, or live provider authentication is claimed.


## Round 10 proposal
- Operability: unchanged; all nine previous fixture outcomes retained.
- Calibration: improved narrowly; tenth duplicate-key fixture baseline PASS (0) → current reject (1), including nested session role duplicate. Synthetic local testing only; no live provider authentication or usage-depletion claim.


## Round 10 evidence correction
Isolated local fixtures now independently exercise duplicate registry, nested session event role, duplicate settlement, and a unique positive; baseline/current exits `0/1`, `0/1`, `0/1`, and `0/0`. Calibration remains narrowly improved; operability unchanged, nine controls preserved. Synthetic evidence only.


## Round 11 proposal
- Operability: improved narrowly; four isolated malformed-shape cases previously escaped as uncaught `AttributeError`; current verifier returns generic failure, while positive exit remains 0. All nine prior outcomes are preserved.
- Calibration: unchanged; checks are limited to shape safety before existing acceptance logic. Synthetic tests only; no provider authentication or live behavior claim.


## Round 11 evidence correction
Three negative fixtures' registry `sessionFile` values now resolve inside their own fixture directories rather than `linked-good`. Baseline/current isolated negative and positive outcomes revalidated; see the appended LOG correction and round-11 report correction. Verdict is unchanged: operability improved narrowly; calibration unchanged. This does not claim handling of malformed JSON syntax, filesystem errors, or NUL input.


## Round 12 proposal
- Operability: improved narrowly; three independently malformed JSON/JSONL inputs previously escaped as `JSONDecodeError` tracebacks, now return generic verifier failures; isolated positive and all prior controls retain outcomes.
- Calibration: unchanged; no valid-input acceptance criteria changed. Synthetic local tests only. File/read errors, NUL paths, and live provider behavior are not claimed.


## Round 14 proposal
- Operability: improved narrowly; isolated invalid UTF-8 at registry, session JSONL, and settlement boundaries changes baseline uncaught traceback/exit 1 to generic FAIL/exit 1 without traceback; valid positive and all prior regression controls retain outcomes.
- Calibration: unchanged; only decode exception reporting changes, not accepted receipt predicates. Synthetic local tests only; no live provider/authentication claim. Filesystem I/O errors are not caught or claimed.
