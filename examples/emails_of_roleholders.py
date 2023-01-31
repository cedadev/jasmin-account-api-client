"""Retrieve list of emails of people who hold access to a service."""

import json
import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.services as jservices
import jasmin_account_api_client.api.users as jusers

SERVICE_ID = 92

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=[
        "jasmin.services.serviceroles.all:read",
        "jasmin.auth.users.all:read",
    ],
)

# Get all the roles which are active in a service.
service_roles = jservices.services_roles_retrieve.sync(SERVICE_ID, client=client)

# Get their usernames.
accesses = []
for role in service_roles:
    accesses += role.accesses
usernames = [x.user.username for x in accesses]

# Get all the users
all_users = jusers.users_list.sync(client=client)
# Filter by service.
emails = {x.email for x in all_users if (x.username in usernames) and x.email}

print(json.dumps(list(emails), indent=2, sort_keys=True))
