"""
VizQL Data Service Client Module

This module provides a client for interacting with the VizQL Data Service API.
It handles authentication and provides methods for querying datasources and reading metadata.
"""

import tableauserverclient as TSC

from openapi_client.models.query_request import QueryRequest
from openapi_client.models.read_metadata_request import ReadMetadataRequest
from src.api.EndPoints import EndPoints
from src.api.HTTPHeaders import default_headers
from src.api.SyncHTTPClient import SyncHTTPClient
from src.models.server import Server
from src.models.user import User


class Client:
    """
    A client for interacting with the VizQL Data Service API.

    This client handles authentication via Tableau Server and provides methods
    for querying datasources and reading metadata.

    Example:
        ```python
        from src.models.user import User
        from src.models.server import Server
        from src.client import Client

        user = User('test', 'password', personal_access_token='')
        server = Server('http://localhost', '')
        client = Client(user, server)

        # Query a datasource
        response = client.query_datasource(query_request)
        ```
    """

    def __init__(self, user: User, server: Server):
        """
        Initialize the VizQL Data Service client.

        Args:
            user: User credentials for authentication
            server: Server configuration
        """
        self.user = user
        self.server = server

    """
    This is a utility method that can be used for VizQL Data Service APIs.
    User login happens via the tableau server-client-python library
    Tableau auth is obtained and used to query the VizQL Data Service apis

    Here is an example usage :
    from openapi_client.models.query_request import QueryRequest
    from src.models.user import User
    from src.models.server import Server
    from src.utils import file_util
    from src.client import Client

    user=User('test','password',personal_access_token='')
    server=Server('http://localhost','')
    query_request_json = file_util.read_json('examples','query_request.json')
    query_request = QueryRequest.from_json(query_request_json)
    client=Client(user,server)
    client.query_datasource(query_request)
    """

    def __str__(self) -> str:
        """Return a string representation of the client."""
        return f"{self.user} - {self.server.server_name}"

    def query_datasource(
        self, query_request: QueryRequest, sync_client: bool = True
    ) -> str:
        """
        Query a datasource using the VizQL Data Service API.

        Args:
            query_request: The query request to execute
            sync_client: Whether to use synchronous client (default: True)

        Returns:
            str: JSON response from the API

        Raises:
            Exception: If authentication or query fails
        """
        tableau_auth = TSC.TableauAuth(
            self.user.username, self.user.password, self.server.site
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
                    query_request,
                )
                return response.model_dump_json()
        else:
            raise NotImplementedError("Async client not implemented yet")

    def read_metadata(
        self, read_metadata_request: ReadMetadataRequest, sync_client: bool = True
    ) -> str:
        """
        Read metadata from a datasource using the VizQL Data Service API.

        Args:
            read_metadata_request: The metadata request to execute
            sync_client: Whether to use synchronous client (default: True)

        Returns:
            str: JSON response from the API

        Raises:
            Exception: If authentication or metadata request fails
        """
        tableau_auth = TSC.TableauAuth(
            self.user.username, self.user.password, self.server.site
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
                    read_metadata_request,
                )
                return response.model_dump_json()
        else:
            raise NotImplementedError("Async client not implemented yet")
