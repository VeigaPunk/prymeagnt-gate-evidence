# Round 2 explicit-selector admission receipt — 2026-10-11

Question: does a lane-owned RLM child pinned to the permitted OpenAI selector admit, expose model provenance, and settle with the requested reply?

## Reproduction and evidence

- Selector lookup: `await rlm.find_models("openai-codex/gpt-6-luna")` returned provider `openai-codex`, selector `openai-codex/gpt-6-luna`.
- Spawn: `await rlm.spawn("Reply with exactly: rlm-dispatch-round2-ok", name="rlm-dispatch-r2-probe", model="openai-codex/gpt-6-luna")` returned child ID `sub-52e968c6`, handle model `openai-codex/gpt-6-luna`.
- Registry `rlm-subagent.json`: `model.provider=openai-codex`, `model.modelId=gpt-6-luna`, final `status=completed`.
- Child session log `01a12d0c-e484-7627-b92e-d6138e736572.jsonl`: first `model_change` is provider `openai-codex`, modelId `gpt-6-luna`; final assistant message is exactly `rlm-dispatch-round2-ok`, stopReason `stop`.
- Settlement: `await rlm.collect([probe], timeout_ms=0)` eventually returned `status='done'`, `settled=True`, `answer_preview='rlm-dispatch-round2-ok'`, `error=None` (duration 49,509 ms). Early polls showed running/unsettled; one idle-agent observation did not mean terminal completion. Continue collection until terminal.
- Child sent the exact reply through `agent_message`; transcript response was also captured in the session log.

The session-artifacts path and timestamps are intentionally omitted. The child was self-owned, depth-2, and read-only. No alternate provider/model was attempted.
