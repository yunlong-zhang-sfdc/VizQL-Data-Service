#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

rm -rf venv
python -m venv venv
source venv/bin/activate

python -m pip install dist/vizql_data_service*.whl
pwd

python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -r test-requirements.txt

echo "Running linting checks..."
# flake8 src tests
# black --check src tests
# isort --check-only src tests
# mypy src

echo "Running tests with coverage..."
pytest tests --disable-warnings --cov

if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Tests failed!"
    exit 1
fi
