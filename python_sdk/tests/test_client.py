import httpx
import tableauserverclient as TSC

from src.api.client import AuthenticatedClient, VizQLDataServiceClient


def test_authenticated_client_initialization():
    """Test basic initialization of AuthenticatedClient"""
    client = AuthenticatedClient(
        base_url="http://test.com",
        token="test-token",
        prefix="Bearer",
        auth_header_name="Authorization",
    )

    assert client.token == "test-token"
    assert client.prefix == "Bearer"
    assert client.auth_header_name == "Authorization"
    assert client._base_url == "http://test.com"


def test_authenticated_client_with_headers():
    """Test with_headers method"""
    client = AuthenticatedClient(base_url="http://test.com", token="test-token")

    new_client = client.with_headers({"X-Custom-Header": "test"})
    assert new_client._headers["X-Custom-Header"] == "test"
    assert new_client.token == client.token  # Ensure other attributes remain unchanged


def test_authenticated_client_with_cookies():
    """Test with_cookies method"""
    client = AuthenticatedClient(base_url="http://test.com", token="test-token")

    new_client = client.with_cookies({"session": "test-session"})
    assert new_client._cookies["session"] == "test-session"
    assert new_client.token == client.token  # Ensure other attributes remain unchanged


def test_authenticated_client_with_timeout():
    """Test with_timeout method"""
    client = AuthenticatedClient(base_url="http://test.com", token="test-token")

    timeout = httpx.Timeout(10.0)
    new_client = client.with_timeout(timeout)
    assert new_client._timeout == timeout
    assert new_client.token == client.token  # Ensure other attributes remain unchanged


def test_authenticated_client_get_httpx_client():
    """Test get_httpx_client method"""
    client = AuthenticatedClient(
        base_url="http://test.com",
        token="test-token",
        prefix="Bearer",
        auth_header_name="Authorization",
    )

    httpx_client = client.get_httpx_client()
    assert isinstance(httpx_client, httpx.Client)
    assert httpx_client.base_url == "http://test.com"
    assert httpx_client.headers["Authorization"] == "Bearer test-token"


def test_authenticated_client_context_manager():
    """Test context manager functionality"""
    client = AuthenticatedClient(base_url="http://test.com", token="test-token")

    with client as ctx_client:
        assert isinstance(ctx_client, AuthenticatedClient)
        assert ctx_client._client is not None


def test_vizql_data_service_client_initialization():
    """Test initialization of VizQLDataServiceClient"""
    server = TSC.Server("http://test.com")
    auth = TSC.TableauAuth("test-user", "test-password")
    server._auth_token = "test-auth-token"

    client = VizQLDataServiceClient(url="http://test.com", server=server, auth=auth)

    assert client.url == "http://test.com"
    assert client.server == server
    assert client.auth == auth
    assert isinstance(client._client, AuthenticatedClient)
