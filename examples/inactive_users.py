"""Quick demonstration of jasmin_accounts api."""
import asyncio
import datetime as dt
import os
import zoneinfo

import httpx
import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.users as jusers


async def main():
    # Auth to the portal.
    client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk", timeout=30)
    client.client_credentials_flow(
        client_id=os.environ["JASMIN_CLIENT_ID"],
        client_secret=os.environ["JASMIN_CLIENT_SECRET"],
        scopes=[
            "jasmin.auth.users.all:read",  # users_retrieve and users_list
        ],
    )

    # Get the time for future use. Needs to have a timezone otherwise comparisons break.
    now = dt.datetime.now(tz=zoneinfo.ZoneInfo("Europe/London"))

    # Get a list of all inactive users.
    inactive_users = await jusers.users_list.asyncio(client=client, is_active=False)
    # Filter out training accounts, shared accounts, service accounts.
    inactive_users = [x for x in inactive_users if x.user_type == "STANDARD"]

    print(f"There are {len(inactive_users)} inactive users.")

    # List to put users more detailed data into.
    # We have to call the details endpoint for each user
    # Because this information isn't available from the list view.
    inactive_user_records = []

    # Get a list off all the inactive usernames. This will be removed when
    # we sucessfully get data for each one.
    failed = [x.username for x in inactive_users]

    async def get_user_details(username):
        """Get a user record by username, and append it to the big list.

        Once we've got it, remove the username from the queue.
        """
        try:
            inactive_user_records.append(
                await jusers.users_retrieve.asyncio(username, client=client)
            )
            failed.remove(username)
        except (httpx.ConnectError, httpx.ConnectTimeout):
            pass

    # In batches of 100, create async tasks to get the user record.
    # Keep doing it until they are all done.
    while failed:
        async with asyncio.TaskGroup() as tg:
            for user in failed[0:100]:
                tg.create_task(get_user_details(user))
            # Sleep to avoid overloading the portal and to avoid race conditions.
            await asyncio.sleep(1)

    # Now filter the result to onlly users which have a deactivate_at time.
    inactive_users_with_time = [
        x for x in inactive_user_records if x.deactivated_at is not None
    ]

    print(f"{len(inactive_users_with_time)} inactive users have a deactivated_at time.")

    # Compare the time to today for the past 10 years.
    for y in range(10):
        year = [
            x
            for x in inactive_users_with_time
            if x.deactivated_at < now - dt.timedelta(days=y * 365)
        ]
        print(f"{len(year)} were deactivated over {y} years ago.")


if __name__ == "__main__":
    asyncio.run(main())
