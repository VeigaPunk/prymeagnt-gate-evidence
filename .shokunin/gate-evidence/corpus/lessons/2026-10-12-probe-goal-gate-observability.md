# 2026-10-12 — Probe: goal/gate observability in session artifacts (operator-run)

Follow-up to r20 (which closed no-axis: root goal.get() null, no host gate
receipts). Operator ran a direct probe instead of spending another lane round.

## Question
Does an autonomous mission's session JSONL record goal-lifecycle or
completion-gate execution events anywhere?

## Method
The r20 mission's own root session artifact was audited:
`~/.prime/agent/sessions/01a12f8d-4197-76bb-94c9-45789cc09143.jsonl`
(cwd gate-evidence/r19-budget, 668 messages, autonomous run with four
completion gates, 2026-10-12 09:59-10:30Z).

## Finding
- goal-state custom events: **0**
- gate/autonomous custom events: **0**
- event types present: session, model_change, thinking_level_change,
  service_tier_change, session_state, message, custom_message (1)

The goal lifecycle and gate executions are written to NO inspectable session
artifact on 0.10.0. Combined with r20 (goal.get() null even for the session's
own seeded goal), the goal/gate lifecycle is observable only through external
operator surfaces (`prime-agent sessions`, the exit report).

## Consequence for box 2
SHONEN box 2 (end-to-end domain task executed and logged) remains unchecked
and is now substrate-pinned: no artifact pathway exists to log a real
gate/goal lifecycle. Not a lane defect.

## Substrate asks (operator-owned)
1. Write gate execution receipts (argv, exit, timestamp) to the session JSONL.
2. Write goal state transitions to the session JSONL (thread_goal_state was
   recorded in the 06:52 pre-pty seed attempt but not in the live mission —
   bind goal events into the artifact unconditionally).
3. Make goal.get() return the root session's own goal (it returned null).
