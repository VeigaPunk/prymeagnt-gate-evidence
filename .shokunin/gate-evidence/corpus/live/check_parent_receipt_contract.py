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
    rejected_precision = run(precise)
    assert rejected_precision.returncode == 2 and not rejected_precision.stdout
    assert "DO-NOT-STORE" not in rejected_precision.stderr
    exact_microseconds = {**synthetic, "observed_utc": "2026-10-11T00:00:00.123456Z"}
    exact = run(exact_microseconds)
    assert exact.returncode == 0
    assert json.loads(exact.stdout)["goal_snapshot"]["observed_utc"] == exact_microseconds["observed_utc"]
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
    print("synthetic parent projection: positive and null parsed; real read-only Git gate exit 0;"
          " stdin whitespace negative control failed as expected;"
          " objective/secret injection and non-UTC timestamp rejected without receipt")


if __name__ == "__main__":
    main()
