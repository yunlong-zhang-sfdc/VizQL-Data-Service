#!/bin/bash

# Exit on error
set -e

# Print commands as they are executed
set -x

# Generate client code
openapi-python-client generate --path ../VizQLDataServiceOpenAPISchema.json --config ./openapi-client.yml --overwrite

rm -rf openapi_client
mv temp_project/openapi_client ./openapi_client
rm -r temp_project

echo "OpenAPI client generation completed successfully"