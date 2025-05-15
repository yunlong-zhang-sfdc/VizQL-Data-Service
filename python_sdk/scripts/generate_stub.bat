@echo off
setlocal enabledelayedexpansion

REM Exit on error
set "EXIT_ON_ERROR=1"

REM Print commands as they are executed
echo on

REM Install required packages
pip install openapi-python-client pydoc-markdown

REM Convert schema
python scripts/convert_schema.py

REM Generate client code
openapi-python-client generate --path build/temp_schema.json --config ./openapi-client.yml --overwrite --meta poetry

REM Clean up and move files
if exist openapi_client rmdir /s /q openapi_client
move temp_project\openapi_client .\openapi_client
rmdir /s /q temp_project

REM Skip if running in GitHub Actions
if "%GITHUB_ACTIONS%"=="true" (
    echo Skipping documentation generation in GitHub Actions
    exit /b 0
)

REM Generate documentation
python scripts/add_enum_docstrings.py
pydoc-markdown

echo OpenAPI client generation completed successfully 