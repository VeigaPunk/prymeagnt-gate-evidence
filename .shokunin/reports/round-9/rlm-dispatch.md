# rlm-dispatch — round 9 report

## Work and evidence
- Required exact registry discriminator `type == "rlm_subagent"` in the read-only verifier. Missing and wrong values both fail. Updated all eight existing synthetic registry fixtures to carry the discriminator; one fixture now deliberately contains a wrong type.
- Native-schema evidence: round-2 observed registry shape is documented at `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-round2-admission.md`; `verification/smoke-test-rerun-20261011.log:231` records native `type: rlm_subagent`; assignment reports a read-only corpus census of 175/175 native records with that type. No private IDs copied.
- Reproduction instructions and synthetic-vs-live limitation are in `.shokunin/rlm-dispatch/corpus/verification/README.md`. Fixture schema edits are not new runtime receipts or live provider authentication.

## Results
- Eight expected exits in README order: `0/1/1/1/1/0/1/1`. The expected eight are retained; third fixture is now explicit wrong-type regression. At baseline `f7c14108b0f484b17a3146674a52b62ccc5b967d`, that fixture passed (exit 0); current verifier rejects it (exit 1).
- `git diff --check` passed.

## Axis proposals
- Operability: **improved** — verifier rejects a wrong native registry discriminator previously accepted; the eight-command test is reproducible.
- Calibration: **improved** — enforces observed discriminator exactly and does not silently treat omitted type as legacy. Synthetic verifier evidence only, not live provider authentication.

Work commit and report-last commit hashes/identities are recorded after landing below. No MANIFEST/global/push.


## Correction — preserved prior positive control
The initial revision incorrectly repurposed `linked-good` as the wrong-type case, changing an existing positive regression control. Corrected by restoring its `rlm_subagent` discriminator and adding a separate ninth `wrong-type` fixture. Eight prior expected results are preserved: `0/1/0/1/1/0/1/1`; new ninth result is baseline 0/current 1. This supersedes the initial eight-case result and axis proposal above. Corrected proposals: operability **unchanged** (old controls preserved), calibration **improved** (the new strict native-type check rejects a demonstrated false PASS).

Correction work commit: `ebeb48fc55836d2d462d8fa3256392ab69c2fe51`. This report correction is committed last; both commits use canonical lane identity.
