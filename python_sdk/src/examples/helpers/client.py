"""
Client Module

This module provides the Client class for handling API authentication and requests.
"""

from importlib.metadata import version

from src.api.client import AuthenticatedClient
from .server import Server
from .utils import format_server_url

API_SUBDOMAIN = "/api/v1/vizql-data-service"
X_TABLEAU_AUTH = "X-Tableau-Auth"
VERSION = version("vizqldataservicepythonsdk")  # Read version from package metadata


class Client:
    """Client for VizQL Data Service API."""

    def __init__(self, server: Server):
        """Initialize the client.

        Args:
            server: The server instance to use for authentication.
        """
        self.server = server
        self._client: AuthenticatedClient = self._create_client()

    def _create_client(self) -> AuthenticatedClient:
        """Create an authenticated client with proper server URL."""
        base_url = format_server_url(self.server.url, API_SUBDOMAIN)
        print(f"Server URL: {base_url}")

        return AuthenticatedClient(
            base_url=base_url,
            token=self.server.get_auth_token(),
            prefix="",
            auth_header_name=X_TABLEAU_AUTH,
            headers={"User-Agent": f"python-sdk/{VERSION}"},
        )  # type: ignore

    @property
    def client(self) -> AuthenticatedClient:
        """Get the authenticated client.

        Returns:
            AuthenticatedClient: The authenticated client instance.

        Raises:
            RuntimeError: If not signed in.
        """
        return self._client

    def __str__(self) -> str:
        return f"Client for {self.server}"
