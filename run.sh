#!/bin/bash
# Move into the exact script directory
cd "$(dirname "$0")"

# Export your API key
export GEMINI_API_KEY="TYPE_UR_API"

# Run main.py using the virtual environment's python interpreter
./venv/bin/python3 main.py

