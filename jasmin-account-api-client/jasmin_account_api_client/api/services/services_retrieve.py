from typing import Any, Dict, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.service import Service
from ...types import Response


def _get_kwargs(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/services/{id}/".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Service]:
    if response.status_code == 200:
        response_200 = Service.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[Service]:
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
) -> Response[Service]:
    """View and get details of a service.

    Args:
        id (int):

    Returns:
        Response[Service]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
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
) -> Optional[Service]:
    """View and get details of a service.

    Args:
        id (int):

    Returns:
        Response[Service]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Service]:
    """View and get details of a service.

    Args:
        id (int):

    Returns:
        Response[Service]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Service]:
    """View and get details of a service.

    Args:
        id (int):

    Returns:
        Response[Service]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
