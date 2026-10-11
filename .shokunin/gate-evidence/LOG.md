# gate-evidence append-only log

## Mint 2026-10-11
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: `.shokunin/mints/gate-evidence.md`; sources: `.shokunin/gate-evidence/corpus/knowledge/seed.md`.
- Next falsifiable move: execute one bounded read-only task, cite before/after, and have L1 judge every owned axis.

## Round 1 — 2026-10-11 — coverage move
- Claim: baseline has no structured decision table; after, one sourced table distinguishes untouched-tree baseline failure, candidate failure, unmet, unverified, and met acceptance conditions. Corpus work commit: `a257b4b35f7718a70eec0f0f31fc70cfeba4538d`. Sources: `skills/ufo/references/run-logic.md:158-174,419-455,512-524`; `docs/ufo-workflow.md:33-34,50-63,202-215`.
- Measured baseline: `git cat-file -e 44a08fd0eeb22c7ed9766aae4675dd452eff232a:.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` exits 128 (no file, 0 rows). Measured after at `a257b4b35f7718a70eec0f0f31fc70cfeba4538d`: `grep -Ec '^\| (B0|C0|G0|G\?|G1) \|' .shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` prints 5.
- Coverage verdict: **improved** — the documented cases now separate baseline, candidate, and mission-goal outcomes; this verdict concerns documentation, not live runtime correctness.
- Calibration verdict: **unchanged** — cited decision sources and caveats constrain claims, but no live gate, acceptance check, or independent reviewer was run. No `goal.complete()` invoked; no goal success claimed.
- Accepted corpus change: `a257b4b35f7718a70eec0f0f31fc70cfeba4538d`. No score invented; no SHONEN box self-verified. Next falsifiable move is a separately authorized read-only exercise with recorded gate-result fixtures and an independent reviewer.
