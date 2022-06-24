import datetime
from typing import Any, Dict, List, Optional, Union

import httpx

from ...client import AuthenticatedClient
from ...models.role import Role
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
    on_date: Union[Unset, None, datetime.date] = UNSET,
) -> Dict[str, Any]:
    url = "{}/api/v1/services/{id}/roles/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_on_date: Union[Unset, None, str] = UNSET
    if not isinstance(on_date, Unset):
        json_on_date = on_date.isoformat() if on_date else None

    params["on_date"] = json_on_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[List[Role]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Role.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List[Role]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    on_date: Union[Unset, None, datetime.date] = UNSET,
) -> Response[List[Role]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        on_date (Union[Unset, None, datetime.date]):

    Returns:
        Response[List[Role]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        on_date=on_date,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: int,
    *,
    client: AuthenticatedClient,
    on_date: Union[Unset, None, datetime.date] = UNSET,
) -> Optional[List[Role]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        on_date (Union[Unset, None, datetime.date]):

    Returns:
        Response[List[Role]]
    """

    return sync_detailed(
        id=id,
        client=client,
        on_date=on_date,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
    on_date: Union[Unset, None, datetime.date] = UNSET,
) -> Response[List[Role]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        on_date (Union[Unset, None, datetime.date]):

    Returns:
        Response[List[Role]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        on_date=on_date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
    on_date: Union[Unset, None, datetime.date] = UNSET,
) -> Optional[List[Role]]:
    """List roles in a services and their holders.

    Args:
        id (int):
        on_date (Union[Unset, None, datetime.date]):

    Returns:
        Response[List[Role]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            on_date=on_date,
        )
    ).parsed
