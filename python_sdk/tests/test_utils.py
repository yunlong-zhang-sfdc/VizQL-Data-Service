import pytest

from src.utils import format_server_url


def test_format_server_url_with_online_tableau():
    """Test URL formatting for online.tableau.com"""
    url = "online.tableau.com"
    formatted = format_server_url(url)
    assert formatted == "https://online.tableau.com"


def test_format_server_url_with_http():
    """Test URL formatting with existing http protocol"""
    url = "http://test.tableau.com"
    formatted = format_server_url(url)
    assert formatted == "http://test.tableau.com"


def test_format_server_url_with_https():
    """Test URL formatting with existing https protocol"""
    url = "https://test.tableau.com"
    formatted = format_server_url(url)
    assert formatted == "https://test.tableau.com"


def test_format_server_url_with_subdomain():
    """Test URL formatting with subdomain"""
    url = "test.tableau.com"
    subdomain = "/api/v1/test"
    formatted = format_server_url(url, subdomain)
    assert formatted == "http://test.tableau.com/api/v1/test"


def test_format_server_url_with_protocol_and_subdomain():
    """Test URL formatting with protocol and subdomain"""
    url = "https://test.tableau.com"
    subdomain = "/api/v1/test"
    formatted = format_server_url(url, subdomain)
    assert formatted == "https://test.tableau.com/api/v1/test"


def test_format_server_url_with_empty_url():
    """Test URL formatting with empty URL"""
    url = ""
    with pytest.raises(ValueError, match="URL cannot be empty"):
        format_server_url(url)


def test_format_server_url_with_none_url():
    """Test URL formatting with None URL"""
    url = None
    with pytest.raises(TypeError, match="URL must be a string"):
        format_server_url(url)


def test_format_server_url_with_invalid_url():
    """Test URL formatting with invalid URL"""
    url = "invalid url with spaces"
    with pytest.raises(ValueError, match="Invalid URL format"):
        format_server_url(url)


def test_format_server_url_with_special_characters():
    """Test URL formatting with special characters"""
    url = "test.tableau.com/path?query=value#fragment"
    formatted = format_server_url(url)
    assert formatted == "http://test.tableau.com/path?query=value#fragment"


def test_format_server_url_with_port():
    """Test URL formatting with port number"""
    url = "test.tableau.com:8080"
    formatted = format_server_url(url)
    assert formatted == "http://test.tableau.com:8080"


def test_format_server_url_with_multiple_subdomains():
    """Test URL formatting with multiple subdomains"""
    url = "test.tableau.com"
    subdomain = "/api/v1/test/subdomain"
    formatted = format_server_url(url, subdomain)
    assert formatted == "http://test.tableau.com/api/v1/test/subdomain"


def test_format_server_url_with_trailing_slash():
    """Test URL formatting with trailing slash"""
    url = "test.tableau.com/"
    subdomain = "/api/v1/test"
    formatted = format_server_url(url, subdomain)
    assert formatted == "http://test.tableau.com/api/v1/test"
