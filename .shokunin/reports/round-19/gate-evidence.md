# Round 19 — gate-evidence token-budget calibration

## Scope and evidence

Baseline `f7842da` accepted fractional `token_budget` values because it shared the nonnegative numeric validation used for `tokens_used` and `time_used_seconds`. The native `/goal --budget` contract is a positive integer; `docs/capability-survey.md:81-82` documents the parse error. The parser now accepts only `null` or an actual positive integer for `token_budget`. It rejects Python booleans as well as fractional and integral floats (`100.0`); the other two clock fields retain their existing numeric behavior.

The native contract checker validates integer `100` and null as accepted. It checks rejection of `100.5`, `100.0`, true/false, zero and negative values, with generic error, exit 2, and no JSON output before Git gate. It also checks fractional `tokens_used` and `time_used_seconds` remain accepted. Existing lifecycle, null-goal, timestamp, duplicate-key, and local Git positive/negative controls remain exercised by that checker.

Commands run from this checkout:

- `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` — passed; real read-only Git diff gate exit 0, stdin whitespace negative control failed as expected.
- `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` — passed.
- `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` — passed.
- `python3 -m py_compile .shokunin/gate-evidence/corpus/live/compare_parent_receipt.py .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` — passed.
- `git diff --check` — passed.

## Proposed one-axis judgment

**Calibration improved narrowly**: the parser now rejects a concrete documented type mismatch and preserves valid integer/null budgets and the unrelated clock-field behavior. **Coverage unchanged**: no decision-table branch or policy category was added.

This test uses synthetic parent-supplied projections. It is not an authenticated host projection and proves no host autonomous-gate execution, acceptance, mission-goal success, or loop-stop. No `goal.complete()` call or such claim is made. No manifest, global harness, provider, daemon, merge, or push change.
