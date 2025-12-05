#!/usr/bin/env bash
# Setup script for UNIX-like shells. Creates a .venv and installs requirements.
set -euo pipefail
PYTHON=${PYTHON:-python3}
echo "Creating virtual environment .venv..."
$PYTHON -m venv .venv
echo "Activating and installing dependencies..."
source .venv/bin/activate
pip install -r requirements.txt
echo "Setup complete. Activate with: source .venv/bin/activate"
