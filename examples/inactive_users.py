"""Quick demonstration of jasmin_accounts api."""
import asyncio
import datetime as dt
import os
import zoneinfo

import httpx
import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.users as jusers


async def main():
    client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk", timeout=30)
    client.client_credentials_flow(
        client_id=os.environ["JASMIN_CLIENT_ID"],
        client_secret=os.environ["JASMIN_CLIENT_SECRET"],
        scopes=[
            "jasmin.auth.users.all:read",  # users_retrieve and users_list
        ],
    )

    now = dt.datetime.now(tz=zoneinfo.ZoneInfo("Europe/London"))

    inactive_users = await jusers.users_list.asyncio(client=client, is_active=False)
    inactive_users = [x for x in inactive_users if x.user_type == "STANDARD"]

    print(f"There are {len(inactive_users)} inactive users.")

    inactive_user_records = []

    failed = [x.username for x in inactive_users]

    async def get_user_details(username):
        try:
            inactive_user_records.append(
                await jusers.users_retrieve.asyncio(username, client=client)
            )
            failed.remove(username)
        except (httpx.ConnectError, httpx.ConnectTimeout):
            pass

    while failed:
        async with asyncio.TaskGroup() as tg:
            for user in failed[0:100]:
                tg.create_task(get_user_details(user))
            await asyncio.sleep(1)

    inactive_users_with_time = [
        x for x in inactive_user_records if x.deactivated_at is not None
    ]

    print(f"{len(inactive_users_with_time)} inactive users have a deactivated_at time.")

    for y in range(10):
        year = [
            x
            for x in inactive_users_with_time
            if x.deactivated_at < now - dt.timedelta(days=y * 365)
        ]
        print(f"{len(year)} were deactivated over {y} years ago.")


if __name__ == "__main__":
    asyncio.run(main())
