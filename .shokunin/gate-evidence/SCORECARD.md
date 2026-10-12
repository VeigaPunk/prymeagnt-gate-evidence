# gate-evidence scorecard — probation round 6

Owned axes: coverage, calibration. Scores remain unassigned without a quality rubric; the row count is a measurement, not a score or verdict. Six fleet axes: depth, coverage, operability, freshness, calibration, adjacency; only coverage and calibration are owned here.

| axis | score | evidence / counting command | last change |
|---|---|---|---|
| coverage | unmeasured | r5: child `await goal.get()` twice returned null goal; five new scoped status/clock-versus-receipt decision rows; `python3 .shokunin/gate-evidence/corpus/live/check_goal_boundary_r5.py` exit 0. Not parent goal or autonomous telemetry. Prior: `git show d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)))"` → 7 fixtures; `git cat-file -e d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/autonomous-cases.json` exits 128 (0 autonomous fixtures); `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` → two classifications at `8bbcd4aad1d2b75970c4c185300318d5bb0e47d9`; independent expected/actual JSON comparison → 2 / 2. Synthetic coverage only, not live execution. | r5 |
| calibration | unmeasured | r6: `git cat-file -e 6c75ea3:.shokunin/gate-evidence/corpus/live/compare_parent_receipt.py` exits 128; `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` validates synthetic redacted parent-projection parser and actual local Git process pass/negative control nonzero. Parent status not actually supplied; autonomous gate/acceptance/stop not assessed. Prior r4: before `52d573bdf502cb1416d65c0756106db9d5b3bde2`, no actual project gate process receipt under `corpus/live/` (`git cat-file -e 52d573b:.shokunin/gate-evidence/corpus/live/observed-bc1bb3c.json` exits 128). After: `python3 .shokunin/gate-evidence/corpus/live/audit_gate.py --revision bc1bb3c` exits 0 and records Git gate exit 0, stdout/stderr empty; in-memory whitespace control exits 3, with diagnosis. Independent native replay observed the same exits; JSON records commit/environment. Not active mission goal and no autonomous state inferred. | r6 |

planned: L1 may optionally supply an actual redacted status/UTC clock from its own goal.get(); independent non-author review needed; host autonomous gate remains unobserved.
retired: none.


## L1 closure correction — 2026-10-12
Supersedes the stale planned statement above that an actual status/UTC projection remained optional or unsupplied, and that independent review was still pending. R7 did record a parent-supplied projection and received named independent review (`gate-r7-review`; `.shokunin/reports/round-7/gate-evidence.md`; closure pointer `91831c0`). R8 had no axis advance (`gate-r8-review`, `b860fd9`, closure `d53d29b`). R9 precision fix calibration improved narrowly after `gate-r9-review` (work `442927e`, report `ade48d7`, path `a7dc21e`; closure `91831c0`). R10 unknown-offset fix calibration improved narrowly after `gate-r10-review` (work `e5642da`, report `4aa930b`; closure `c60cd8f`). Coverage remains unchanged across R7–R10; numeric scores remain unassigned. These receipts do not prove host autonomous-gate execution, acceptance, mission-goal success, or loop-stop. SHONEN end-to-end box remains unchecked; no promotion. Historical planned text is retained above, not current status.


## Correction — closure commit pointers (2026-10-12)
This append-only correction supersedes the closure-hash references in “L1 closure correction — 2026-10-12” above: R7 pointer `91831c0` was wrong; correct closure is `2bef169`. R8 pointer `d53d29b` was wrong; correct closure is `b91df28`. R9 `91831c0` and R10 `c60cd8f` were correct and remain unchanged. Correct pointers: R7 `2bef169`, R8 `b91df28`, R9 `91831c0`, R10 `c60cd8f`. No verdict or evidence claim changes.


## Round 11 evidence (synthetic, no score assigned)
Calibration evidence: `corpus/fixtures/r11-syntax-cases.json` gives 3 baseline `datetime.fromisoformat` accepts (`T` space, `+0000`, `+00`) rejected by strict candidate syntax; `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` passed. Z/+00:00 and six-digit fraction controls pass; -00:00, >6 digits, non-UTC controls reject. Leap second remains unsupported. Proposed calibration improved narrowly; coverage unchanged (no new policy branches). These are synthetic parser/process tests, not host autonomous or acceptance proof.


## Round 13 precision-boundary correction (2026-10-12)
Correction to R13 report counts: accepted fractional widths actually tested are 7 and 19 digits with `Z`, plus 14 digits with `+00:00`; a 20-digit `Z` timestamp (41 chars total) is rejected by the retained 40-character whole-timestamp cap. Arbitrary fraction precision applies only within that cap. Added boundary checker passed (exit 0), work commit `ae613ad428375ad4b81dd963f3718e329c6a934f`. Coverage improved; calibration unchanged remains the proposed round judgment, with no leap-second completeness or host gate proof. See R13 report correction.


## Round 14 (proposed; synthetic)
Calibration improved narrowly: duplicate JSON object keys at top-level and nested object depth now reject before the read-only Git gate. Coverage unchanged; no policy branch added. Native duplicate negatives and unique control passed. No host autonomous acceptance/stop claim. Details: `.shokunin/reports/round-14/gate-evidence.md`.
