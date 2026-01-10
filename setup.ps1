<#
PowerShell setup script to create a virtual environment and install dependencies.
Usage: Run this script from the project root in PowerShell (Windows):
  .\setup.ps1
#>
Set-StrictMode -Version Latest
Write-Host "Creating virtual environment .venv..."
python -m venv .venv
Write-Host "Activating virtual environment and installing dependencies..."
.\.venv\Scripts\Activate.ps1; pip install -r requirements.txt
Write-Host "Setup complete. To activate the venv later: .\.venv\Scripts\Activate.ps1"
