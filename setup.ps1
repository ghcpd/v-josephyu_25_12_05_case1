# PowerShell setup script
param([switch]$Recreate)

if ($Recreate -and (Test-Path .venv)) {
    Remove-Item -Recurse -Force .venv
}

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Write-Host "Virtual environment created and dependencies installed. Use '.\\.venv\\Scripts\\Activate.ps1' to activate."