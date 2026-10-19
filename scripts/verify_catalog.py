#!/usr/bin/env python3
"""Verify only the public metadata staging surface, not withheld experimental data."""
from pathlib import Path
import hashlib, json, re, sys
ROOT = Path(__file__).resolve().parents[1]
checksums = ROOT / 'CHECKSUMS.sha256'
errors=[]
listed={}
for line in checksums.read_text().splitlines():
    if not line.strip(): continue
    if '  ' not in line: errors.append('bad checksum line'); continue
    sha, rel = line.split('  ', 1)
    if rel in listed or not re.fullmatch(r'[0-9a-f]{64}', sha): errors.append('duplicate/bad digest '+rel)
    listed[rel]=sha
paths={str(p.relative_to(ROOT).as_posix()) for p in ROOT.rglob('*') if p.is_file() and '.git' not in p.parts and p.name!='CHECKSUMS.sha256'}
if set(listed)!=paths: errors.append('checksum path set differs: missing='+str(sorted(paths-set(listed)))+' extra='+str(sorted(set(listed)-paths)))
for rel,sha in listed.items():
    p=ROOT/rel
    if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=sha: errors.append('digest mismatch '+rel)
cat=json.loads((ROOT/'research/catalog.json').read_text())
if cat.get('catalog_status')!='initial-public-metadata-only': errors.append('wrong catalog status')
ids=[x['object_id'] for x in cat['research_objects']]
if len(ids)!=4 or len(set(ids))!=4: errors.append('expected 4 distinct records')
expected_counts={'NGAST-OPEN-CHOICE-HISTORICAL-001': [100], 'NGAST-PAIR-OBS-001':[36,92,152], 'NGAST-EVIDENCE-COORDINATION-PILOT-001':[203], 'NGAST-EVIDENCE-STANDING-DIAGNOSTIC-001':[7,283]}
for row in cat['research_objects']:
    ident=row['object_id']; mp=ROOT/'research/objects'/ident/'metadata.json'
    if not mp.is_file(): errors.append('missing metadata '+ident); continue
    m=json.loads(mp.read_text()); counts=sorted(v['events'] for v in m['primary_event_chains'].values())
    if counts!=sorted(expected_counts[ident]): errors.append('event counts '+ident)
    for ent in m['primary_event_chains'].values():
        if not re.fullmatch(r'[0-9a-f]{64}', ent['chain_tip_sha256']): errors.append('bad chain tip '+ident)
    arc=m['archived_study_packet']
    if not re.fullmatch(r'[0-9a-f]{64}', arc['sha256']) or arc['published'] is not False: errors.append('bad private archive status '+ident)
    if any([m['doi'] is not None,m['orcid_work_confirmed'],m['fork_core_admitted'],m['primary_evidence_released']]): errors.append('wrong release claims '+ident)
    if m['license']!='not selected' or m['rights_review']!='pending': errors.append('premature rights claim '+ident)
    for k in ('title','study_status','publication_status','doi','orcid_work_confirmed','fork_core_admitted'):
        if row[k]!=m[k]: errors.append('catalog mismatch '+ident+' '+k)
if errors:
    for e in errors: print('FAIL:',e)
    sys.exit(1)
print('PASS: '+str(len(paths))+' public file hashes; 4 catalog objects and event-chain metadata; 0 issued DOI/ORCID/Fork claims')
print('SCOPE: metadata only; original raw-event chains are NOT distributed or verified by this script')
