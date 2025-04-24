"""
This is an synchronous http client that can be used to query VizDataService API.
"""

from typing import Optional, Dict, Any
import openapi_client
from vizdataserviceclient.api.BaseVizqlDataServiceHTTPClient import BaseVizqlDataServiceHTTPClient

class SyncHTTPClient(BaseVizqlDataServiceHTTPClient):
    
    def query_datasource(self, url: str, headers: Optional[Dict[str, str]] = None,
                         json: Optional[Dict[str, Any]] = None) -> Any:
        configuration=openapi_client.Configuration(
            host= url)
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = openapi_client.DefaultApi(api_client)
        try:
            api_response = api_instance.query_datasource(query_request=json,
                                                         _headers=headers)
        except openapi_client.ApiException as e:
            print("Exception when calling  SyncHTTPClient-> query_datasource: %s\n" % e)
        return api_response

    def read_metadata(self, url: str, headers: Optional[Dict[str, str]] = None,
                      json: Optional[Dict[str, Any]] = None) -> Any:
        configuration=openapi_client.Configuration(
            host= url)
        api_response=None
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = openapi_client.DefaultApi(api_client)
        try:
            api_response = api_instance.read_metadata(read_metadata_request=json,
                                                         _headers=headers)
        except openapi_client.ApiException as e:
            print("Exception when calling  SyncHTTPClient-> read_metadata: %s\n" % e)
        return api_response

