from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_list import UserList
from ...models.users_list_user_type import UsersListUserType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
    user_type: Union[Unset, None, UsersListUserType] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/users/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["institution"] = institution

    params["is_active"] = is_active

    params["ordering"] = ordering

    params["search"] = search

    params["service_user"] = service_user

    json_user_type: Union[Unset, None, str] = UNSET
    if not isinstance(user_type, Unset):
        json_user_type = user_type.value if user_type else None

    params["user_type"] = json_user_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[List["UserList"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[List["UserList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
    user_type: Union[Unset, None, UsersListUserType] = UNSET,
) -> Response[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):
        user_type (Union[Unset, None, UsersListUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserList']]
    """

    kwargs = _get_kwargs(
        client=client,
        institution=institution,
        is_active=is_active,
        ordering=ordering,
        search=search,
        service_user=service_user,
        user_type=user_type,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
    user_type: Union[Unset, None, UsersListUserType] = UNSET,
) -> Optional[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):
        user_type (Union[Unset, None, UsersListUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UserList']
    """

    return sync_detailed(
        client=client,
        institution=institution,
        is_active=is_active,
        ordering=ordering,
        search=search,
        service_user=service_user,
        user_type=user_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
    user_type: Union[Unset, None, UsersListUserType] = UNSET,
) -> Response[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):
        user_type (Union[Unset, None, UsersListUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserList']]
    """

    kwargs = _get_kwargs(
        client=client,
        institution=institution,
        is_active=is_active,
        ordering=ordering,
        search=search,
        service_user=service_user,
        user_type=user_type,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
    user_type: Union[Unset, None, UsersListUserType] = UNSET,
) -> Optional[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):
        user_type (Union[Unset, None, UsersListUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['UserList']
    """

    return (
        await asyncio_detailed(
            client=client,
            institution=institution,
            is_active=is_active,
            ordering=ordering,
            search=search,
            service_user=service_user,
            user_type=user_type,
        )
    ).parsed
