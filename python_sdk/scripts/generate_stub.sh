#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Convert schema
python scripts/convert_schema.py

# Generate client code
openapi-python-client generate --path build/temp_schema.json --config ./openapi-client.yml --overwrite

rm -rf openapi_client
mv temp_project/openapi_client ./openapi_client
rm -r temp_project

echo "OpenAPI client generation completed successfully"