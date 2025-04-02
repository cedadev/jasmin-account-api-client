"""Quick demonstration of jasmin_accounts api."""

import asyncio
import json
import os

import httpx
import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.users as jusers


async def main():
    # Increase the connection pool timeout.
    # We are going to be making many http requests.
    # httpx has a pool which allows 20 to happen concurrently.
    # We are going to make more requests, but don't mind waiting longer for space in the pool.
    # Also kubernetes sometimes has a bug where http connections take a long time to make.
    # Reduce the connect timout, so that if this happens we fail fast and try again.
    # Read and write timeouts set to values which seem sensible.
    timeout = httpx.Timeout(connect=2, read=5, write=2, pool=10)

    # Create a client and auth to the portal.
    client = jclient.AuthenticatedClient(
        "https://accounts.jasmin.ac.uk", timeout=timeout
    )
    client.client_credentials_flow(
        client_id=os.environ["JASMIN_CLIENT_ID"],
        client_secret=os.environ["JASMIN_CLIENT_SECRET"],
        scopes=[
            "jasmin.auth.users.all:read",  # needed to get big list of users.
            "jasmin.services.userservices.all:read",  # needed to get user services.
        ],
    )

    # Get the list of all users.
    all_users = jusers.users_list.sync(client=client)

    # Output dictionary.
    results = {}
    # When a request for a user succeeds, we will remove it from 'failed' until they are all done.
    failed = [x.username for x in all_users]

    async def get_service_count(username):
        """Get the user count for a single user and put it directly into the results dict."""
        try:
            services = await jusers.users_services_list.asyncio(username, client=client)
            # Mark this user as completed successfully.
            failed.remove(username)
            if services:
                jasmin_login = [x for x in services if x.name == "jasmin-login"]
                if jasmin_login:
                    services = [
                        x for x in services if x.category.name == "group_workspaces"
                    ]
                    if len(services) < 1:
                        results[username] = len(services)
        # If the connection failed, don't worry.
        except (
            httpx.ConnectError,
            httpx.ConnectTimeout,
            httpx.ReadTimeout,
            httpx.PoolTimeout,
        ):
            pass

    # Make requests continuiously until the failed list is empty.
    while failed:
        print(len(failed))
        # Spawn tasks in groups of 500.
        async with asyncio.TaskGroup() as tg:
            for username in failed[0:500]:
                tg.create_task(get_service_count(username))
            # Sleep to avoid overloading the portal and to avoid race conditions.
            await asyncio.sleep(1)

    # All done? Write the results to yaml.
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
