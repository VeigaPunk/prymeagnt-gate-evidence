#!/usr/bin/env python3
"""Read-only synthetic autonomous branch comparison; never invokes a gate."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = HERE.parent / "knowledge/gate-decision-table.md"
CASES = HERE / "autonomous-cases.json"


def main():
    rows = re.findall(r"^\| (A[01]) \|([^\n]+)$", TABLE.read_text(), re.M)
    assert [name for name, _ in rows] == ["A0", "A1"]
    policy = {}
    for name, line in rows:
        columns = [column.strip() for column in line.split("|") if column.strip()]
        assert len(columns) == 8
        gate, baseline, candidate, criteria, goal, permitted, stop, conclusion = columns
        assert permitted == "false" and stop == "unclassified"
        assert (name, gate, baseline, candidate, criteria, goal) in (
            ("A0", "failed_retries_exhausted", "pass", "failed", "unverified", "not-assessed"),
            ("A1", "passed_goal_unmet", "pass", "pass", "unmet", "incomplete"),
        )
        assert "goal.complete()" in conclusion or "goal-complete" in conclusion
        policy[gate] = (name, baseline, candidate, criteria, goal, permitted == "true", stop)
    actual = []
    for fixture in json.loads(CASES.read_text()):
        name, baseline, candidate, criteria, goal, permitted, stop = policy[fixture["autonomous_gate"]]
        assert (fixture["baseline"], fixture["candidate"], fixture["criteria"]) == (baseline, candidate, criteria)
        observed = {"id": fixture["id"], "case": name, "candidate_gates_passed": candidate == "pass",
                    "mission_goal": goal, "goal_complete_permitted": permitted, "loop_stop": stop}
        actual.append(observed)
        if observed != fixture["expected"]:
            print(json.dumps({"expected": fixture["expected"], "actual": observed}), file=sys.stderr)
            return 1
    print(json.dumps(actual, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
