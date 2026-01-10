#!/bin/bash
# Bash Test Runner Script
# Usage: bash run_tests.sh

echo "==============================================="
echo "Flask Login App - Test Runner"
echo "==============================================="
echo ""

# Activate virtual environment if not already active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
fi

# Run pytest
echo "Running test suite..."
echo ""

python -m pytest test_full_app.py -v --tb=short

TEST_RESULT=$?

echo ""
echo "==============================================="

if [ $TEST_RESULT -eq 0 ]; then
    echo "✓ ALL TESTS PASSED"
    exit 0
else
    echo "✗ SOME TESTS FAILED"
    exit 1
fi
