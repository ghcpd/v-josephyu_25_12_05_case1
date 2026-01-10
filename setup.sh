#!/bin/bash
# Bash Setup Script for Flask Login App
# Usage: bash setup.sh

echo "==============================================="
echo "Flask Login App - Linux/macOS Setup"
echo "==============================================="
echo ""

# Check if Python is installed
echo "Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo "✗ Python3 not found. Please install Python 3.10+"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
echo "✓ Python found: $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "Creating virtual environment (.venv)..."
if [ -d ".venv" ]; then
    echo "✓ Virtual environment already exists"
else
    python3 -m venv .venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source .venv/bin/activate
echo "✓ Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip
echo "✓ pip upgraded"

# Install dependencies
echo ""
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt
echo "✓ Dependencies installed"

# Initialize database
echo ""
echo "Initializing database..."
python -c "from app import app; from models import init_db; init_db(app); print('Database initialized')"
echo "✓ Database initialized (app.db)"

# Run tests
echo ""
echo "Running tests..."
python -m pytest test_full_app.py -v --tb=short
TEST_RESULT=$?

if [ $TEST_RESULT -eq 0 ]; then
    echo "✓ All tests passed!"
else
    echo "⚠ Some tests failed (see above)"
fi

# Display next steps
echo ""
echo "==============================================="
echo "Setup Complete!"
echo "==============================================="
echo ""
echo "Next steps:"
echo "1. Activate environment (each new terminal):"
echo "   source .venv/bin/activate"
echo ""
echo "2. Start the app:"
echo "   python app.py"
echo ""
echo "3. Open in browser:"
echo "   http://127.0.0.1:5000"
echo ""
echo "4. Run tests anytime:"
echo "   bash run_tests.sh"
echo ""
echo "For more information, see: corrected_readme.md"
echo ""
