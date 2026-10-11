#!/usr/bin/env python3
"""Exercise the ordered, read-only decision table with deterministic fixtures."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = HERE.parent / "knowledge/gate-decision-table.md"
FIXTURES = HERE / "gate-cases.json"


def rows():
    table = TABLE.read_text()
    matches = re.findall(r"^\| (B0|C0|G0|G\?|G1) \|([^\n]+)$", table, re.M)
    assert [name for name, _ in matches] == ["B0", "C0", "G0", "G?", "G1"]
    return [(name, [cell.strip() for cell in line.split("|")]) for name, line in matches]


def matches(row, sample):
    baseline, candidate, criteria = row[:3]
    baseline_ok = baseline == "all observed pass" and sample["baseline"] == "pass"
    if baseline == "failed or unrun":
        baseline_ok = sample["baseline"] in ("failed", "unrun")
    if not baseline_ok:
        return False
    if candidate == "failed or unrun" and sample["candidate"] not in ("failed", "unrun"):
        return False
    if candidate == "all observed pass" and sample["candidate"] != "pass":
        return False
    if candidate not in ("any / not applicable", "failed or unrun", "all observed pass"):
        raise ValueError(f"unknown candidate predicate: {candidate}")
    if criteria == "at least one measured unmet":
        return sample["criteria"] == "unmet"
    if criteria == "string-only or unmeasurable / no evidence":
        return sample["criteria"] == "unverified"
    if criteria == "every mechanical criterion measured met":
        return sample["criteria"] == "met"
    if criteria == "any":
        return True
    raise ValueError(f"unknown criteria predicate: {criteria}")


def classify(sample, table_rows):
    for name, cells in table_rows:
        if matches(cells, sample):
            conclusion = cells[3]
            # Assertions bind the row's prose to the expected policy, not merely its label.
            goal = {"B0": "not-assessed", "C0": "not-assessed", "G0": "incomplete",
                    "G?": "unverified", "G1": "satisfied"}[name]
            if goal in ("incomplete", "unverified", "satisfied"):
                assert f"`{goal}`" in conclusion
            if name in ("G0", "G?", "G1"):
                assert "`goal.complete()`" in conclusion
            if name == "G1":
                assert "only then" in conclusion
            if name == "C0":
                assert "No ship claim" in conclusion
            return {"case": name, "mission_goal": goal,
                    "goal_complete_permitted": name == "G1", "candidate_gates_passed": name in ("G0", "G?", "G1")}
    raise AssertionError(f"no row matched {sample['id']}")


def main():
    table_rows = rows()
    fixtures = json.loads(FIXTURES.read_text())
    actual = []
    for fixture in fixtures:
        observed = classify(fixture, table_rows)
        actual.append({"id": fixture["id"], **observed})
        if actual[-1] != fixture["expected"]:
            print(json.dumps({"id": fixture["id"], "expected": fixture["expected"],
                              "actual": actual[-1]}, sort_keys=True), file=sys.stderr)
            return 1
    print(json.dumps(actual, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
