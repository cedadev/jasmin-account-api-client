"""Number of users who have an active jasmin_accounts_portal account.."""

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

active_users = jusers.users_list.sync(client=client, is_active=True)

print(len(active_users))
