# RLM dispatch — round 14 report

## Move
Operability improved narrowly: `verify_receipt.py` now catches `UnicodeDecodeError` only at registry/settlement JSON decoding and session JSONL decoding. Each returns a generic `FAIL: input contains invalid UTF-8 encoding`, exit 1, with no traceback. Calibration is unchanged: no accepted-input criteria or authentication checks changed.

## Evidence
Native Python 3.14.2 on synthetic local fixtures. At each isolated boundary, only the target file contains invalid UTF-8 (`b"{\xff"`); other receipt files are copied valid positive data with registry `sessionFile` corrected to the local copied session. Baseline source is extracted from base `9804b13`.

| input boundary | baseline | current |
|---|---|---|
| registry | exit 1, uncaught `UnicodeDecodeError` traceback | exit 1, generic FAIL, no traceback |
| session JSONL | exit 1, uncaught `UnicodeDecodeError` traceback | exit 1, generic FAIL, no traceback |
| settlement | exit 1, uncaught `UnicodeDecodeError` traceback | exit 1, generic FAIL, no traceback |
| copied valid positive | PASS / 0 | PASS / 0 |

Regression controls (baseline/current exits): original nine `0/1/0/1/1/0/1/1/1`; R10 duplicate registry/session/settlement + unique positive `1/1/1/0`; R11 malformed-shape negatives + positive `1/1/1/1/0`; R12 malformed-syntax registry/session/settlement + valid positive `1/1/1/0`.

## Limits
Synthetic local inputs only. No provider, daemon, authentication, or live runtime operation was invoked. No claim about filesystem I/O errors, which remain uncaught, or behavior for encodings other than invalid UTF-8.


## Fixture portability correction (after integration smoke)
The initial R14 fixture copy stored absolute `sessionFile` paths from the isolated worktree. Integration smoke found that three paths were non-portable after replay. Corrected `utf8-session-only`, `utf8-settlement-only`, and `utf8-unique-positive` registries to use repository-root-relative `.shokunin/rlm-dispatch/corpus/verification/fixtures/.../session.jsonl` paths, consistent with the verifier's documented invocation from the repository root. This supersedes any prior implication that all fixture copies were portable as committed. Re-ran all four R14 fixture commands from the isolated repository root: the three malformed inputs return generic FAIL/exit 1, and the unique positive passes/exit 0. The path adjustment changes no verifier behavior or verdict; no integration merge/push was performed.
