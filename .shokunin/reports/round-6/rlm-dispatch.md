# rlm-dispatch — round 6

## Question and findings

Tested whether the exact-single-reply check materially misclassifies documented `rlm.collect` receipts, and whether the verifier accepts a registry/collect status mismatch.

- The installed runtime source defines `RLMChildResult.answer_preview: str | None` and `collect()` parses it as an optional string (`/home/vgpnk/.local/share/prime-agent/prime-agent-runtime/src/rlm/__init__.py`, lines 84–96, 399–432). The public collect docstring documents status/settlement behavior, but does not document preview truncation or guarantee preview equals the full transcript reply.
- Found `ANSWER_CAPTURE_CAP = 200` and truncation in `factory.py` lines 1007, 1313, 2712; that is a separate factory-state capture path, not evidence that `rlm.collect` truncates `answer_preview`. Applying it as collect behavior would be speculative.
- The verifier independently requires registry `status == completed` and collect `status == done` plus `settled is True`. These are separately documented fields/vocabularies (the round-2 cited receipt records both); no source/corpus evidence establishes that they should be equal. A mixed status cannot be called a false accept from evidence available here.
- Current baseline reproduced: the seven documented fixtures exit `0/1/0/1/1/0/1` in README order. The exact-reply mismatch fixture is rejected; it provides no evidence of a valid truncated preview.

No material false accept or false reject was established. Therefore no speculative verifier check or fixture was added; seven exits are retained. Operability and calibration: unchanged / no-axis advance. No live runtime probe was performed.

## Reproduction / source references

`python3 .shokunin/rlm-dispatch/corpus/verification/verify_receipt.py` with the seven fixture triples documented in `corpus/verification/README.md` produced exits `0,1,0,1,1,0,1`. Runtime source was read-only; relevant locations are as cited above.

## Bounds

Only this round report was added. No verifier, fixture, corpus, scorecard, manifest, global harness, or runtime source was changed. No provider policy or usage-depletion claim.
