# gate-evidence — round 3

## Work performed
- Added source-backed autonomous retry-ceiling and passed-gate/unmet-goal rows, distinct from the existing baseline/candidate table: `.shokunin/gate-evidence/corpus/knowledge/gate-decision-table.md:13-18`; sources `docs/ufo-workflow.md:50-63,202-215`, `docs/capability-survey.md:86-96`, `skills/ufo/references/run-logic.md:443-455`.
- Added two deterministic synthetic fixtures, a read-only parser, and recorded actual outputs: `.shokunin/gate-evidence/corpus/fixtures/autonomous-cases.json:1-29`, `.shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py:1-43`, `.shokunin/gate-evidence/corpus/fixtures/autonomous-actual.json:1-20`. Both cases leave the terminal `loop_stop` unclassified; neither calls a live gate.
- Re-ran both fixture checkers and an independent JSON expected/actual comparison at `f6bb1ce0e5f313dfd1c76c91248eb1fde082dbc8`: `python3 .shokunin/gate-evidence/corpus/fixtures/check_gate_cases.py` exit 0 (7 cases); `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` exit 0 (2 cases); `python3 -c 'import json,pathlib; p=pathlib.Path(".shokunin/gate-evidence/corpus/fixtures"); e=json.loads((p/"autonomous-cases.json").read_text()); a=json.loads((p/"autonomous-actual.json").read_text()); assert a == [f["expected"] for f in e]; print("independent expected/actual comparison:",len(a),"/",len(e))'` printed `independent expected/actual comparison: 2 / 2`.
- Recorded both owned-axis verdicts and an unapplied global-triple refinement proposal in `.shokunin/gate-evidence/LOG.md:24-28`. No sub-lanes warranted for this two-fixture read-only change; L2 lanes **not-dispatched**. No live autonomous mission or gate run, no `goal.complete()`, no GitHub push.

## Landed changes
- Corpus decision rows, fixtures, checker and index: `.shokunin/gate-evidence/LOG.md:25-27`, carried by `8bbcd4aad1d2b75970c4c185300318d5bb0e47d9`.
- Append-only round log and scorecard evidence update: `.shokunin/gate-evidence/LOG.md:24-28`, `.shokunin/gate-evidence/SCORECARD.md:7`, carried by `f6bb1ce0e5f313dfd1c76c91248eb1fde082dbc8`.

## Before → after measurements
- **Coverage: improved** for synthetic branch coverage only. At `d88b2eaee128252b4bf7ae497f9edee4001c833d`, `git show d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/gate-cases.json | python3 -c "import json,sys; print(len(json.load(sys.stdin)))"` printed `7`; `git cat-file -e d88b2eaee128252b4bf7ae497f9edee4001c833d:.shokunin/gate-evidence/corpus/fixtures/autonomous-cases.json` exited 128 (absent; 0 autonomous fixtures). At `f6bb1ce0e5f313dfd1c76c91248eb1fde082dbc8`, `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` printed two distinct A0/A1 classifications; independent command above printed `2 / 2`. Existing seven-case checker remained green.
- **Calibration: unchanged**. `python3 .shokunin/gate-evidence/corpus/fixtures/check_autonomous_cases.py` and independent JSON comparison pass at `f6bb1ce0e5f313dfd1c76c91248eb1fde082dbc8`, but synthetic fixture agreement does not establish live runtime gate behavior. `docs/ufo-workflow.md:57-63` gives a bounded retry count, not a terminal `loop_stop` mapping; `skills/ufo/references/run-logic.md:443-455` separates stop and goal. No live mission completed or verifier applied to this round.

## SHONEN
- [x] Real decision tables/error patterns/checklists with cited sources — non-author verifiers `round1-independent-review` at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` and `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f`; prior verification only, not a new review.
- [ ] End-to-end domain task executed and logged — no live gate or goal task, no non-author verifier.
- [x] Instructions executable without oral context — non-author verifier `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f`; prior verification only.
- [x] No cross-domain bleed and PROVINCE accurate — non-author verifiers `round1-independent-review` at `65a1d7b8215bf1bb764c0c9957f217a930f27b78` and `round2-independent-review` at `68b425729ffbceb2d4fdfc59d1e154a52360de3f`; prior verification only.

## Proposed self-refinement (not applied)
Global triple delta: memory records retry-ceiling versus passed-gate/unmet-goal with the cited uncertainty; skill requires independently compared deterministic fixtures for a synthetic coverage claim; spec forbids inferring `budget_halt` from retry exhaustion without observed `limitReason`. Falsification: current source or live telemetry deterministically maps retry exhaustion to a terminal stop, or independent fixture comparison fails. L1 must authorize any global harness update. No open operator question; no `.shokunin/l0-questions.md` change.
