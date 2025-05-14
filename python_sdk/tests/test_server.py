import re
from unittest.mock import Mock, patch

import pytest
import tableauserverclient as TSC

from src.server import Server


@pytest.fixture
def mock_tsc_auth():
    with patch("tableauserverclient.PersonalAccessTokenAuth") as mock_pat:
        with patch("tableauserverclient.TableauAuth") as mock_tableau:
            yield mock_pat, mock_tableau


@pytest.fixture
def mock_tsc_server():
    with patch("tableauserverclient.Server") as mock_server:
        server_instance = Mock()
        mock_server.return_value = server_instance
        yield server_instance


def test_server_init_with_pat():
    """Test server initialization with Personal Access Token"""
    server = Server(
        url="test.tableau.com",
        pat_name="test-pat",
        pat_secret="test-secret",
        site_id="test-site",
    )
    assert server.url == "test.tableau.com"
    assert server.pat_name == "test-pat"
    assert server.pat_secret == "test-secret"
    assert server.site_id == "test-site"
    assert server.username is None
    assert server.password is None


def test_server_init_with_credentials():
    """Test server initialization with username/password"""
    server = Server(
        url="test.tableau.com",
        username="test-user",
        password="test-pass",
        site_id="test-site",
    )
    assert server.url == "test.tableau.com"
    assert server.username == "test-user"
    assert server.password == "test-pass"
    assert server.site_id == "test-site"
    assert server.pat_name is None
    assert server.pat_secret is None


def test_server_init_without_auth():
    """Test server initialization without authentication"""
    with pytest.raises(
        ValueError, match="Either username/password or PAT name/secret must be provided"
    ):
        Server(url="test.tableau.com")


def test_server_sign_in(mock_tsc_server):
    """Test server sign in"""
    server = Server(
        url="test.tableau.com", pat_name="test-pat", pat_secret="test-secret"
    )
    mock_tsc_server.auth.sign_in.return_value = "test-token"
    result = server.sign_in()
    assert result == "test-token"
    mock_tsc_server.auth.sign_in.assert_called_once()


def test_get_datasources(mock_tsc_server):
    """Test getting datasources"""
    server = Server(
        url="test.tableau.com", pat_name="test-pat", pat_secret="test-secret"
    )
    mock_tsc_server.auth_token = "test-token"
    mock_datasources = [Mock(spec=TSC.DatasourceItem)]
    mock_pagination = Mock(spec=TSC.PaginationItem)
    mock_tsc_server.datasources.get.return_value = (mock_datasources, mock_pagination)

    datasources, pagination = server.get_datasources()
    assert datasources == mock_datasources
    assert pagination == mock_pagination
    mock_tsc_server.datasources.get.assert_called_once()


def test_get_datasources_not_signed_in(mock_tsc_server):
    """Test getting datasources without signing in"""
    server = Server(
        url="test.tableau.com", pat_name="test-pat", pat_secret="test-secret"
    )
    mock_tsc_server.auth_token = None

    with pytest.raises(
        RuntimeError, match=re.escape("Not signed in. Please call sign_in() first.")
    ):
        server.get_datasources()


def test_get_auth_token(mock_tsc_server):
    """Test getting auth token"""
    server = Server(
        url="test.tableau.com", pat_name="test-pat", pat_secret="test-secret"
    )
    mock_tsc_server.auth_token = "test-token"
    assert server.get_auth_token() == "test-token"


def test_get_auth_token_not_signed_in(mock_tsc_server):
    """Test getting auth token without signing in"""
    server = Server(
        url="test.tableau.com", pat_name="test-pat", pat_secret="test-secret"
    )
    mock_tsc_server.auth_token = None

    with pytest.raises(
        RuntimeError, match=re.escape("Not signed in. Please call sign_in() first.")
    ):
        server.get_auth_token()


def test_server_string_representation():
    """Test server string representation"""
    server = Server(
        url="test.tableau.com",
        site_id="test-site",
        pat_name="test-pat",
        pat_secret="test-secret",
    )
    expected_str = "Server: test.tableau.com\nSite: test-site"
    assert str(server) == expected_str


def test_get_server_info():
    """Test getting server info"""
    server = Server(
        url="test.tableau.com",
        site_id="test-site",
        pat_name="test-pat",
        pat_secret="test-secret",
    )
    expected_info = {"serverName": "test.tableau.com", "site": "test-site"}
    assert server.get_server_info() == expected_info
