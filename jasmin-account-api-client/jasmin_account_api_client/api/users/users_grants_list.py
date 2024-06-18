from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_grant import UserGrant
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_username: str,
    *,
    category: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["category"] = category

    params["ordering"] = ordering

    params["role"] = role

    params["search"] = search

    params["service"] = service

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/{user_username}/grants/".format(
            user_username=user_username,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["UserGrant"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserGrant.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["UserGrant"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_username: str,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
) -> Response[List["UserGrant"]]:
    """Get the grants associated with a user.

    Args:
        user_username (str):
        category (Union[Unset, str]):
        ordering (Union[Unset, str]):
        role (Union[Unset, str]):
        search (Union[Unset, str]):
        service (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserGrant']]
    """

    kwargs = _get_kwargs(
        user_username=user_username,
        category=category,
        ordering=ordering,
        role=role,
        search=search,
        service=service,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_username: str,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
) -> Optional[List["UserGrant"]]:
    """Get the grants associated with a user.

    Args:
        user_username (str):
        category (Union[Unset, str]):
        ordering (Union[Unset, str]):
        role (Union[Unset, str]):
        search (Union[Unset, str]):
        service (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UserGrant']
    """

    return sync_detailed(
        user_username=user_username,
        client=client,
        category=category,
        ordering=ordering,
        role=role,
        search=search,
        service=service,
    ).parsed


async def asyncio_detailed(
    user_username: str,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
) -> Response[List["UserGrant"]]:
    """Get the grants associated with a user.

    Args:
        user_username (str):
        category (Union[Unset, str]):
        ordering (Union[Unset, str]):
        role (Union[Unset, str]):
        search (Union[Unset, str]):
        service (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserGrant']]
    """

    kwargs = _get_kwargs(
        user_username=user_username,
        category=category,
        ordering=ordering,
        role=role,
        search=search,
        service=service,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_username: str,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    role: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service: Union[Unset, str] = UNSET,
) -> Optional[List["UserGrant"]]:
    """Get the grants associated with a user.

    Args:
        user_username (str):
        category (Union[Unset, str]):
        ordering (Union[Unset, str]):
        role (Union[Unset, str]):
        search (Union[Unset, str]):
        service (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UserGrant']
    """

    return (
        await asyncio_detailed(
            user_username=user_username,
            client=client,
            category=category,
            ordering=ordering,
            role=role,
            search=search,
            service=service,
        )
    ).parsed
