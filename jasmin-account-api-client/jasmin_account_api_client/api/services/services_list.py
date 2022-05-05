from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.service_list import ServiceList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, None, int] = UNSET,
    ceda_managed: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/services/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["category"] = category

    params["ceda_managed"] = ceda_managed

    params["hidden"] = hidden

    params["ordering"] = ordering

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[ServiceList]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ServiceList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[ServiceList]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, None, int] = UNSET,
    ceda_managed: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[ServiceList]]:
    """View and get details of a service.

    Args:
        category (Union[Unset, None, int]):
        ceda_managed (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[ServiceList]]
    """

    kwargs = _get_kwargs(
        client=client,
        category=category,
        ceda_managed=ceda_managed,
        hidden=hidden,
        ordering=ordering,
        search=search,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, None, int] = UNSET,
    ceda_managed: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[ServiceList]]:
    """View and get details of a service.

    Args:
        category (Union[Unset, None, int]):
        ceda_managed (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[ServiceList]]
    """

    return sync_detailed(
        client=client,
        category=category,
        ceda_managed=ceda_managed,
        hidden=hidden,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, None, int] = UNSET,
    ceda_managed: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[ServiceList]]:
    """View and get details of a service.

    Args:
        category (Union[Unset, None, int]):
        ceda_managed (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[ServiceList]]
    """

    kwargs = _get_kwargs(
        client=client,
        category=category,
        ceda_managed=ceda_managed,
        hidden=hidden,
        ordering=ordering,
        search=search,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    category: Union[Unset, None, int] = UNSET,
    ceda_managed: Union[Unset, None, bool] = UNSET,
    hidden: Union[Unset, None, bool] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[ServiceList]]:
    """View and get details of a service.

    Args:
        category (Union[Unset, None, int]):
        ceda_managed (Union[Unset, None, bool]):
        hidden (Union[Unset, None, bool]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[ServiceList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            category=category,
            ceda_managed=ceda_managed,
            hidden=hidden,
            ordering=ordering,
            search=search,
        )
    ).parsed