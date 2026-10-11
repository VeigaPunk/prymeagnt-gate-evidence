# gate-evidence — round 2

## Work performed
- Exercised ordered table against deterministic baseline-failed/unrun, candidate-failed/unrun, goal-unmet/unverified/met fixtures: `.shokunin/gate-evidence/corpus/fixtures/gate-cases.json:1`, `.shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py:1`, `.shokunin/gate-evidence/corpus/fixtures/actual.json:1`. Sources remain read-only (`skills/ufo/references/run-logic.md:158-174,443-455,512-524`).
- Documented invocation and fixture/live distinction: `.shokunin/gate-evidence/corpus/fixtures/README.md:1-11`. No real gate invoked and no `goal.complete()` called.
- Recorded calibration **improved** for synthetic classification evidence and coverage **unchanged**; no assertion of actual gate or mission success: `.shokunin/gate-evidence/LOG.md:15-19`, `.shokunin/gate-evidence/SCORECARD.md:8`.

## Landed changes
- `LOG.md:15-19` records fixture input, expected/actual output, independent comparison, claim, and both owned-axis verdicts; corpus fixtures and index carried by `86fb105a888dd77d138a482faecdc21f22baefcc`, log/scorecard by `eb0f8c6c56742ac0dbcddfab952028a9819b1974`. `git rev-parse HEAD` at report write: `eb0f8c6c56742ac0dbcddfab952028a9819b1974`.

## Before → after measurements
- Calibration claim, baseline `65a1d7b8215bf1bb764c0c9957f217a930f27b78`: `git cat-file -e 65a1d7b8215bf1bb764c0c9957f217a930f27b78:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json` exits 128 (fixture absent; zero independently tested classifications). After fixture commit `86fb105a888dd77d138a482faecdc21f22baefcc` and record commit `eb0f8c6c56742ac0dbcddfab952028a9819b1974`: `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` exits 0, stdout at `.shokunin/gate-evidence/corpus/fixtures/actual.json:1-51`; independent comparison `python3 -c 'import json,pathlib; p=pathlib.Path(".shokunin/gate-evidence/corpus/fixtures"); e=json.loads((p/"gate-cases.json").read_text()); a=json.loads((p/"actual.json").read_text()); assert a == [f["expected"] for f in e]; print("independent expected/actual comparison:",len(a),"/",len(e))'` prints `independent expected/actual comparison: 7 / 7`. This is deterministic fixture coverage, not live runtime correctness.
- Coverage: **unchanged**; the same five decision rows in `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` before and after. `grep -Ec '^\| (B0|C0|G0|G\?|G1) \|' .shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` prints 5 at `eb0f8c6c56742ac0dbcddfab952028a9819b1974`; round-1 LOG records 5 at `a257b4b35f7718a70eec0f0f31fc70cfeba4538d` (`.shokunin/gate-evidence/LOG.md:8-12`).

## SHONEN
- [~] Real decision table with cited sources: `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:1-15`; no named non-author verifier.
- [ ] End-to-end domain task executed and logged: synthetic fixtures only; no live gate.
- [~] Instructions executable without oral context: `.shokunin/gate-evidence/corpus/fixtures/README.md:1-11`; no named non-author verifier.
- [~] No cross-domain bleed; PROVINCE remains accurate: `.shokunin/gate-evidence/PROVINCE.md:1-13`; no named non-author verifier.

No operator question opened. No L2 sub-lanes dispatched: this bounded local fixture task did not warrant delegation. Push/publication remain L1-owned.
