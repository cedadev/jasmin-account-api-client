from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.category_list import CategoryList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/categories/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["name"] = name

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


def _parse_response(*, response: httpx.Response) -> Optional[List[CategoryList]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CategoryList.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[CategoryList]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[CategoryList]]:
    """Details of services categories.

    Args:
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[CategoryList]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
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
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[CategoryList]]:
    """Details of services categories.

    Args:
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[CategoryList]]
    """

    return sync_detailed(
        client=client,
        name=name,
        ordering=ordering,
        search=search,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Response[List[CategoryList]]:
    """Details of services categories.

    Args:
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[CategoryList]]
    """

    kwargs = _get_kwargs(
        client=client,
        name=name,
        ordering=ordering,
        search=search,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    name: Union[Unset, None, str] = UNSET,
    ordering: Union[Unset, None, str] = UNSET,
    search: Union[Unset, None, str] = UNSET,
) -> Optional[List[CategoryList]]:
    """Details of services categories.

    Args:
        name (Union[Unset, None, str]):
        ordering (Union[Unset, None, str]):
        search (Union[Unset, None, str]):

    Returns:
        Response[List[CategoryList]]
    """

    return (
        await asyncio_detailed(
            client=client,
            name=name,
            ordering=ordering,
            search=search,
        )
    ).parsed
