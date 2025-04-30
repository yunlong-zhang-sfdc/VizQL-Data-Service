"""
VizQL Data Service Client Module

This module provides a client for interacting with the VizQL Data Service API.
It handles authentication and provides methods for querying datasources and reading metadata.
"""

from typing import Union

import tableauserverclient as TSC

from openapi_client.models.query_request import QueryRequest
from openapi_client.models.read_metadata_request import ReadMetadataRequest
from src.api.EndPoints import EndPoints
from src.api.HTTPHeaders import default_headers
from src.api.SyncHTTPClient import SyncHTTPClient
from src.models.server import Server
from src.models.user import User


class Client:
    def __init__(self, user: User, server: Server):
        """
        Initialize the VizQL Data Service client.

        Args:
            user: User credentials for authentication
            server: Server configuration
        """
        self.user = user
        self.server = server

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
        tableau_auth = self._build_auth()
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
                return response.data
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
        tableau_auth = self._build_auth()
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
                return response.data
        else:
            raise NotImplementedError("Async client not implemented yet")

    def _build_auth(self) -> Union[TSC.PersonalAccessTokenAuth, TSC.TableauAuth]:
        """Private method to create Tableau authentication based on user credentials."""
        if self.user.personal_access_token:
            return TSC.PersonalAccessTokenAuth(
                token_name=self.user.username,  # Used as token_name for PAT
                personal_access_token=self.user.personal_access_token,
                site_id=self.server.site,
            )
        elif self.user.password:
            return TSC.TableauAuth(
                username=self.user.username,
                password=self.user.password,
                site_id=self.server.site,
            )
        else:
            raise ValueError(
                "User must provide either a password or a personal access token."
            )
