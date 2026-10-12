# Gate-evidence — round 8

## Independent-input check; no axis advance

**Falsifiable claim tested:** The R7 comparator records a parent-supplied goal projection independently of its pinned local Git result; changing a syntactically valid projection with gate pins fixed changes the recorded snapshot but not the gate result, and changing the candidate pin with the snapshot fixed does not rewrite that snapshot.

**Evidence:** On baseline `2bef16987347693f8d896e2df9cb13a3cec7499c`, `compare_parent_receipt.py` and its contract checker already existed. Ran `python3 .shokunin/gate-evidence/corpus/live/check_parent_receipt_contract.py`; exit 0. Additional read-only calls to the comparator held pins `52d573bdf502cb1416d65c0756106db9d5b3bde2` and `bc1bb3c572981158f8ac0b4994d3333741650886` fixed while varying valid snapshot from active (8 tokens) to paused (999 tokens) and null; each exited 0, emitted the corresponding normalized snapshot, and retained Git gate exit 0. With the active snapshot fixed, changing candidate pin to `c8217280cc056303a8ca0984ff28a91067bd2284` still emitted an equal `goal_snapshot`; both Git checks exited 0. Output receipts differed in their pinned inputs/timing, as expected.

**Interpretation and verdict:** This confirms co-recording of independent supplied inputs for these local benign Git pairs, not authentication or truth of the snapshot, nor causal relation. The comparator already states parent-supplied provenance and “same recording, independent inputs; no causal inference.” No misleading claim or defect was found; therefore **calibration unchanged** and **coverage unchanged**. No axis advance. No goal completion, autonomous acceptance, or stop is assessed or claimed. No files in the corpus needed changes.

**Limits:** This did not execute or validate the host autonomous gate, acceptance criteria, mission-goal state, or loop-stop. It does not strengthen provenance. SHONEN remains probationary; no promotion.
