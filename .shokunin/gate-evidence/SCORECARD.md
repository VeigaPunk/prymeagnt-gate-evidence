# gate-evidence scorecard — probation round 4

Owned axes: coverage, calibration. Scores remain unassigned without a quality rubric; the row count is a measurement, not a score or verdict. Six fleet axes: depth, coverage, operability, freshness, calibration, adjacency; only coverage and calibration are owned here.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| coverage | unmeasured | `git show d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)))"` → 7 fixtures; `git cat-file -e d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/autonomous-cases.json` exits 128 (0 autonomous fixtures); `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` → two classifications at `8bbcd4aad1d2b75970c4c185300318d5bb0e47d9`; independent expected/actual JSON comparison → 2 / 2. Synthetic coverage only, not live execution. | r3 |
| calibration | unmeasured | r4: before `52d573bdf502cb1416d65c0756106db9d5b3bde2`, no actual project gate process receipt under `corpus/live/` (`git cat-file -e 52d573b:.shokunin/gate-evidence/corpus/live/observed-bc1bb3c.json` exits 128). After: `python3 .shokunin/gate-evidence/corpus/live/audit_gate.py --revision bc1bb3c` exits 0 and records Git gate exit 0, stdout/stderr empty; in-memory whitespace control exits 3, with diagnosis. Independent native replay observed the same exits; JSON records commit/environment. Not active mission goal and no autonomous state inferred. | r4 |

planned: independent non-author review of the round-4 read-only local Git gate receipt; never conflate gate passage with live goal completion.
retired: none.
