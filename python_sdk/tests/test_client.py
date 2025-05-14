from unittest.mock import Mock

import pytest

from src import AuthenticatedClient
from src.client import Client
from src.server import Server


@pytest.fixture
def mock_server():
    server = Mock(spec=Server)
    server.url = "test.tableau.com"
    server.get_auth_token.return_value = "test-token"
    return server


def test_client_initialization(mock_server):
    """Test client initialization"""
    client = Client(mock_server)
    assert client.server == mock_server
    assert client._client is not None
    assert isinstance(client._client, AuthenticatedClient)


def test_create_client_with_https():
    """Test client creation with HTTPS protocol"""
    server = Mock(spec=Server)
    server.url = "10ax.online.tableau.com"
    server.get_auth_token.return_value = "test-token"

    client = Client(server)
    auth_client = client._create_client()

    assert isinstance(auth_client, AuthenticatedClient)
    assert auth_client._base_url.startswith("https://")
    assert auth_client._headers["User-Agent"].startswith("python-sdk/")
    assert auth_client.auth_header_name == "X-Tableau-Auth"
    assert auth_client.prefix == ""
    assert auth_client.token == "test-token"
    assert "/api/v1/vizql-data-service" in auth_client._base_url


def test_create_client_with_http():
    """Test client creation with HTTP protocol"""
    server = Mock(spec=Server)
    server.url = "localhost:8080"
    server.get_auth_token.return_value = "test-token"

    client = Client(server)
    auth_client = client._create_client()

    assert isinstance(auth_client, AuthenticatedClient)
    assert auth_client._base_url.startswith("http://")
    assert auth_client._headers["User-Agent"].startswith("python-sdk/")
    assert auth_client.auth_header_name == "X-Tableau-Auth"
    assert auth_client.prefix == ""
    assert auth_client.token == "test-token"
    assert "/api/v1/vizql-data-service" in auth_client._base_url


def test_client_property(mock_server):
    """Test client property access"""
    client = Client(mock_server)

    # Both accesses should return the same client instance
    auth_client1 = client.client
    auth_client2 = client.client
    assert auth_client1 is auth_client2


def test_client_string_representation(mock_server):
    """Test client string representation"""
    client = Client(mock_server)
    assert str(client) == f"Client for {mock_server}"
