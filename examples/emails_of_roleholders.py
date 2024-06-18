"""Retrieve list of emails of people who hold access to a service."""

import json
import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.categories as jcats
import jasmin_account_api_client.api.services as jservices
import jasmin_account_api_client.api.users as jusers

CATEGORY_NAME = "group_workspaces"
SERVICE_NAME = "name"

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
service_roles = jcats.categories_services_roles_list.sync(
    category_name=CATEGORY_NAME, service_name=SERVICE_NAME, client=client
)

# Get their usernames.
accesses = []
for role in service_roles:
    accesses += role.accesses
emails = [x.user.email for x in accesses]

print(json.dumps(list(emails), indent=2, sort_keys=True))
