# Read-only gate table fixture exercise — round 2

Run from the repository root:

```sh
python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py
```

Exit 0 means the observed classifications match `gate-cases.json` expected outputs; stdout is persisted at `actual.json` from the round-2 run. The checker parses the ordered case rows in `../knowledge/gate-decision-table.md` and applies their baseline, candidate, and acceptance predicates. It also checks critical conclusion wording. Its finite predicate vocabulary deliberately rejects unknown wording rather than silently assigning a success case. A failed, unrun or missing gate is **not** represented as a live gate result: these are made-up deterministic inputs. Source basis: `skills/ufo/references/run-logic.md:158-174,443-455,512-524` and `docs/ufo-workflow.md:33-34,50-63,202-215` (read-only).

Seven fixtures cover baseline failed/unrun, candidate failed/unrun, mechanical goal unmet, goal unverified, and mechanically met. `candidate_gates_passed` means only the synthetic gate state is pass, **not** that a ship claim is authorized. `goal_complete_permitted` is only a table-policy classification, not a call to `goal.complete()` or observed satisfaction. No gate was invoked, no runtime inspected, and no mission marked complete.
