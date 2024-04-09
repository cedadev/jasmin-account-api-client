import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.role import Role
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    category: Union[Unset, int] = UNSET,
    ceda_managed: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    on_date: Union[Unset, datetime.date] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["category"] = category

    params["ceda_managed"] = ceda_managed

    params["hidden"] = hidden

    json_on_date: Union[Unset, str] = UNSET
    if not isinstance(on_date, Unset):
        json_on_date = on_date.isoformat()
    params["on_date"] = json_on_date

    params["ordering"] = ordering

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/services/{id}/roles/".format(
            id=id,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[List["Role"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Role.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[List["Role"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, int] = UNSET,
    ceda_managed: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    on_date: Union[Unset, datetime.date] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[List["Role"]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        category (Union[Unset, int]):
        ceda_managed (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        on_date (Union[Unset, datetime.date]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Role']]
    """

    kwargs = _get_kwargs(
        id=id,
        category=category,
        ceda_managed=ceda_managed,
        hidden=hidden,
        on_date=on_date,
        ordering=ordering,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, int] = UNSET,
    ceda_managed: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    on_date: Union[Unset, datetime.date] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[List["Role"]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        category (Union[Unset, int]):
        ceda_managed (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        on_date (Union[Unset, datetime.date]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Role']
    """

    return sync_detailed(
        id=id,
        client=client,
        category=category,
        ceda_managed=ceda_managed,
        hidden=hidden,
        on_date=on_date,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, int] = UNSET,
    ceda_managed: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    on_date: Union[Unset, datetime.date] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[List["Role"]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        category (Union[Unset, int]):
        ceda_managed (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        on_date (Union[Unset, datetime.date]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['Role']]
    """

    kwargs = _get_kwargs(
        id=id,
        category=category,
        ceda_managed=ceda_managed,
        hidden=hidden,
        on_date=on_date,
        ordering=ordering,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    category: Union[Unset, int] = UNSET,
    ceda_managed: Union[Unset, bool] = UNSET,
    hidden: Union[Unset, bool] = UNSET,
    on_date: Union[Unset, datetime.date] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[List["Role"]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        category (Union[Unset, int]):
        ceda_managed (Union[Unset, bool]):
        hidden (Union[Unset, bool]):
        on_date (Union[Unset, datetime.date]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['Role']
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            category=category,
            ceda_managed=ceda_managed,
            hidden=hidden,
            on_date=on_date,
            ordering=ordering,
            search=search,
        )
    ).parsed
