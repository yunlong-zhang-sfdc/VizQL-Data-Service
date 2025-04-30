#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Install dependencies
python -m pip install --upgrade pip
python -m pip install --upgrade build

# Build the package
python build

echo "Build completed successfully. Packages are in python_sdk/dist/"