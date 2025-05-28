from http import HTTPStatus
from typing import Any, Optional

import httpx

from .client import AuthenticatedClient
from .errors import UnexpectedStatus
from .openapi_generated import QueryOutput, QueryRequest
from .types import Response


def _get_kwargs(
    *,
    body: QueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/query-datasource",
    }

    _body = body.model_dump(mode="json", exclude_none=True)

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Optional[QueryOutput]:
    if response.status_code == 200:
        response_200 = QueryOutput.model_validate_json(response.content)

        return response_200
    if client.raise_on_unexpected_status:
        raise UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Response[QueryOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Response[QueryOutput]:
    """Query data source with detailed response information

     Queries a specific data source and returns a detailed response containing:
     - The query results (QueryOutput)
     - HTTP status code
     - Response headers
     - Raw response content

    Args:
        body (QueryRequest): The query request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryOutput]: A response object containing both the query results and response metadata
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Optional[QueryOutput]:
    """Query data source and get only the query results

     Queries a specific data source and returns only the query results without response metadata.
     This is a convenience wrapper around sync_detailed() that returns only the parsed query results.

    Args:
        body (QueryRequest): The query request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[QueryOutput]: The query results, or None if the request was unsuccessful
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Response[QueryOutput]:
    """Query data source asynchronously with detailed response information

     Asynchronously queries a specific data source and returns a detailed response containing:
     - The query results (QueryOutput)
     - HTTP status code
     - Response headers
     - Raw response content

    Args:
        body (QueryRequest): The query request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[QueryOutput]: A response object containing both the query results and response metadata
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: QueryRequest,
) -> Optional[QueryOutput]:
    """Query data source asynchronously and get only the query results

     Asynchronously queries a specific data source and returns only the query results without response metadata.
     This is a convenience wrapper around asyncio_detailed() that returns only the parsed query results.

    Args:
        body (QueryRequest): The query request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[QueryOutput]: The query results, or None if the request was unsuccessful
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed


__all__ = [
    "sync",
    "sync_detailed",
    "asyncio",
    "asyncio_detailed",
]
