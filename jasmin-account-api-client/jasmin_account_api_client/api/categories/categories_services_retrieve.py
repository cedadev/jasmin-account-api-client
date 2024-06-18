from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.service import Service
from ...types import Response


def _get_kwargs(
    category_name: str,
    name: str,
) -> Dict[str, Any]:

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/categories/{category_name}/services/{name}/".format(
            category_name=category_name,
            name=name,
        ),
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Service]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Service.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Service]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    category_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Service]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (str): The name of the service. This is also used in URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Service]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
        name=name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    category_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Service]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (str): The name of the service. This is also used in URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Service
    """

    return sync_detailed(
        category_name=category_name,
        name=name,
        client=client,
    ).parsed


async def asyncio_detailed(
    category_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Response[Service]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (str): The name of the service. This is also used in URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Service]
    """

    kwargs = _get_kwargs(
        category_name=category_name,
        name=name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    category_name: str,
    name: str,
    *,
    client: AuthenticatedClient,
) -> Optional[Service]:
    """Viewset to allow services to be nested under categories.

    Same as ServicesViewset, but lookup the service by name instead of pk,
    and filter by category.

    Args:
        category_name (str):
        name (str): The name of the service. This is also used in URLs.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Service
    """

    return (
        await asyncio_detailed(
            category_name=category_name,
            name=name,
            client=client,
        )
    ).parsed
