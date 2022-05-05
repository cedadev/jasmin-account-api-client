from typing import Any, Dict, List, Optional

import httpx

from ...client import AuthenticatedClient
from ...models.service_list import ServiceList
from ...types import Response


def _get_kwargs(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/api/v1/users/{username}/services/".format(client.base_url, username=username)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[ServiceList]]:
    """List the services of a given user.

    Args:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    Returns:
        Response[List[ServiceList]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List[ServiceList]]:
    """List the services of a given user.

    Args:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    Returns:
        Response[List[ServiceList]]
    """

    return sync_detailed(
        username=username,
        client=client,
    ).parsed


async def asyncio_detailed(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Response[List[ServiceList]]:
    """List the services of a given user.

    Args:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    Returns:
        Response[List[ServiceList]]
    """

    kwargs = _get_kwargs(
        username=username,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    username: str,
    *,
    client: AuthenticatedClient,
) -> Optional[List[ServiceList]]:
    """List the services of a given user.

    Args:
        username (str): Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.

    Returns:
        Response[List[ServiceList]]
    """

    return (
        await asyncio_detailed(
            username=username,
            client=client,
        )
    ).parsed
