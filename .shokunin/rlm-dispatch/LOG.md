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

## Round 2 — 2026-10-11
- Executed one self-owned read-only child probe with explicit `openai-codex/gpt-6-luna`; handle, registry, model_change, child reply, and terminal collect receipt agree. Early collect polls remained running despite child briefly appearing idle; terminal status was later observed by re-polling.
- Durable redacted receipt: `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-round2-admission.md`; corpus index row appended in `.shokunin/rlm-dispatch/corpus/README.md`.
- Operability: improved (first independently performed, durable lane-owned selector-admission and terminal-settlement receipt; count 0 → 1 in assigned round-2 receipts corpus, command/report details). Calibration: improved (independent runtime admission and terminal evidence confirms the procedure's distinction between admission, transient idle, and settlement). These are lane proposals; L1 judges.
- No >=8 wave: assignment specifies one bounded self-owned probe, not a multi-lane task.

## Independent review receipts — rounds 1–2
- `round1-independent-review` at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` verified sourced admission table and owned province, but no new lane-owned spawn (boxes 2/3 deferred). `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f` independently read depth-2 child transcript and registry: openai-codex/gpt-6-luna model_change, exact `rlm-dispatch-round2-ok` reply and parent collect done/settled=True/error=None after 49,509ms. Recommends SHONEN boxes 1–4 for bounded explicit-selector admission/settlement only. L1 records verifier names; rank remains shonen until >=3 verified rounds.

## Round 3 — 2026-10-11
- Added a read-only fixed-selector receipt verifier and sanitized positive/negative fixtures at `corpus/verification/`; reproducible command and checks are in the round-3 report.
- Validation outcome: positive fixture accepted (exit 0); wrong provider/model plus running/unsettled fixture rejected (exit 1). This is synthetic fixture evidence, not a new runtime admission receipt.
- Operability: improved (a reusable local verifier now detects wrong routing and unsettled receipts; baseline had no verifier). Calibration: unchanged (no additional live admission/settlement observation; fixture checks only validate the verifier implementation).
- Proposed harness self-refinement: add an RLM-dispatch procedure requiring local sanitized fixture-based checks after runtime receipts, with explicit separation of synthetic verifier tests from live admission evidence. Falsification: reject this proposal if a subsequent independent lane cannot reproduce the positive/negative exits from the documented command on the committed fixtures, or if the verifier mutates inputs / makes network calls. Awaiting L1 approval; no global harness edit made.
