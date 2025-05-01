"""
Synchronous HTTP client for querying VizQL Data Service API.

This module provides a synchronous HTTP client implementation for interacting with
the VizQL Data Service API. It uses the openapi_client library for making HTTP requests
and handling responses.

Key Features:
- query_datasource: Synchronously query data sources
- read_metadata: Synchronously read metadata

Example Usage:
    client = SyncHTTPClient()
    response = client.query_datasource(url, headers, request)
"""

from typing import Any, Dict, Optional

import openapi_client
from openapi_client.models import QueryRequest, ReadMetadataRequest
from src.api.BaseVizqlDataServiceHTTPClient import BaseVizqlDataServiceHTTPClient


class SyncHTTPClient(BaseVizqlDataServiceHTTPClient):

    def query_datasource(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        request: Optional[QueryRequest] = None,
    ) -> Any:
        configuration = openapi_client.Configuration(host=url)
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = openapi_client.DefaultApi(api_client)
        try:
            api_response = api_instance.query_datasource(
                query_request=request, _headers=headers
            )
        except openapi_client.ApiException as e:
            print("Exception when calling SyncHTTPClient-> query_datasource: %s\n" % e)
        return api_response

    def read_metadata(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        request: Optional[ReadMetadataRequest] = None,
    ) -> Any:
        configuration = openapi_client.Configuration(host=url)
        api_response = None
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = openapi_client.DefaultApi(api_client)
        try:
            api_response = api_instance.read_metadata(
                read_metadata_request=request, _headers=headers
            )
        except openapi_client.ApiException as e:
            print("Exception when calling SyncHTTPClient-> read_metadata: %s\n" % e)
        return api_response
