# Windows PowerShell Setup Script for Flask Login App
# Usage: .\setup.ps1

Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Flask Login App - Windows Setup" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.10+" -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host ""
Write-Host "Creating virtual environment (.venv)..." -ForegroundColor Yellow
if (Test-Path ".\.venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv .venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host ""
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& ".\\.venv\\Scripts\\Activate.ps1"
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host ""
Write-Host "Installing dependencies from requirements.txt..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

# Initialize database
Write-Host ""
Write-Host "Initializing database..." -ForegroundColor Yellow
python -c "from app import app; from models import init_db; init_db(app); print('Database initialized')"
Write-Host "✓ Database initialized (app.db)" -ForegroundColor Green

# Run tests
Write-Host ""
Write-Host "Running tests..." -ForegroundColor Yellow
python -m pytest test_full_app.py -v --tb=short
$testResult = $LASTEXITCODE

if ($testResult -eq 0) {
    Write-Host "✓ All tests passed!" -ForegroundColor Green
} else {
    Write-Host "⚠ Some tests failed (see above)" -ForegroundColor Yellow
}

# Display next steps
Write-Host ""
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host "Setup Complete!" -ForegroundColor Cyan
Write-Host "===============================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor White
Write-Host "1. Activate environment (each new terminal):" -ForegroundColor White
Write-Host "   .\\.venv\\Scripts\\Activate.ps1" -ForegroundColor Cyan
Write-Host ""
Write-Host "2. Start the app:" -ForegroundColor White
Write-Host "   python app.py" -ForegroundColor Cyan
Write-Host ""
Write-Host "3. Open in browser:" -ForegroundColor White
Write-Host "   http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host ""
Write-Host "4. Run tests anytime:" -ForegroundColor White
Write-Host "   .\run_tests.ps1" -ForegroundColor Cyan
Write-Host ""
Write-Host "For more information, see: corrected_readme.md" -ForegroundColor White
Write-Host ""
