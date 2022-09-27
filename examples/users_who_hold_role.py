"""Retrieve list of usernames who hold access to a service."""

import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.services as jservices

SERVICE_ID = 182
ROLE_NAME = "USER"

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=["jasmin.services.serviceroles.all:read"],
)

# Get all the roles which are active in a service.
service_roles = jservices.services_roles_retrieve.sync(SERVICE_ID, client=client)
# If there are no roles service_roles will be None.
if service_roles:
    # Select role by name.
    role = [x for x in service_roles if x.name == ROLE_NAME][0]
    # Transform list of accesses to retrieve username only.
    usernames = [x.user.username for x in role.accesses]
    print(usernames)
