from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.role import Role
from ...types import Response


def _get_kwargs(
    service_id: int,
    name: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/services/{service_id}/roles/{name}/".format(
            service_id=service_id,
            name=name,
        ),
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Role]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Role.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Role]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_id: int,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Role]:
    """View roles for a service.

    Args:
        service_id (int):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Role]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: int,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Role]:
    """View roles for a service.

    Args:
        service_id (int):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Role
    """

    return sync_detailed(
        service_id=service_id,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_id: int,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Role]:
    """View roles for a service.

    Args:
        service_id (int):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Role]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: int,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Role]:
    """View roles for a service.

    Args:
        service_id (int):
        name (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Role
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            name=name,
            client=client,
        )
    ).parsed
