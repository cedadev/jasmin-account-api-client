from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_list import UserList
from ...models.users_list_lifecycle_state import UsersListLifecycleState
from ...models.users_list_user_type import UsersListUserType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    institution: Union[Unset, int] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    lifecycle_state: Union[Unset, UsersListLifecycleState] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service_user: Union[Unset, bool] = UNSET,
    user_type: Union[Unset, UsersListUserType] = UNSET,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["institution"] = institution

    params["is_active"] = is_active

    json_lifecycle_state: Union[Unset, str] = UNSET
    if not isinstance(lifecycle_state, Unset):
        json_lifecycle_state = lifecycle_state.value

    params["lifecycle_state"] = json_lifecycle_state

    params["ordering"] = ordering

    params["search"] = search

    params["service_user"] = service_user

    json_user_type: Union[Unset, str] = UNSET
    if not isinstance(user_type, Unset):
        json_user_type = user_type.value

    params["user_type"] = json_user_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/users/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["UserList"]]:
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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["UserList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, int] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    lifecycle_state: Union[Unset, UsersListLifecycleState] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service_user: Union[Unset, bool] = UNSET,
    user_type: Union[Unset, UsersListUserType] = UNSET,
) -> Response[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        lifecycle_state (Union[Unset, UsersListLifecycleState]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):
        service_user (Union[Unset, bool]):
        user_type (Union[Unset, UsersListUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserList']]
    """

    kwargs = _get_kwargs(
        institution=institution,
        is_active=is_active,
        lifecycle_state=lifecycle_state,
        ordering=ordering,
        search=search,
        service_user=service_user,
        user_type=user_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, int] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    lifecycle_state: Union[Unset, UsersListLifecycleState] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service_user: Union[Unset, bool] = UNSET,
    user_type: Union[Unset, UsersListUserType] = UNSET,
) -> Optional[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        lifecycle_state (Union[Unset, UsersListLifecycleState]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):
        service_user (Union[Unset, bool]):
        user_type (Union[Unset, UsersListUserType]):

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
        lifecycle_state=lifecycle_state,
        ordering=ordering,
        search=search,
        service_user=service_user,
        user_type=user_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, int] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    lifecycle_state: Union[Unset, UsersListLifecycleState] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service_user: Union[Unset, bool] = UNSET,
    user_type: Union[Unset, UsersListUserType] = UNSET,
) -> Response[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        lifecycle_state (Union[Unset, UsersListLifecycleState]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):
        service_user (Union[Unset, bool]):
        user_type (Union[Unset, UsersListUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['UserList']]
    """

    kwargs = _get_kwargs(
        institution=institution,
        is_active=is_active,
        lifecycle_state=lifecycle_state,
        ordering=ordering,
        search=search,
        service_user=service_user,
        user_type=user_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, int] = UNSET,
    is_active: Union[Unset, bool] = UNSET,
    lifecycle_state: Union[Unset, UsersListLifecycleState] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    service_user: Union[Unset, bool] = UNSET,
    user_type: Union[Unset, UsersListUserType] = UNSET,
) -> Optional[List["UserList"]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, int]):
        is_active (Union[Unset, bool]):
        lifecycle_state (Union[Unset, UsersListLifecycleState]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):
        service_user (Union[Unset, bool]):
        user_type (Union[Unset, UsersListUserType]):

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
            lifecycle_state=lifecycle_state,
            ordering=ordering,
            search=search,
            service_user=service_user,
            user_type=user_type,
        )
    ).parsed
