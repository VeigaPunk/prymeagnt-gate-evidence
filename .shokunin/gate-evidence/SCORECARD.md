# gate-evidence scorecard — probation round 1

Owned axes: coverage, calibration. Scores remain unassigned without a quality rubric; the row count is a measurement, not a score or verdict. Six fleet axes: depth, coverage, operability, freshness, calibration, adjacency; only coverage and calibration are owned here.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| coverage | unmeasured | `git cat-file -e 44a08fd0eeb22c7ed9766aae4675dd452eff232a:.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` exits 128 (absent, 0 rows); `grep -Ec '^\| (B0|C0|G0|G\?|G1) \|' .shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` → 5 rows at `a257b4b35f7718a70eec0f0f31fc70cfeba4538d` | r1 |
| calibration | unmeasured | source and caveat review of `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` at `a257b4b35f7718a70eec0f0f31fc70cfeba4538d`; no runtime gates run | r1 |

planned: a later, separately authorized round may add a tested gate-result fixture; never conflate it with live goal completion.
retired: none.
