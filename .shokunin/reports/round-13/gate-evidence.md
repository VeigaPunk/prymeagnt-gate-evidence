# Round 13 — RFC3339 arbitrary fractional precision

## Scope and cited rule

RFC3339 §5.6 defines `time-secfrac = "." 1*DIGIT`, with no six-digit ceiling. The projection retains its existing total timestamp limit of 40 characters. This round corrects a false negative for otherwise-valid long fractions without changing the UTC-only policy. Source: [RFC 3339 §5.6](https://www.rfc-editor.org/rfc/rfc3339#section-5.6).

## Change and verification

Work commit: `72b83f7b1419f2635a9207f284363b8f14a10a9c`. The parser validates the same strict timestamp grammar, truncates only a temporary validation copy to at most six fractional digits for Python `datetime`, and returns the original timestamp exactly. `-00:00` remains rejected; calendar dates and second 60 remain subject to existing datetime validation/rejection.

`python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py` passed (exit 0), including exact-preservation positive cases at 7 and 20 fractional digits with `Z` and `+00:00`, invalid 2023-02-29 with seven digits, leap second 60 negative, and prior syntax/offset/precision controls. Each accepted case executes the pinned read-only Git gate. `git diff --check` passed before work commit; report-last diff check follows.

Explicit limitation: this is not leap-second completeness and does not prove host autonomous gate behavior, acceptance, or mission success.

## Proposed axis judgment (L1 decision pending)

- **Coverage: improved.** Inputs conforming to RFC3339 arbitrary fractional width, within the existing total length cap, are now accepted and preserved exactly. New native contract cases exercise 7/20 digits and invalid calendar/leap second controls.
- **Calibration: unchanged.** Existing syntax, UTC-offset, date, leap-second, null, injection and gate controls remain; this broadens precision acceptance only. Evidence is synthetic/native parser contract testing, not host-gate proof.

No MANIFEST/global harness changes or push. No gate mutation or host autonomous proof claimed.


## Append-only correction — precision boundary (2026-10-12)

The original summary incorrectly said “20 fractional digits with `Z` and `+00:00`.” A 20-digit `Z` timestamp is 41 characters and cannot pass the existing 40-character whole-timestamp limit; the prior fixture actually tested 14 digits with `+00:00`. The observed accepted fractions are 7 and 19 digits with `Z`, and 14 digits with `+00:00`. Added native control confirms 20 digits with `Z` is rejected by the 40-character limit. “Arbitrary precision” means any fraction length that fits the existing whole-timestamp cap, not unbounded digits. New boundary work commit: `ae613ad428375ad4b81dd963f3718e329c6a934f`; contract checker passed exit 0. This correction supersedes only the erroneous digit counts above; axis judgments and limitations are unchanged.
