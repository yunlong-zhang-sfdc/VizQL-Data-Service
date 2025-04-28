#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Install dependencies
python -m pip install --upgrade pip
pip install setuptools wheel build
pip install requests

# Build the package
python setup.py sdist bdist_wheel

echo "Build completed successfully. Packages are in python_sdk/dist/"