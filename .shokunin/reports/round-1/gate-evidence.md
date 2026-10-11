# gate-evidence — round 1

## Work performed
- Re-read the installed shokunin contract and read-only domain sources; `skills/ufo/references/run-logic.md:158-174,419-455,512-524` and `docs/ufo-workflow.md:33-34,50-63,202-215` establish baseline, candidate, and goal distinction.
- Added a first-match, five-case read-only decision table, `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:1-15`; indexed at `.shokunin/gate-evidence/corpus/README.md:6`. No project gate was executed and no `goal.complete()` call was made.
- Recorded measurements and separate owned-axis verdicts at `.shokunin/gate-evidence/LOG.md:8-13` and `.shokunin/gate-evidence/SCORECARD.md:3-11`. No sub-lanes were warranted for this bounded source-reading move; none were dispatched.

## Landed changes
- Decision table and index, LOG round-1 entry `.shokunin/gate-evidence/LOG.md:8-13`, corpus commit `a257b4b35f7718a70eec0f0f31fc70cfeba4538d`.
- Scorecard and append-only LOG verdict entry `.shokunin/gate-evidence/LOG.md:8-13`, books commit `d9c17935263a101aa93e83e2b3aafe728b7b7a46` (`git rev-parse HEAD` when this report was written). Both commits use the lane identity.

## Before → after measurements
- Coverage claim: `git cat-file -e 44a08fd0eeb22c7ed9766aae4675dd452eff232a:.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` exits 128, so baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a` has **0 rows** in that nonexistent file. `grep -Ec '^\| (B0|C0|G0|G\?|G1) \|' .shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md` prints **5** at corpus commit `a257b4b35f7718a70eec0f0f31fc70cfeba4538d` and at books commit `d9c17935263a101aa93e83e2b3aafe728b7b7a46`. Verdict: **improved** for documented coverage, not verified runtime behavior. Source references are in each row, `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:7-11`.
- Calibration: baseline seed explicitly disclaimed a run (`.shokunin/gate-evidence/corpus/knowledge/seed.md:7`, baseline `44a08fd0eeb22c7ed9766aae4675dd452eff232a`); after table explicitly disclaims runtime or goal success (`.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:3,13-15`, commit `a257b4b35f7718a70eec0f0f31fc70cfeba4538d`). Source/caveat review only; no live gate or acceptance check was run. Verdict: **unchanged**; an unrun check is not passed. No calibration improvement asserted.

## SHONEN
- [~] Real decision table exists at `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:5-11`; no named non-author verifier yet.
- [ ] End-to-end domain task executed and logged: untouched; only read-only source evaluation performed.
- [~] Instructions have reproducible count commands at `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:15`; no named non-author verifier yet.
- [~] Boundary remains in `.shokunin/gate-evidence/PROVINCE.md:3-9`; no named non-author verifier yet.

No operator question or contested scope arose. No remote push, global harness mutation, MANIFEST edit, or domain-source edit was made; L1 owns those actions.
