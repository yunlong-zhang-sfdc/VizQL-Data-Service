from http import HTTPStatus
from typing import Any, Optional

import httpx

from .client import AuthenticatedClient
from .errors import UnexpectedStatus
from .openapi_generated import MetadataOutput, ReadMetadataRequest
from .types import Response


def _get_kwargs(
    *,
    body: ReadMetadataRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/read-metadata",
    }

    _body = body.model_dump(mode="json", exclude_none=True)
    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Optional[MetadataOutput]:
    if response.status_code == 200:
        response_200 = MetadataOutput.model_validate_json(response.content)

        return response_200
    if client.raise_on_unexpected_status:
        raise UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient, response: httpx.Response
) -> Response[MetadataOutput]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ReadMetadataRequest,
) -> Response[MetadataOutput]:
    """Request data source metadata with detailed response information

     Requests metadata for a specific data source and returns a detailed response containing:
     - The metadata information (MetadataOutput)
     - HTTP status code
     - Response headers
     - Raw response content

     The metadata provides information about the data fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest): The metadata request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataOutput]: A response object containing both the metadata and response metadata
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
    body: ReadMetadataRequest,
) -> Optional[MetadataOutput]:
    """Request data source metadata and get only the metadata information

     Requests metadata for a specific data source and returns only the metadata information without response metadata.
     This is a convenience wrapper around sync_detailed() that returns only the parsed metadata.

     The metadata provides information about the data fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest): The metadata request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[MetadataOutput]: The metadata information, or None if the request was unsuccessful
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ReadMetadataRequest,
) -> Response[MetadataOutput]:
    """Request data source metadata asynchronously with detailed response information

     Asynchronously requests metadata for a specific data source and returns a detailed response containing:
     - The metadata information (MetadataOutput)
     - HTTP status code
     - Response headers
     - Raw response content

     The metadata provides information about the data fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest): The metadata request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataOutput]: A response object containing both the metadata and response metadata
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ReadMetadataRequest,
) -> Optional[MetadataOutput]:
    """Request data source metadata asynchronously and get only the metadata information

     Asynchronously requests metadata for a specific data source and returns only the metadata information without response metadata.
     This is a convenience wrapper around asyncio_detailed() that returns only the parsed metadata.

     The metadata provides information about the data fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest): The metadata request parameters

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Optional[MetadataOutput]: The metadata information, or None if the request was unsuccessful
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
