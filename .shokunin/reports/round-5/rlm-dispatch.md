# rlm-dispatch — round 5

## Work performed
- Updated `.shokunin/rlm-dispatch/corpus/verification/verify_receipt.py` so every session `model_change` must match permitted `openai-codex/gpt-6-luna`, rather than checking only the first event.
- Added sanitized `two-matching-model-changes` positive and `late-forbidden-switch` negative fixtures. Existing five fixtures are unchanged.
- Work commit: `bfb7c556717ce5f9bf15dff359c62ae76831c5f5`.

## Before → after
- Baseline verifier accepted `late-forbidden-switch` (PASS, exit 0): it checked the allowed first `model_change` and ignored the later synthetic Anthropic route.
- Current verifier rejects that same fixture with `session provider/model mismatch` (exit 1). Two matching allowed changes pass (exit 0).
- All seven fixtures, in README order, produced exits `0/1/0/1/1/0/1`. `python3 -m py_compile .../verify_receipt.py` and `git diff --check` passed. README provides exact commands.
- These are sanitized synthetic fixtures. They establish verifier behavior only—not live provider authentication, real model usage, or usage depletion.

## Owned-axis verdicts (proposed)
- **Calibration: improved.** The verifier no longer accepts a synthetic session with a later forbidden selector switch; positive repeated allowed provenance remains accepted.
- **Operability: unchanged.** Same local, read-only verifier interface and preserved original five fixture outcomes.

## Bounded proposed global triple update
If independently admitted, update only the RLM-dispatch global procedure/memory/subagent triple to require checking every session `model_change` against the permitted selector and to keep synthetic verifier evidence explicitly separate from live authentication / usage claims. No global harness entries were changed in this lane.

## Bounds
Only `.shokunin/rlm-dispatch/**` and this report were edited. No MANIFEST, global harness, source, or push. No live provider authentication or model usage depletion is claimed.
