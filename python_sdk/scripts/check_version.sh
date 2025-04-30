#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Get pyproject.toml major and minor version
pyproject_version=$(cat pyproject.toml | grep -oP 'version = "\K[0-9]+\.[0-9]+')

# Get VizQLDataServiceOpenAPISchema.json major and minor version
schema_version=$(cat ../VizQLDataServiceOpenAPISchema.json | grep -oP '"version": "\K[0-9]+\.[0-9]+')

# Check if pyproject.toml version matches VizQLDataServiceOpenAPISchema.json version
if [ "$pyproject_version" != "$schema_version" ]; then
    echo "Error: pyproject.toml version ($pyproject_version) does not match VizQLDataServiceOpenAPISchema.json version ($schema_version)"
    exit 1
else
    echo "Success: pyproject.toml version ($pyproject_version) matches VizQLDataServiceOpenAPISchema.json version ($schema_version)"
fi