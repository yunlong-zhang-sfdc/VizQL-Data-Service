#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

rm -rf venv
python -m venv venv
source venv/bin/activate

ls dist -al

python -m pip install dist/vizqldataservicepythonsdk*.whl
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
