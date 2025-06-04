from unittest.mock import AsyncMock, Mock

import pytest

from src.api.client import AuthenticatedClient, VizQLDataServiceClient
from src.api.openapi_generated import Datasource, MetadataOutput, ReadMetadataRequest
from src.api.read_metadata import asyncio, asyncio_detailed, sync, sync_detailed


@pytest.fixture
def mock_client():
    client = Mock(spec=VizQLDataServiceClient)
    client.raise_on_unexpected_status = True
    mock_authenticated_client = Mock(spec=AuthenticatedClient)
    mock_httpx_client = Mock()
    mock_authenticated_client.get_httpx_client.return_value = mock_httpx_client
    client.client = mock_authenticated_client
    return client


@pytest.fixture
def mock_async_client():
    client = Mock(spec=VizQLDataServiceClient)
    client.raise_on_unexpected_status = True
    mock_authenticated_client = Mock(spec=AuthenticatedClient)
    mock_async_httpx_client = AsyncMock()
    mock_authenticated_client.get_async_httpx_client.return_value = (
        mock_async_httpx_client
    )
    client.client = mock_authenticated_client
    return client


@pytest.fixture
def mock_metadata_request():
    return ReadMetadataRequest(datasource=Datasource(datasourceLuid="test_datasource"))


def test_sync_detailed_success(mock_client, mock_metadata_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"fieldName": "id", "dataType": "INTEGER"}, {"fieldName": "name", "dataType": "STRING"}]}'
    mock_response.headers = {}

    mock_client.client.get_httpx_client.return_value.request.return_value = (
        mock_response
    )

    response = sync_detailed(client=mock_client, body=mock_metadata_request)

    assert response.status_code == 200
    assert isinstance(response.parsed, MetadataOutput)
    assert (
        response.content
        == b'{"data": [{"fieldName": "id", "dataType": "INTEGER"}, {"fieldName": "name", "dataType": "STRING"}]}'
    )


def test_sync_success(mock_client, mock_metadata_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"fieldName": "id", "dataType": "INTEGER"}, {"fieldName": "name", "dataType": "STRING"}]}'
    mock_response.headers = {}

    mock_client.client.get_httpx_client.return_value.request.return_value = (
        mock_response
    )

    result = sync(client=mock_client, body=mock_metadata_request)

    assert isinstance(result, MetadataOutput)


@pytest.mark.asyncio
async def test_asyncio_detailed_success(mock_async_client, mock_metadata_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"fieldName": "id", "dataType": "INTEGER"}, {"fieldName": "name", "dataType": "STRING"}]}'
    mock_response.headers = {}

    mock_async_client.client.get_async_httpx_client.return_value.request.return_value = (
        mock_response
    )

    response = await asyncio_detailed(
        client=mock_async_client, body=mock_metadata_request
    )

    assert response.status_code == 200
    assert isinstance(response.parsed, MetadataOutput)
    assert (
        response.content
        == b'{"data": [{"fieldName": "id", "dataType": "INTEGER"}, {"fieldName": "name", "dataType": "STRING"}]}'
    )


@pytest.mark.asyncio
async def test_asyncio_success(mock_async_client, mock_metadata_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"fieldName": "id", "dataType": "INTEGER"}, {"fieldName": "name", "dataType": "STRING"}]}'
    mock_response.headers = {}

    mock_async_client.client.get_async_httpx_client.return_value.request.return_value = (
        mock_response
    )

    result = await asyncio(client=mock_async_client, body=mock_metadata_request)

    assert isinstance(result, MetadataOutput)
