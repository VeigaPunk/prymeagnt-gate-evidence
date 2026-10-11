# Round 3: local admission/settlement verifier — 2026-10-11

Added read-only `corpus/verification/verify_receipt.py` with sanitized fixtures. It checks fixed `openai-codex/gpt-6-luna` in registry and first session `model_change`, completed registry state, assistant response, and a `done`/settled/no-error collect receipt. It has no external dependency beyond Python stdlib and no network/runtime side effects.

Validation: positive fixture exit 0 (`PASS`); negative fixture with wrong provider/model and running/unsettled receipt exit 1, naming registry provider/model mismatch, unsettled receipt, session mismatch, and missing assistant response. Command is in round report. Baseline before this commit: no local verifier and 0 fixture scenarios recognized; after: 1 positive accepted and 1 deliberately invalid scenario rejected. This is fixture validation, not a new live spawn/settlement receipt. The verifier is intentionally fixed-selector and does not claim generic provider coverage.
