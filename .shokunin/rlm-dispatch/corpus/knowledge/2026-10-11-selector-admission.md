# Explicit-selector admission decision table

Round 1 asked whether the live model selector can be checked and whether this lane has an independently visible completed spawn receipt. The first is checkable; the second requires a parent-provided runtime receipt and was not present at inspection.

## Decision table

| Need | Evidence/action | Decision |
|---|---|---|
| Select a supported exact model string | `rlm.find_models("OpenAI", limit=20)`; choose the returned `.selector`, not a display name or inferred alias. Live result included `openai-codex/gpt-6-luna` and `openai-codex/gpt-6-sol` (OpenAI Codex provider). | Selector availability confirmed at lookup time only; availability is not proof of admission. |
| Pin a child to that route | Pass the exact selector as `model=` to `rlm.spawn(prompt=..., name=..., model=<selector>)`. The runtime API contract is listed in `docs/capability-survey.md` §2.1. | Do not rely on omitted model: `docs/smoke-testing.md` Test 2 / `verification/smoke-test.log` F1 document inheritance behavior in 0.10.0. |
| Establish child admission | Preserve the returned handle's `model` plus the child registry `rlm-subagent.json` model object and child-session `model_change` event. | Matching evidence is an admission receipt; model discovery alone is not. This lane did not independently observe a new spawn. |
| Establish settlement | Poll `rlm.collect` until `status == 'done'`, `settled is True`, and `error is None`; retain reply/answer preview. | A single `collect(timeout_ms=...)` call is not proof of settlement (`docs/smoke-testing.md` Test 2, finding F3). |
| OpenAI-only constraint | Check the returned `RLMModel.provider`/selector and handle/registry provider; reject `prime-inference/...` even if the model label looks OpenAI. | Provider identity must be evidenced, not guessed from model naming. |

## Round observation and limits

- Live lookup in this RLM session returned `openai-codex/gpt-6-luna` (`gpt-6-luna`) and `openai-codex/gpt-6-sol` (`gpt-6-sol`); it also returned Prime Inference selectors, which are not OpenAI Codex routes.
- A completed prior explicit-selector receipt exists in the published source log: `verification/smoke-test-rerun-20261011.log`, “Smoke test 2 rerun”, handle/registry/session evidence for `openai-codex/gpt-6-luna`, settled `done`, reply `subagent-ok`. It is historical evidence from another run, not a new spawn by this lane.
- Parent later provided a scout receipt: child `sub-9bfd0406` was spawned with `model="openai-codex/gpt-6-luna"`; the parent reports handle.model matched, `rlm.list_subagents()` showed completed, and child `agent_message` supplied cited F1/F3 findings. I did not independently inspect that ephemeral registry, and the child did not report its own `model_change` / registry details. Use the published rerun log as the durable receipt; do not represent this as a lane-owned spawn.

Sources: `docs/capability-survey.md` §2.1; `docs/smoke-testing.md` Test 2 and “Collect re-poll”; `verification/smoke-test-rerun-20261011.log` Smoke test 2 rerun.
