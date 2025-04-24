"""
VizDataService Client Module

This module provides a client for interacting with the VizDataService API.
It handles authentication and provides methods for querying datasources and reading metadata.
"""

from typing import Optional, Union
import tableauserverclient as TSC

from openapi_client import ReadMetadataRequest
from openapi_client.models.query_request import QueryRequest
from vizdataserviceclient.models.user import User
from vizdataserviceclient.models.server import Server

from vizdataserviceclient.api.EndPoints import EndPoints
from vizdataserviceclient.api.HTTPHeaders import default_headers
from vizdataserviceclient.api.SyncHTTPClient import SyncHTTPClient

class Client:
    """
    A client for interacting with the VizDataService API.
    
    This client handles authentication via Tableau Server and provides methods
    for querying datasources and reading metadata.
    
    Example:
        ```python
        from vizdataserviceclient.models.user import User
        from vizdataserviceclient.models.server import Server
        from vizdataserviceclient.client import Client
        
        user = User('test', 'password', personal_access_token='')
        server = Server('http://localhost', '')
        client = Client(user, server)
        
        # Query a datasource
        response = client.query_datasource(query_request)
        ```
    """
    
    def __init__(self, user: User, server: Server):
        """
        Initialize the VizDataService client.
        
        Args:
            user: User credentials for authentication
            server: Server configuration
        """
        self.user = user
        self.server = server

    """
    This is a utility method that can be used for VizDataService APIs.
    User login happens via the tableau server-client-python library
    Tableau auth is obtained and used to query the Vizdataservice apis
    
    Here is an example usage :
    from openapi_client.models.query_request import QueryRequest
    from vizdataserviceclient.models.user import User
    from vizdataserviceclient.models.server import Server
    from vizdataserviceclient.utils import file_util
    from vizdataserviceclient.client import Client

    user=User('test','password',personal_access_token='')
    server=Server('http://localhost','')
    query_request_json = file_util.read_json('examples/payloads','query_request.json')
    query_request = QueryRequest.from_json(query_request_json)
    client=Client(user,server)
    client.query_datasource(query_request)
    """

    def __str__(self) -> str:
        """Return a string representation of the client."""
        return f"{self.user} - {self.server.server_name}"

    def query_datasource(
        self,
        query_request: QueryRequest,
        sync_client: bool = True
    ) -> str:
        """
        Query a datasource using the VizDataService API.
        
        Args:
            query_request: The query request to execute
            sync_client: Whether to use synchronous client (default: True)
            
        Returns:
            str: JSON response from the API
            
        Raises:
            Exception: If authentication or query fails
        """
        tableau_auth = TSC.TableauAuth(
            self.user.username,
            self.user.password,
            self.server.site
        )
        server = TSC.Server(self.server.server_name)
        headers = default_headers()
        
        if sync_client:
            client = SyncHTTPClient()
            with server.auth.sign_in(tableau_auth):
                headers.set_tableau_auth(server.auth_token)
                response = client.query_datasource(
                    self.server.server_name + EndPoints.VIZQL_DATA_SERVICE_URL,
                    headers.to_dict(),
                    query_request
                )
                return response.model_dump_json()
        else:
            raise NotImplementedError("Async client not implemented yet")

    def read_metadata(
        self,
        read_metadata_request: ReadMetadataRequest,
        sync_client: bool = True
    ) -> str:
        """
        Read metadata from a datasource using the VizDataService API.
        
        Args:
            read_metadata_request: The metadata request to execute
            sync_client: Whether to use synchronous client (default: True)
            
        Returns:
            str: JSON response from the API
            
        Raises:
            Exception: If authentication or metadata request fails
        """
        tableau_auth = TSC.TableauAuth(
            self.user.username,
            self.user.password,
            self.server.site
        )
        server = TSC.Server(self.server.server_name)
        headers = default_headers()
        
        if sync_client:
            client = SyncHTTPClient()
            with server.auth.sign_in(tableau_auth):
                headers.set_tableau_auth(server.auth_token)
                response = client.read_metadata(
                    self.server.server_name + EndPoints.VIZQL_DATA_SERVICE_URL,
                    headers.to_dict(),
                    read_metadata_request
                )
                return response.model_dump_json()
        else:
            raise NotImplementedError("Async client not implemented yet")


