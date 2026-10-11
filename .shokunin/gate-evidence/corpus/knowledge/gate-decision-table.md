# Gate and goal decision table — round 1

This is a **read-only interpretation** of the cited UFO workflow. It is not a gate run, a runtime oracle, or evidence that a particular mission is satisfied. A gate's exit status is scoped to its own command; acceptance criteria are a separate check. The columns below are ordered: the first matching row applies. `unknown` means no observed result, not success.

| case | untouched-tree baseline gates | candidate gates on pinned baseline | mechanical acceptance criteria at final scores | permitted conclusion / next action | source |
|---|---|---|---|---|---|
| B0 | failed or unrun | any / not applicable | any | Do not enter round 1. Fix baseline and rerun Phase 0; an unrun gate has not passed. No goal-complete claim. | `skills/ufo/references/run-logic.md:158-174`; `docs/ufo-workflow.md:21-34` |
| C0 | all observed pass | failed or unrun | any | No ship claim: all candidate gates must be rerun green before application. Do not infer task completion. | `skills/ufo/references/run-logic.md:512-524`; `docs/ufo-workflow.md:101-102` |
| G0 | all observed pass | all observed pass | at least one measured unmet | Gate passage only verifies its commands; mission is `incomplete`, and `goal.complete()` is forbidden. A sound saturated round may still be `saturated + incomplete`. | `skills/ufo/references/run-logic.md:443-455`; `docs/ufo-workflow.md:202-215` |
| G? | all observed pass | all observed pass | string-only or unmeasurable / no evidence | Mission is `unverified`, not satisfied; do not call `goal.complete()`. Make acceptance criteria mechanical in a future contract, not mid-round. | `skills/ufo/references/run-logic.md:133-137,443-455`; `docs/ufo-workflow.md:50-56,79-81` |
| G1 | all observed pass | all observed pass | every mechanical criterion measured met | Mission may be `satisfied`; only then may L1 call `goal.complete()`. This is conditional guidance, **not** an assertion that this lane ran a gate or met a goal. | `skills/ufo/references/run-logic.md:443-455`; `docs/ufo-workflow.md:50-56` |

Stop classification remains independent: a clean sound zero-accept round can be `saturated`, while a limit yields `budget_halt` or `honesty_brake`, neither implying task success. Report the triple (`round_validity`, `loop_stop`, `mission_goal`) rather than equating candidate-gate passage to goal completion (`skills/ufo/references/run-logic.md:407-455`). This table does not diagnose live state or override authority boundaries.

Measurement: count data rows with `grep -Ec '^\| (B0|C0|G0|G\?|G1) \|' .shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` (expected 5). Baseline absence at `44a08fd0eeb22c7ed9766aae4675dd452eff232a` is verified by `git cat-file -e 44a08fd0eeb22c7ed9766aae4675dd452eff232a:.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` (exit 128, therefore zero rows). This measures documented branches, **not** runtime gate correctness.
