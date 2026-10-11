# gate-evidence scorecard — probation round 3

Owned axes: coverage, calibration. Scores remain unassigned without a quality rubric; the row count is a measurement, not a score or verdict. Six fleet axes: depth, coverage, operability, freshness, calibration, adjacency; only coverage and calibration are owned here.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| coverage | unmeasured | `git show d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)))"` → 7 fixtures; `git cat-file -e d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/autonomous-cases.json` exits 128 (0 autonomous fixtures); `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` → two classifications at `8bbcd4aad1d2b75970c4c185300318d5bb0e47d9`; independent expected/actual JSON comparison → 2 / 2. Synthetic coverage only, not live execution. | r3 |
| calibration | unmeasured | source-only at `65a1d7b8215bf1bb764c0c9957f217a930f27b78`: `git cat-file -e 65a1d7b8215bf1bb764c0c9957f217a930f27b78:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json` exits 128 (0 tested); after `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` exits 0 and independent expected/actual comparison prints `7 / 7`, fixture commit `86fb105a888dd77d138a482faecdc21f22baefcc`; synthetic, not a live gate | r2 |

planned: a later, separately authorized round may exercise a real gate; never conflate synthetic fixtures with live goal completion.
retired: none.
