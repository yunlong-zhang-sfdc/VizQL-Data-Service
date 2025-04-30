#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Get pyproject.toml major version
pyproject_major_version=$(cat pyproject.toml | grep -oP 'version = "\K[0-9]+')

# Get VizQLDataServiceOpenAPISchema.json major version
schema_major_version=$(cat ../VizQLDataServiceOpenAPISchema.json | grep -oP '"version": "\K[0-9]+')

# Check if pyproject.toml major version matches VizQLDataServiceOpenAPISchema.json major version
if [ "$pyproject_major_version" != "$schema_major_version" ]; then
    echo "Error: pyproject.toml major version ($pyproject_major_version) does not match VizQLDataServiceOpenAPISchema.json major version ($schema_major_version)"
    exit 1
else
    echo "Success: pyproject.toml major version ($pyproject_major_version) matches VizQLDataServiceOpenAPISchema.json major version ($schema_major_version)"
fi