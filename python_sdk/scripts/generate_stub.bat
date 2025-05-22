@echo off
setlocal enabledelayedexpansion

REM Exit on error
set "EXIT_ON_ERROR=1"

REM Print commands as they are executed
echo on

REM Install required packages
pip install datamodel-code-generator

REM Generate client code
datamodel-codegen --input ../VizQLDataServiceOpenAPISchema.json --output-model-type pydantic_v2.BaseModel --input-file-type openapi --output src/api/openapi_generated-raw.py --use-annotated --allow-population-by-field-name

echo Starting post-processing...
python scripts/post_process.py

echo OpenAPI client generation completed successfully 