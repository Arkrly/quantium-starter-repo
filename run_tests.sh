#!/bin/bash

# Activate the virtual environment and run the test suite
# Exit with the code from pytest (0 for success, non-zero for failure)

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Error: Virtual environment not found at .venv"
    exit 1
fi

# Run pytest using the virtual environment's python
.venv/bin/pytest test_app.py
exit_code=$?

# Exit with the same code as pytest
exit $exit_code