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
    """Request data source metadata

     Requests metadata for a specific data source. The metadata provides information about the data
    fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataOutput]
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
    """Request data source metadata

     Requests metadata for a specific data source. The metadata provides information about the data
    fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataOutput
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
    """Request data source metadata

     Requests metadata for a specific data source. The metadata provides information about the data
    fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MetadataOutput]
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
    """Request data source metadata

     Requests metadata for a specific data source. The metadata provides information about the data
    fields, such as field names, data types, and descriptions.

    Args:
        body (ReadMetadataRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MetadataOutput
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed


__all__ = [
    "sync_detailed",
    "asyncio_detailed",
]
