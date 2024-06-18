from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service_list import ServiceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    category_name: str,
    *,
    name: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Dict[str, Any]:

    params: Dict[str, Any] = {}

    params["name"] = name

    params["ordering"] = ordering

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/categories/{category_name}/services/".format(
            category_name=category_name,
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ServiceList"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ServiceList"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_name: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[List["ServiceList"]]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (Union[Unset, str]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ServiceList']]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
        name=name,
        ordering=ordering,
        search=search,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_name: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[List["ServiceList"]]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (Union[Unset, str]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ServiceList']
    """

    return sync_detailed(
        category_name=category_name,
        client=client,
        name=name,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    category_name: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Response[List["ServiceList"]]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (Union[Unset, str]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ServiceList']]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
        name=name,
        ordering=ordering,
        search=search,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_name: str,
    *,
    client: AuthenticatedClient,
    name: Union[Unset, str] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
) -> Optional[List["ServiceList"]]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (Union[Unset, str]):
        ordering (Union[Unset, str]):
        search (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ServiceList']
    """

    return (
        await asyncio_detailed(
            category_name=category_name,
            client=client,
            name=name,
            ordering=ordering,
            search=search,
        )
    ).parsed
