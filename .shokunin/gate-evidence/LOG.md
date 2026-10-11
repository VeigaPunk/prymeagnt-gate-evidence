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

## Round 2 — 2026-10-11 — calibration move
- One falsifiable claim: baseline at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` has 0 independently exercised classifications (fixture file absent); after, the ordered table classifies baseline-failed/unrun, candidate-failed/unrun, goal-unmet/unverified/met synthetic inputs and an independent expected/actual comparison reports 7/7. Fixture work commit: `86fb105a888dd77d138a482faecdc21f22baefcc`.
- Measurement: `git cat-file -e 65a1d7b8215bf1bb764c0c9957f217a930f27b78:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json` exits 128 (absent); `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` exits 0 and prints seven results; independent `python3 -c 'import json,pathlib; p=pathlib.Path(".shokunin/gate-evidence/corpus/fixtures"); e=json.loads((p/"gate-cases.json").read_text()); a=json.loads((p/"actual.json").read_text()); assert a == [f["expected"] for f in e]; print("independent expected/actual comparison:",len(a),"/",len(e))'` prints `independent expected/actual comparison: 7 / 7`. Inputs, expected and actual outputs: `corpus/fixtures/gate-cases.json`, `corpus/fixtures/actual.json`; executable checker: `corpus/fixtures/check_gate_cases.py`.
- Calibration verdict: **improved** for deterministic fixture validation against the cited table; **not** evidence of live gate correctness, actual acceptance, or goal completion. Coverage verdict: **unchanged** — no new policy branch or source scope. No gate invocation or `goal.complete()` call.
- Accepted corpus change: `86fb105a888dd77d138a482faecdc21f22baefcc`; next falsifiable move requires operator-approved real gate observations or a separate independent non-author verifier, never an inferred goal success.

## Independent review receipts — rounds 1–2
- `round1-independent-review` at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` independently counted five cited decision rows and verified own province scope; recommends SHONEN boxes 1 and 4. `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f` reran fixture checker 7/7 and confirms standalone synthetic procedure (box 3); box 2 remains unchecked because no live gate/goal task was executed. Fixture expected/actual match is table consistency, not an independent runtime oracle. Rank remains shonen.
