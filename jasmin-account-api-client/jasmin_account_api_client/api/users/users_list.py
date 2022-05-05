from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.user_list import UserList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[UserList]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[UserList]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
) -> Response[List[UserList]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):

    Returns:
        Response[List[UserList]]
    """

    kwargs = _get_kwargs(
        client=client,
        institution=institution,
        is_active=is_active,
        ordering=ordering,
        search=search,
        service_user=service_user,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
) -> Optional[List[UserList]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):

    Returns:
        Response[List[UserList]]
    """

    return sync_detailed(
        client=client,
        institution=institution,
        is_active=is_active,
        ordering=ordering,
        search=search,
        service_user=service_user,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
) -> Response[List[UserList]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):

    Returns:
        Response[List[UserList]]
    """

    kwargs = _get_kwargs(
        client=client,
        institution=institution,
        is_active=is_active,
        ordering=ordering,
        search=search,
        service_user=service_user,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    institution: Union[Unset, None, int] = UNSET,
    is_active: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
    service_user: Union[Unset, None, bool] = UNSET,
) -> Optional[List[UserList]]:
    """View jasmin_auth Users.

    Args:
        institution (Union[Unset, None, int]):
        is_active (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):
        service_user (Union[Unset, None, bool]):

    Returns:
        Response[List[UserList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            institution=institution,
            is_active=is_active,
            ordering=ordering,
            search=search,
            service_user=service_user,
        )
    ).parsed
