#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Install dependencies
pip install --upgrade pip
pip install setuptools wheel build
pip install requests

# Build the package
cd python_sdk
python setup.py sdist bdist_wheel

echo "Build completed successfully. Packages are in python_sdk/dist/"