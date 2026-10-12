#!/usr/bin/env python3
"""Synthetic input contract tests; each accepted run executes a real Git diff gate."""
import json
from pathlib import Path
import subprocess
import sys

SCRIPT = Path(__file__).with_name("compare_parent_receipt.py")
BASE = "52d573bdf502cb1416d65c0756106db9d5b3bde2"
CANDIDATE = "bc1bb3c572981158f8ac0b4994d3333741650886"


def run(snapshot):
    return subprocess.run([sys.executable, str(SCRIPT), "--base", BASE, "--candidate", CANDIDATE],
                          input=json.dumps(snapshot), text=True, capture_output=True, check=False)


def main():
    synthetic = {"observed_utc": "2026-10-11T00:00:00+00:00",
                 "goal": {"status": "active", "tokens_used": 8,
                          "time_used_seconds": 1.5, "token_budget": 100}}
    accepted = run(synthetic)
    assert accepted.returncode == 0, accepted.stderr
    result = json.loads(accepted.stdout)
    assert result["goal_snapshot"] == {"observed_utc": synthetic["observed_utc"],
                                         "goal_present": True, **synthetic["goal"]}
    assert result["gate"]["exit_code"] == 0
    assert result["gate"]["base"] == BASE and result["gate"]["candidate"] == CANDIDATE
    assert all(result[k] == "not-assessed" for k in
               ("autonomous_gate", "acceptance", "loop_stop", "mission_goal"))
    assert result["status_provenance"].startswith("parent-supplied")
    assert result["goal_complete_called"] is False
    precise = {**synthetic, "observed_utc": "2026-10-11T00:00:00.123456789Z"}
    truncated_old_behavior = __import__("datetime").datetime.fromisoformat(
        precise["observed_utc"].replace("Z", "+00:00")).isoformat()
    assert truncated_old_behavior == "2026-10-11T00:00:00.123456+00:00"
    accepted_precision = run(precise)
    assert accepted_precision.returncode == 0
    assert json.loads(accepted_precision.stdout)["goal_snapshot"]["observed_utc"] == precise["observed_utc"]
    for digits, zone in (("1234567", "Z"), ("12345678901234", "+00:00"),
                         ("1234567890123456789", "Z")):
        exact_fraction = {**synthetic, "observed_utc": f"2026-10-11T00:00:00.{digits}{zone}"}
        accepted_fraction = run(exact_fraction)
        assert accepted_fraction.returncode == 0, accepted_fraction.stderr
        assert json.loads(accepted_fraction.stdout)["goal_snapshot"]["observed_utc"] == exact_fraction["observed_utc"]
    too_long_fraction = {**synthetic, "observed_utc": "2026-10-11T00:00:00.12345678901234567890Z"}
    rejected_length = run(too_long_fraction)
    assert rejected_length.returncode == 2 and not rejected_length.stdout
    bad_calendar = {**synthetic, "observed_utc": "2023-02-29T00:00:00.1234567Z"}
    invalid_date = run(bad_calendar)
    assert invalid_date.returncode == 2 and not invalid_date.stdout
    leap_second = {**synthetic, "observed_utc": "2026-10-11T00:00:60.1234567Z"}
    invalid_second = run(leap_second)
    assert invalid_second.returncode == 2 and not invalid_second.stdout
    exact_microseconds = {**synthetic, "observed_utc": "2026-10-11T00:00:00.123456Z"}
    exact = run(exact_microseconds)
    assert exact.returncode == 0
    assert json.loads(exact.stdout)["goal_snapshot"]["observed_utc"] == exact_microseconds["observed_utc"]
    utc_z = {**synthetic, "observed_utc": "2026-10-11T00:00:00.123456Z"}
    utc_offset = {**synthetic, "observed_utc": "2026-10-11T00:00:00.123456+00:00"}
    for positive in (utc_z, utc_offset):
        accepted_utc = run(positive)
        assert accepted_utc.returncode == 0, accepted_utc.stderr
        assert json.loads(accepted_utc.stdout)["goal_snapshot"]["observed_utc"] == positive["observed_utc"]
    # RFC3339 §5.6 NOTE: lowercase t/z are equivalent to uppercase T/Z.
    lower_tz_cases = (
        "2026-10-11t00:00:00z",
        "2026-10-11T00:00:00z",
    )
    for timestamp in lower_tz_cases:
        lowercase = {**synthetic, "observed_utc": timestamp}
        accepted_lowercase = run(lowercase)
        assert accepted_lowercase.returncode == 0, accepted_lowercase.stderr
        assert json.loads(accepted_lowercase.stdout)["goal_snapshot"]["observed_utc"] == timestamp
    unknown_offset = {**synthetic, "observed_utc": "2026-10-11T00:00:00.123456-00:00"}
    rejected_unknown = run(unknown_offset)
    assert rejected_unknown.returncode == 2 and not rejected_unknown.stdout
    null = run({"observed_utc": "2026-10-11T00:00:00Z", "goal": None})
    assert null.returncode == 0 and json.loads(null.stdout)["goal_snapshot"]["goal_present"] is False
    negative = subprocess.run(["git", "diff", "--no-index", "--check", "/dev/null", "/dev/stdin"],
                              input="negative-control trailing-space \n", text=True,
                              capture_output=True, check=False)
    assert negative.returncode != 0 and "trailing whitespace" in negative.stdout + negative.stderr
    poison = "DO-NOT-STORE-OBJECTIVE-SECRET"
    rejected = run({**synthetic, "objective": poison})
    assert rejected.returncode == 2 and not rejected.stdout
    assert poison not in rejected.stderr
    malformed = run({"observed_utc": "2026-10-11T00:00:00+01:00", "goal": None})
    assert malformed.returncode == 2 and not malformed.stdout
    # These are accepted by datetime.fromisoformat, but not the RFC3339
    # separator/offset grammar required by the projection contract.
    for nonconforming in ("2026-10-11 00:00:00Z", "2026-10-11T00:00:00+0000",
                          "2026-10-11T00:00:00+00"):
        assert __import__("datetime").datetime.fromisoformat(
            nonconforming.replace("Z", "+00:00"))
        rejected_syntax = run({**synthetic, "observed_utc": nonconforming})
        assert rejected_syntax.returncode == 2 and not rejected_syntax.stdout, nonconforming
    print("synthetic parent projection: positive and null parsed; strict RFC3339 UTC syntax rejects space/+0000/+00; real read-only Git gate exit 0;"
          " stdin whitespace negative control failed as expected;"
          " objective/secret injection and non-UTC timestamp rejected without receipt")


if __name__ == "__main__":
    main()
