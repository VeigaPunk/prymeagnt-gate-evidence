# gate-evidence scorecard — probation round 2

Owned axes: coverage, calibration. Scores remain unassigned without a quality rubric; the row count is a measurement, not a score or verdict. Six fleet axes: depth, coverage, operability, freshness, calibration, adjacency; only coverage and calibration are owned here.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| coverage | unmeasured | `git cat-file -e 44a08fd0eeb22c7ed9766aae4675dd452eff232a:.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` exits 128 (absent, 0 rows); `grep -Ec '^\| (B0|C0|G0|G\?|G1) \|' .shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` → 5 rows at `a257b4b35f7718a70eec0f0f31fc70cfeba4538d` | r1 |
| calibration | unmeasured | source-only at `65a1d7b8215bf1bb764c0c9957f217a930f27b78`: `git cat-file -e 65a1d7b8215bf1bb764c0c9957f217a930f27b78:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json` exits 128 (0 tested); after `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` exits 0 and independent expected/actual comparison prints `7 / 7`, fixture commit `86fb105a888dd77d138a482faecdc21f22baefcc`; synthetic, not a live gate | r2 |

planned: a later, separately authorized round may exercise a real gate; never conflate synthetic fixtures with live goal completion.
retired: none.
