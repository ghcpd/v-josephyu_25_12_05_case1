# Windows PowerShell Test Runner Script
# Usage: .\run_tests.ps1

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Flask Login App - Test Runner" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Activate virtual environment if not already active
if (-not $env:VIRTUAL_ENV) {
    Write-Host "Activating virtual environment..." -ForegroundColor Yellow
    & ".\\.venv\\Scripts\\Activate.ps1"
}

# Run pytest
Write-Host "Running test suite..." -ForegroundColor Yellow
Write-Host ""

python -m pytest test_full_app.py -v --tb=short

$testResult = $LASTEXITCODE

Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan

if ($testResult -eq 0) {
    Write-Host "✓ ALL TESTS PASSED" -ForegroundColor Green
    exit 0
} else {
    Write-Host "✗ SOME TESTS FAILED" -ForegroundColor Red
    exit 1
}
