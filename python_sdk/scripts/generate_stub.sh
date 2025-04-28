#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

which python
which pip
pip list  # Check installed packages

# Generate client code
openapi-generator-cli generate \
    -i VizQLDataServiceOpenAPISchema.json \
    -g python-pydantic-v1 \
    -o python_sdk/build/generated \
    --ignore-file-override .openapi-generator-ignore \
    --additional-properties=generateSourceCodeOnly=true,packageName=openapi_client,projectName=openapi_client

echo "OpenAPI client generation completed successfully"