"""
Asynchronous HTTP client for querying VizQL Data Service API.

This module provides an asynchronous HTTP client implementation using the httpx library for HTTP requests.
It inherits from BaseVizqlDataServiceHTTPClient and implements asynchronous methods for data source querying
and metadata reading.

Key Features:
- query_datasource: Asynchronously query data sources
- read_metadata: Asynchronously read metadata

Example Usage:
    client = AsyncHTTPClient()
    response = await client.query_datasource(url, headers, request)
"""

import json as json_lib
from typing import Any, Dict, Optional

import httpx

from openapi_client import (
    MetadataOutput,
    QueryOutput,
    QueryRequest,
    ReadMetadataRequest,
)
from src.api.BaseVizqlDataServiceHTTPClient import BaseVizqlDataServiceHTTPClient


class AsyncHTTPClient(BaseVizqlDataServiceHTTPClient):

    async def query_datasource(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        request: Optional[QueryRequest] = None,
    ) -> Any:
        async with httpx.AsyncClient() as client:
            try:
                json_data = request.to_dict() if request else {}
                response = await client.post(url, headers=headers, json=json_data)
                if response.status_code == 200:
                    return QueryOutput.from_json(json_lib.dumps(response.json()))
                response.raise_for_status()
                return response
            except httpx.RequestError as e:
                print(f"Request error: {e}")
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None

    async def read_metadata(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        request: Optional[ReadMetadataRequest] = None,
    ) -> Any:
        async with httpx.AsyncClient() as client:
            try:
                json_data = request.to_dict() if request else {}
                response = await client.post(url, headers=headers, json=json_data)
                if response.status_code == 200:
                    return MetadataOutput.from_json(json_lib.dumps(response.json()))
                response.raise_for_status()
                return response
            except httpx.RequestError as e:
                print(f"Request error: {e}")
                return None
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                return None
