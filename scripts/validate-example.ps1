# Minimal PowerShell wrapper
param([Parameter(Mandatory=$true)][string[]]$PackDir)
$script = Join-Path $PSScriptRoot 'validate-example.py'
python $script @PackDir
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
