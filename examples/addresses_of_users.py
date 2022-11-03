"""Quick demonstration of jasmin_accounts api."""
import json
import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.users as jusers

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=[
        "jasmin.auth.users.all:read",  # users_retrieve and users_list
    ],
)

all_users = jusers.users_list.sync(client=client)

if all_users:
    with open("./list_of_usernames.json", "r") as f:
        usernames = json.load(f)

    emails = [x.email for x in all_users if x.username in usernames]

    print("\n".join(emails))
