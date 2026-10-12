# Round 16 — documented goal lifecycle status allowlist

## Candidate

The parent-projection parser accepted any lowercase-looking label (`[a-z][a-z_-]{0,31}`) as a goal status and then ran its Git gate. The goal skill is the contract source: `/home/vgpnk/.local/share/prime-agent/skills/goal/SKILL.md` documents `goal` as `None` when no goal is set and lists `active`, `paused`, `budget-limited`, `completed`, and `errored` in the `create` precondition. Its adjacent Python source (`skills/goal/src/goal/__init__.py`) repeats these states and returns the host `goal.get` mapping. No other goal lifecycle state was found in the installed skill/runtime source search. Null/no-goal is explicitly permitted and was already accepted by the comparator contract; null has no lifecycle status to allowlist.

The bounded allowlist in `compare_parent_receipt.py` now accepts only those five documented labels. It does not claim that the projection is authenticated or current host telemetry. `check_parent_receipt_contract.py` exercises every documented status through the native checker process. All five returned exit 0, emitted a receipt preserving the supplied status, and therefore executed the ordinary read-only pinned Git `diff --check` (exit 0). `native` and `not-a-real`, both formerly accepted by the lexical grammar, each returned exit 2, no stdout, and the generic `invalid redacted status; no gate run` diagnostic. Null goal remains accepted and its Git gate passes. This is parser/process contract evidence, not proof that the host was in any given status.

## Validation

- `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` — exit 0; status controls above plus retained timestamp, duplicate-key, secret/objective, null, non-UTC, positive Git gate, and whitespace negative control.
- `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` — exit 0 (7 existing fixtures).
- `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` — exit 0 (2 existing fixtures).
- `python3 -m py_compile` on the parser and contract checker — exit 0.
- `git diff --check` — exit 0.

## Axis proposal

- **Calibration: improved narrowly.** Two bogus values accepted before are rejected before gate execution; all five documented values and null goal retain the ordinary gate behavior. This is better alignment to the documented host lifecycle, not host-status verification.
- **Coverage: unchanged.** This tightens validation of an existing field; it adds no new policy branch or autonomous/acceptance/stop evidence.

No host autonomous acceptance/stop inference, real parent goal projection, `goal.complete()`, gate configuration mutation, or external service action occurred. Existing contract/timestamp/duplicate/gate fixtures were retained.
