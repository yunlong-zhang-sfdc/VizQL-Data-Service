#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Install dependencies
python -m pip install --upgrade pip
python -m pip install --upgrade build

# Build the package
python -m build

echo "Check Tar content"
tar -tzf dist/vizqldataservicepythonsdk-1.0.10.tar.gz

echo "Check client folder"
ls openapi_client -alR
echo "Build completed successfully. Packages are in python_sdk/dist/"