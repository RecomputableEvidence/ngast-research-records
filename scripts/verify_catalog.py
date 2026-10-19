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
if cat.get('catalog_status')!='one-documentary-release-published-primary-evidence-restricted': errors.append('wrong catalog status')
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
    if m['fork_core_admitted'] or m['primary_evidence_released']: errors.append('wrong original-release claims '+ident)
    if ident=='NGAST-EVIDENCE-STANDING-DIAGNOSTIC-001':
        d=m.get('documentary_release',{})
        if m['doi']!='10.5281/zenodo.23480962': errors.append('incorrect report DOI')
        if m['publication_status']!='published_documentation_only_primary_evidence_restricted': errors.append('wrong diagnostic publication status')
        if d.get('version')!='0.3-doc-only' or d.get('version_specific_doi')!=m['doi'] or d.get('all_versions_doi')!='10.5281/zenodo.23480961': errors.append('wrong release DOI/version relation')
        if d.get('file_bytes')!=12950 or d.get('local_candidate_sha256')!='872c39906289bf6dd1d7bd5ada2cf48c56e643680fed83cc8bc923bda7c59020': errors.append('wrong local release candidate digest')
        if d.get('license')!='CC-BY-4.0' or d.get('post_publication_download_and_hash_comparison')!='not_completed': errors.append('rights or verification boundary overclaimed')
        o=m.get('orcid_work',{})
        if m['orcid_work_confirmed'] is not True or d.get('orcid_work_confirmed') is not True: errors.append('diagnostic ORCID Work observation missing')
        if o.get('orcid_id')!='0009-0000-7863-5792' or o.get('doi_shown')!=m['doi'] or o.get('public_profile_access_observed_in_owner_screenshot') is not True: errors.append('diagnostic ORCID identity/DOI discrepancy')
        if o.get('independent_orcid_api_fetch')!='not_completed' or o.get('identifier_relationship_self')!='not_explicitly_shown_in_screenshot': errors.append('overstated ORCID API/identifier verification')
        if m['archived_study_packet']['published'] or d.get('original_source_archive_published') is not False: errors.append('raw archive improperly marked published')
    else:
        if m['doi'] is not None or m['publication_status']!='public_metadata_staging_only': errors.append('premature DOI/release claim '+ident)
        if m['orcid_work_confirmed'] is not False: errors.append('premature ORCID Work claim '+ident)
        if m['license']!='not selected' or m['rights_review']!='pending': errors.append('premature rights claim '+ident)
    for k in ('title','study_status','publication_status','doi','orcid_work_confirmed','fork_core_admitted'):
        if row[k]!=m[k]: errors.append('catalog mismatch '+ident+' '+k)
if cat.get('catalog_version')!='0.3.0' or 'public-orcid-work-observed' not in cat.get('external_release_status',''): errors.append('wrong catalog/ORCID version')
if errors:
    for e in errors: print('FAIL:',e)
    sys.exit(1)
if errors:
    for e in errors: print('FAIL:',e)
    sys.exit(1)
print('PASS: '+str(len(paths))+' public file hashes; 4 catalog objects and event-chain metadata; one documentary DOI and one bounded ORCID Work observation; no Fork admission claims')
print('SCOPE: one documentary release + metadata; original raw-event chains are NOT distributed or verified by this script')
