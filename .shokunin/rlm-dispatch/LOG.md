# rlm-dispatch append-only log

## Mint 2026-10-11
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: `.shokunin/mints/rlm-dispatch.md`; sources: `.shokunin/rlm-dispatch/corpus/knowledge/seed.md`.
- Next falsifiable move: execute one bounded read-only task, cite before/after, and have L1 judge every owned axis.


## Round 1 — 2026-10-11
- Added an explicit-selector admission decision table, distinguishing lookup from admission and settlement evidence; corpus entry cites capability survey, smoke procedure, and rerun receipt.
- Live `rlm.find_models("OpenAI", limit=20)` returned selector `openai-codex/gpt-6-luna` (also `openai-codex/gpt-6-sol`). No lane-owned spawn was performed. The parent-provided receipt identifies child `sub-9bfd0406`; durable explicit-selector admission evidence is in `verification/smoke-test-rerun-20261011.log`.
- Operability: improved (live exact-selector discovery, parent-reported completed scout, and durable published explicit-selector receipt support an actionable decision table; the ephemeral scout registry itself was not independently inspected). Calibration: unchanged (no new runtime admission evidence to test calibration).

## L1 closure correction — round 1
- Supersedes the preceding optimistic operability verdict: the pre-existing published receipt count stayed **1 → 1** at baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a` and work commit `f12210537e8b2f0246c78547a82f28feb7cd2c62` using `grep -c "Smoke test 2 rerun" verification/smoke-test-rerun-20261011.log`. Operability is **unprovable-but-better**, calibration **unchanged**. The decision table is useful but its assigned receipt-count claim did not improve. L1 does not admit round 1; retain the work as a candidate and run a genuinely independent admission exercise in a subsequent round.

- Evidence: `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-selector-admission.md`; live REPL output; parent request sent through `agent_message`.

- Parent later supplied corroboration: child `sub-9bfd0406`, explicit `openai-codex/gpt-6-luna` selector, reported completed via `rlm.list_subagents()` plus child `agent_message`; ephemeral registry was not independently inspected. Durable prior explicit-selector evidence remains the published rerun log. This does not establish a lane-owned spawn.
