from unittest.mock import AsyncMock, Mock

import pytest

from src.api.client import AuthenticatedClient
from src.api.query_datasource import asyncio, asyncio_detailed, sync, sync_detailed
from src.openapi_client import (
    Datasource,
    Query,
    QueryOutput,
    QueryRequest,
    SimpleField,
    TabField,
)


@pytest.fixture
def mock_client():
    client = Mock(spec=AuthenticatedClient)
    client.raise_on_unexpected_status = True
    return client


@pytest.fixture
def mock_async_client():
    client = Mock(spec=AuthenticatedClient)
    client.raise_on_unexpected_status = True
    async_client = AsyncMock()
    client.get_async_httpx_client.return_value = async_client
    return client


@pytest.fixture
def mock_query_request():
    return QueryRequest(
        datasource=Datasource(datasourceLuid="test_datasource"),
        query=Query(
            fields=[
                TabField(root=SimpleField(fieldCaption="id")),
                TabField(root=SimpleField(fieldCaption="name")),
            ]
        ),
    )


def test_sync_detailed_success(mock_client, mock_query_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"id": 1, "name": "test"}]}'
    mock_response.headers = {}

    mock_client.get_httpx_client.return_value.request.return_value = mock_response

    response = sync_detailed(client=mock_client, body=mock_query_request)

    assert response.status_code == 200
    assert isinstance(response.parsed, QueryOutput)
    assert response.content == b'{"data": [{"id": 1, "name": "test"}]}'


def test_sync_success(mock_client, mock_query_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"id": 1, "name": "test"}]}'
    mock_response.headers = {}

    mock_client.get_httpx_client.return_value.request.return_value = mock_response

    result = sync(client=mock_client, body=mock_query_request)

    assert isinstance(result, QueryOutput)


@pytest.mark.asyncio
async def test_asyncio_detailed_success(mock_async_client, mock_query_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"id": 1, "name": "test"}]}'
    mock_response.headers = {}

    mock_async_client.get_async_httpx_client.return_value.request.return_value = (
        mock_response
    )

    response = await asyncio_detailed(client=mock_async_client, body=mock_query_request)

    assert response.status_code == 200
    assert isinstance(response.parsed, QueryOutput)
    assert response.content == b'{"data": [{"id": 1, "name": "test"}]}'


@pytest.mark.asyncio
async def test_asyncio_success(mock_async_client, mock_query_request):
    # Mock successful response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'{"data": [{"id": 1, "name": "test"}]}'
    mock_response.headers = {}

    mock_async_client.get_async_httpx_client.return_value.request.return_value = (
        mock_response
    )

    result = await asyncio(client=mock_async_client, body=mock_query_request)

    assert isinstance(result, QueryOutput)
