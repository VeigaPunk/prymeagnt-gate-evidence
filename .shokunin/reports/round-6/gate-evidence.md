# Gate-evidence round 6 — calibration

## Work performed
- Established parent-owned, objective-free projection and UTC clock contract in `.shokunin/gate-evidence/corpus/knowledge/parent-receipt-contract-r6.md`; an L1 read of **its own** `goal.get()` is required, never a child read.
- Added `.shokunin/gate-evidence/corpus/live/compare_parent_receipt.py`: allowlisted stdin parser, immutable commit IDs, actual non-mutating `git diff --check` process, process timestamps and sanitized exit receipt. Explicitly sets autonomous gate, acceptance, `mission_goal` and `loop_stop` to `not-assessed`.
- Added `.shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py`: synthetic active/null redacted inputs, rejected objective/secret and non-UTC input, actual pinned Git process pass, independent stdin whitespace negative control nonzero.

## Landed changes
- `LOG.md` R6 entry and `SCORECARD.md` R6 calibration evidence plus the three corpus files committed as `df2dfc7b2c26483c30c71f4a5dcd54d939484570` by `gate-evidence-shonen <gate-evidence@shokunin.local>`. No MANIFEST, source, global harness, or goal change; no push.

## Before → after measurements
- Before `6c75ea3d90d8a328d8de72b39b57e9b04a40a782`: `git cat-file -e 6c75ea3:.shokunin/gate-evidence/corpus/live/compare_parent_receipt.py` exits 128 (file absent). After work commit `df2dfc7b2c26483c30c71f4a5dcd54d939484570`: `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` exit 0, prints `synthetic parent projection: positive and null parsed; real read-only Git gate exit 0; stdin whitespace negative control failed as expected; objective/secret injection and non-UTC timestamp rejected without receipt`; `git diff --check 6c75ea3d90d8a328d8de72b39b57e9b04a40a782 df2dfc7b2c26483c30c71f4a5dcd54d939484570` exit 0, empty stdout.
- **Calibration: improved**, narrowly for reproducible scoped parent-owned receipt contract and actual benign gate-process check with negative control; only synthetic projection was supplied. **Coverage: unchanged**, no additional decision branch. No live parent goal data, configured host autonomous gate, actual acceptance, stop telemetry, or full end-to-end mission observed. The parser's injected synthetic `active` status is not evidence of the parent's goal. An actual parent-supplied redacted status/process comparison remains unrun.

## SHONEN
- [x] Real cited decision tables; non-author `round1-independent-review` / `round2-independent-review`, `LOG.md` independent review receipts.
- [ ] End-to-end domain task; no actual L1 status or host autonomous-gate observation; non-author verifier required.
- [x] Executable instructions; non-author `round1-independent-review` / `round2-independent-review`, `LOG.md` independent review receipts. R6 additions not independently verified.
- [x] Province boundary accurate; non-author `round1-independent-review` / `round2-independent-review`, `LOG.md` independent review receipts. No R6 promotion asserted.
