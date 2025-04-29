"""
This is an asynchronous http client that can be used to query VizQL Data Service API.
httpx module is used for these requests
"""

from typing import Optional, Dict, Any
import json as json_lib
import httpx
from openapi_client import MetadataOutput, QueryOutput
from src.api.BaseVizqlDataServiceHTTPClient import BaseVizqlDataServiceHTTPClient


class AsyncHTTPClient(BaseVizqlDataServiceHTTPClient):

    async def query_datasource(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, json=json)
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
        json: Optional[Dict[str, Any]] = None,
    ) -> MetadataOutput:
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, json=json)
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
