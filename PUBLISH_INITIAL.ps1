# Powershell: run after creating an EMPTY GitHub repository at the destination below.
# No publication occurs unless the operator types PUBLISH and GitHub push succeeds.
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot
$remote = 'https://github.com/RecomputableEvidence/ngast-research-records.git'
Write-Host 'PUBLIC-METADATA-ONLY STAGING — raw transcripts and runners are not included.'
python .\scripts\verify_catalog.py
if ($LASTEXITCODE -ne 0) { throw 'Verification failed. No publishing attempted.' }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw 'Git is required.' }
if (-not (Test-Path .git)) { git init -b main }
if ($LASTEXITCODE -ne 0) { throw 'git init failed.' }
git add -A
Write-Host 'Review the exact staged file list before publication:'
git diff --cached --name-only
Write-Host ''
$answer = Read-Host 'Type PUBLISH to commit and push these metadata files to the public repository'
if ($answer -cne 'PUBLISH') { Write-Host 'Not published.'; exit 0 }
git commit -m 'Initialize NGAST independent research metadata catalog'
if ($LASTEXITCODE -ne 0) { throw 'Commit failed; configure your real Git author identity and rerun.' }
if (-not (git remote)) { git remote add origin $remote }
if ($LASTEXITCODE -ne 0) { throw 'Remote setup failed.' }
git push -u origin main
if ($LASTEXITCODE -ne 0) { throw 'Push failed. Local commit is preserved; no confirmed public release.' }
Write-Host 'Git push succeeded; examine public repository contents and status manually.'
