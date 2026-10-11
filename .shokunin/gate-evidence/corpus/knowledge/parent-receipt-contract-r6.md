# R6 parent-owned receipt: status/UTC clock alongside a read-only gate process

The child `goal.get()` of R5 is local to that child. **Only L1 can read its own goal** in its own persistent REPL. L1 may create a *redacted projection* without saving the raw `goal.get()` response or objective. In L1's REPL:

```python
from datetime import datetime, timezone
snapshot = await goal.get()                 # L1's own session only
local_goal = snapshot.get("goal")
projection = {"observed_utc": datetime.now(timezone.utc).isoformat(),
              "goal": None if local_goal is None else {
                  key: local_goal.get(key) for key in
                  ("status", "tokens_used", "time_used_seconds", "token_budget")}}
# Inspect projection in memory. Do not persist/forward snapshot, objective, timestamps or IDs.
```

L1 chooses whether to provide that projection as standard input to `python3 .shokunin/gate-evidence/corpus/live/compare_parent_receipt.py --base <full-40-hex-commit> --candidate <full-40-hex-commit>` from the repository root. Provide the *in-memory* JSON through a trusted L1-owned standard-input channel; do not put JSON in a command-line argument, shell history, or a file. The checker accepts **exactly** `observed_utc` plus a `goal` of `null` or exactly four allowlisted fields; it rejects objective, identifiers, extra keys, invalid clock, and invalid status. L1 owns its decision to retain or discard the printed receipt. Parent status is claimed as **parent-supplied**, never authenticated by this child script. This is not a route to query L1 from a child, and no parent projection was supplied during R6.

The script runs an actual local `git diff --check <base> <candidate>` process after validating two immutable commit IDs and captures gate start/end UTC and exit. Exit 0 means *only* that this Git whitespace check passed for that revision range; it is **not** evidence that the configured host `--autonomous-gate` ran or passed. The process can fail if Git is unavailable, revisions are invalid, or whitespace is flagged; its failure does not prove mission failure. No Git tree, gate configuration, goal, or autonomous state is mutated. Gate stdout/stderr and path details are deliberately omitted from the receipt. No implicit time alignment: status was read before invocation; no causal relation between independent observations is established. A nonzero exit returns nonzero while still printing a gate receipt labelled `nonzero-unclassified` (it may reflect whitespace or a process error).

Test from the repo root: `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py`. It supplies a **synthetic** parent projection, checks positive/null parses, rejects an objective/secret injection and a non-UTC clock before gate execution, observes real read-only Git check exit 0 on pinned commits, and independently runs a stdin whitespace negative-control process that returns nonzero with a whitespace diagnosis. This verifies the *contract and process parser*, **not actual parent status**. If L1 supplies a redacted projection later, independently rerun the tool and compare its JSON to L1's in-memory projection and UTC clock; only then cite an actual parent-owned status receipt. There is no actual parent-provided process/status pair in R6.

The receipt deliberately fixes `autonomous_gate`, `acceptance`, `loop_stop`, and `mission_goal` to `not-assessed`, whether goal status is active, null, completed, or budget-limited and whether Git returns 0 or nonzero. No `goal.complete()` call follows from it. Actual autonomous-gate state requires host telemetry for the same root/model inference; acceptance requires measured final criteria; stop classification requires its own limit/stop receipt. The separate fresh isolated root/model inference and operator authority remain unresolved.

Sources: `skills/goal/SKILL.md` (`goal.get` read shape and local goal); `docs/capability-survey.md:83,86-96` (root goal and autonomous telemetry); `docs/ufo-workflow.md:50-63,202-215` and `skills/ufo/references/run-logic.md:407-455,512-524` (gate versus criteria versus stop). Related prior evidence: `goal-read-boundary-r5.md`, `../live/observed-child-goal-r5.json`, `../live/observed-bc1bb3c.json`.
