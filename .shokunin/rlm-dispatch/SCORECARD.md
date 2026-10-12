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
