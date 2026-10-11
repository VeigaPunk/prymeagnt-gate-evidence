# rlm-dispatch — round 7 report

## Work performed
- Inspected the exact round-2 live registry artifact `rlm-subagent.json`; it contains `sessionFile` (alongside `childId`, `sessionDir`, `model`, `status`). The recorded round-2 corpus summary omitted that field; source artifact: `/home/vgpnk/.prime/agent/session-artifacts/01a12d0c-9c40-7153-9d7f-967a6e189ec5/sub-52e968c6/rlm-subagent.json` (observed field names and child/session linkage printed during this round).
- Added validation that registry `sessionFile` resolves to the supplied session path and added a same-child-ID swapped-session fixture. Old verifier on fixture: PASS (exit 0); updated verifier: FAIL, `session path does not match registry sessionFile` (exit 1).
- Updated all seven prior registry fixtures with sanitized repo-relative `sessionFile` values and documented the eighth check. No network/runtime calls, live spawn, or receipt-input mutation.

## Landed changes
- Verifier, docs, seven existing fixture registry paths, new swapped-session fixture, LOG and SCORECARD: commit `7abe5fb63fced16d368b3a3a062b16f24fe82de8`.
- Swapped-session fixture hashes: expected and alternate session JSONL are both SHA-256 `38e0457186d025cd47f3853e34c24fba257d1f08655608f2556bb2c02b0c31bd`; verifier SHA-256 `26a56fe3aae1e3718a19c38aea259347e512a7bc4bd2ac1de7874b7604ae65b2`.

## Before → after measurements
- Falsifiable operability claim: same `childId` and basename but supplied session path differs from registry `sessionFile`. Baseline verifier accepted the sanitized swapped-path fixture (PASS, exit 0); current verifier rejects it (FAIL, exit 1) with the path mismatch error.
- Regression command: the eight commands listed in `corpus/verification/README.md`, run from repository root. Outcomes in README order: 0/1/0/1/1/0/1/1. Thus all seven prior fixtures retain their outcomes and the new counterfeit is rejected. `git diff --check` also passed before commit. Measured work commit: `7abe5fb63fced16d368b3a3a062b16f24fe82de8`.

## Axis verdicts
- Operability: **improved** — a same-ID session swap previously passed and is rejected using the registry's observed `sessionFile` field.
- Calibration: **unchanged** — no new runtime observation or selector-admission evidence; fixture behavior alone is not live provenance.

## SHONEN
- [~] Real decision tables/error patterns/checklists with cited sources — existing cited procedure; no new independent verifier this round.
- [~] End-to-end domain task executed and logged — new synthetic verifier scenario only; not a live domain task.
- [~] Instructions executable without oral context — eight documented local fixture commands, executed successfully as expected.
- [~] No cross-domain bleed; PROVINCE remains accurate — only `.shokunin/rlm-dispatch/**` and this report changed.

## Evidence limits and constraints
- Synthetic fixtures test verifier logic only. They do not prove live authentication, provider/model execution, or usage depletion. No depletion inference is made.
- No MANIFEST/global harness/source edits or push. Both author and committer of the work commit are `rlm-dispatch-shokunin <rlm-dispatch@shokunin.local>`.
