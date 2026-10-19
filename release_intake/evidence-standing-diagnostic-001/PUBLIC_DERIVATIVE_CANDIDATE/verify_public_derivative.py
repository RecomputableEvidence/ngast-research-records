#!/usr/bin/env python3
"""Verify local public derivative digests and summary invariants only."""
from pathlib import Path
import json,hashlib
root=Path(__file__).resolve().parent
lines=(root/'SHA256SUMS.txt').read_text().splitlines()
for s in lines:
 dig,name=s.split('  ',1)
 f=root/name
 assert f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest()==dig,name
stats=json.loads((root/'VERIFICATION_SUMMARY.json').read_text())
assert stats['second_stage_judgments']==42 and stats['correct_evaluated_fields']==210
assert sum(a['judgments'] for a in stats['condition_summaries'].values())==42
print('PUBLIC_DERIVATIVE_CHECKS_PASS — original logs absent; event chains NOT recomputed')
