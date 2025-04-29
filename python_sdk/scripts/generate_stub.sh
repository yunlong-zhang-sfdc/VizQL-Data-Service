#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Generate client code
openapi-generator-cli generate \
    -i ../VizQLDataServiceOpenAPISchema.json \
    -g python-pydantic-v1 \
    --additional-properties=generateSourceCodeOnly=true,packageName=openapi_client,projectName=openapi_client

echo "OpenAPI client generation completed successfully"