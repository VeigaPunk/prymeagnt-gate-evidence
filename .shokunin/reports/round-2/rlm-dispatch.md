# rlm-dispatch — round 2 report

## Work performed
- Resolved the allowed OpenAI selector using live model discovery; lookup returned `openai-codex/gpt-6-luna` from provider `openai-codex` (REPL output; round-2 receipt).
- Spawned one self-owned depth-2 child pinned to that selector; its handle, registry, and session `model_change` agree on `openai-codex/gpt-6-luna` (`.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-round2-admission.md`; commit `828e17c7403917b80a26d3c1004232effa1166bd`).
- Re-polled collection through transient running/idle observations to terminal `done`, `settled=True`, `error=None`; exact reply captured as `rlm-dispatch-round2-ok` (same receipt and child session transcript).
- Added one redacted reproducible receipt and index row; appended round 2 log and updated proposed owned-axis scorecard (commit `828e17c7403917b80a26d3c1004232effa1166bd`).
- Opened the L0 question about idle child versus running collect state in `.shokunin/l0-questions.md`; routed around it by re-polling to terminal rather than waiting.

## Landed changes
- Round-2 receipt and corpus index: `LOG.md` round 2; commit `828e17c7403917b80a26d3c1004232effa1166bd`.
- Round-2 log and proposed scorecard: `LOG.md` round 2; commit `828e17c7403917b80a26d3c1004232effa1166bd`.

## Before → after measurements
- Independently captured lane-owned selector-admission receipt entries: baseline `65a1d7b` count 0 → commit `828e17c7403917b80a26d3c1004232effa1166bd` count 1. Counting command: `git show 65a1d7b:.shokunin/rlm-dispatch/corpus/README.md | grep -c 'lane-owned explicit-selector admission'` versus `grep -c 'lane-owned explicit-selector admission' .shokunin/rlm-dispatch/corpus/README.md`. This measures durable receipts, not all runtime capability.

## Axis verdicts
- Operability: **improved** (one verifiable lane-owned explicit-selector admission and terminal-settlement receipt; evidence in corpus receipt, commit `828e17c7403917b80a26d3c1004232effa1166bd`).
- Calibration: **improved** (independent handle, registry, model-change, and completed-collect evidence; observed transient idle/running state correctly treated as unsettled until terminal; corpus receipt at same commit).

## SHONEN
- [~] Real decision tables/error patterns/checklists with cited sources; non-author verifier required — pointer: `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-selector-admission.md` (prior table) and `2026-10-11-round2-admission.md` (cited runtime evidence); no named non-author verifier this round.
- [~] End-to-end domain task executed and logged; non-author verifier required — pointer: lane-owned probe and settlement receipt at `.shokunin/rlm-dispatch/corpus/knowledge/2026-10-11-round2-admission.md`; no named non-author verifier.
- [~] Instructions executable without oral context; non-author verifier required — pointer: explicit reproduction commands and terminal criteria in `2026-10-11-round2-admission.md`; no named non-author verifier.
- [~] No cross-domain bleed; PROVINCE remains accurate; non-author verifier required — pointer: only RLM selector/admission/settlement touched, `.shokunin/rlm-dispatch/PROVINCE.md` unchanged; no named non-author verifier.

## Constraints and attribution
- This round executed one requested bounded probe; no eight-lane wave was warranted by the assigned one-probe test.
- Lane verdicts are proposals for L1 judgment. Only OpenAI Codex `gpt-6-luna` was spawned; no fallback provider was used.
- Pre-report work commit: `828e17c7403917b80a26d3c1004232effa1166bd`.
