#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Install dependencies
python -m pip install --upgrade pip
python -m pip install --upgrade build

# Clean build the package
rm -rf build dist *.egg-info src/*.egg-info
python -m build

echo "Show vizqldataservicepythonsdk tar file content"
tar -tzf dist/vizqldataservicepythonsdk-*.tar.gz

echo "Build completed successfully. Packages are in python_sdk/dist/"