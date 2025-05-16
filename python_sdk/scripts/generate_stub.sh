#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

pip install datamodel-code-generator

# Generate client code
datamodel-codegen --input ../VizQLDataServiceOpenAPISchema.json --output-model-type pydantic_v2.BaseModel --input-file-type openapi --output src/api/openapi_api-raw.py --use-annotated --allow-population-by-field-name

echo "Starting post-processing..."
python scripts/post_process.py

echo "OpenAPI client generation completed successfully"