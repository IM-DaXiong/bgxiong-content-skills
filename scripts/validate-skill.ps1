# ASCII-ONLY on purpose: Windows PowerShell 5.1 GBK parse hazard.
$ErrorActionPreference = "Stop"
$py = Join-Path $PSScriptRoot "validate_skill.py"
python $py @args
exit $LASTEXITCODE
