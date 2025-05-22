#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

rm -rf venv
python -m venv venv

# Detect OS and activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

ls dist -al

python -m pip install dist/vizql_data_service_py*.whl
python -m pip install --upgrade pip
pip install -e .[dev]

echo "Running linting checks..."
black . --check
isort .
flake8 .
mypy .

echo "Running tests with coverage..."
pytest tests --disable-warnings --cov

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Tests failed!"
    exit 1
fi
