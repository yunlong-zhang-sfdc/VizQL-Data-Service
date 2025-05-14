"""
Server Model Module

This module provides the Server model class for handling server configuration information.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

import tableauserverclient as TSC

from .utils import format_server_url


@dataclass
class Server:
    """Server configuration for VizQL Data Service."""

    url: str
    username: Optional[str] = None
    password: Optional[str] = None
    pat_name: Optional[str] = None
    pat_secret: Optional[str] = None
    site_id: str = ""

    def __post_init__(self):
        if self.pat_name and self.pat_secret:
            self.auth = TSC.PersonalAccessTokenAuth(
                self.pat_name, self.pat_secret, self.site_id
            )
        elif self.username and self.password:
            self.auth = TSC.TableauAuth(self.username, self.password, self.site_id)
        else:
            raise ValueError(
                "Either username/password or PAT name/secret must be provided"
            )

        self.server = TSC.Server(format_server_url(self.url))

    def sign_in(self):
        """Sign in to the server."""
        return self.server.auth.sign_in(self.auth)

    def get_datasources(self) -> Tuple[List[TSC.DatasourceItem], TSC.PaginationItem]:
        """Get all datasources from the server.

        Returns:
            Tuple[List[TSC.DatasourceItem], TSC.PaginationItem]: A tuple containing:
                - List of datasource items
                - Pagination information

        Raises:
            RuntimeError: If not signed in.
        """
        if not self.server.auth_token:
            raise RuntimeError("Not signed in. Please call sign_in() first.")
        return self.server.datasources.get()

    def __str__(self) -> str:
        return f"Server: {self.url}\nSite: {self.site_id}"

    def get_server_info(self) -> Dict[str, str]:
        return {"serverName": self.url, "site": self.site_id}

    def get_auth_token(self) -> str:
        """Get the authentication token.

        Returns:
            str: The authentication token.

        Raises:
            RuntimeError: If not signed in.
        """
        if not self.server.auth_token:
            raise RuntimeError("Not signed in. Please call sign_in() first.")
        return self.server.auth_token
