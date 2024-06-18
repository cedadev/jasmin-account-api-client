"""Retrieve list of usernames who hold access to a service."""

import asyncio
import json
import os

import httpx
import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.services as jservices
import jasmin_account_api_client.api.users as jusers

ROLE_NAME = ["MANAGER", "DEPUTY"]


async def main():
    client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
    client.client_credentials_flow(
        client_id=os.environ["JASMIN_CLIENT_ID"],
        client_secret=os.environ["JASMIN_CLIENT_SECRET"],
        scopes=[
            "jasmin.services.serviceroles.all:read",
            "jasmin.services.services.all:read",
            "jasmin.auth.users.all:read",
        ],
    )

    # Get a list of all the services.
    services = jservices.services_list.sync(client=client)
    # Get a list of all the users
    all_users = jusers.users_list.sync(client=client)

    service_roles = {}
    failed = [x.id for x in services]

    async def get_service_roles(service_id):
        try:
            service_roles[service_id] = await jservices.services_roles_list.asyncio(
                service_id, client=client, name=["DEPUTY", "MANAGER"]
            )
            failed.remove(service_id)
        except (httpx.ConnectError, httpx.ConnectTimeout):
            pass

    # For each service, get it's managers. Run this in paralell batches of 100.
    while failed:
        async with asyncio.TaskGroup() as tg:
            for service_id in failed[0:100]:
                tg.create_task(get_service_roles(service_id))
            # Sleep to avoid overloading the portal and to avoid race conditions.
            await asyncio.sleep(1)

    # Combine all the data into a pretty dictionary.
    result = []
    for service in services:
        roles = [
            {
                x.name: [
                    [z.email for z in all_users if z.username == y.user.username][0]
                    for y in x.accesses
                ]
            }
            for x in service_roles[service.id]
        ]
        result.append(
            {
                "service_id": service.id,
                "service_name": service.name,
                "service_category": service.category.name,
                "roles": roles,
            }
        )

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
