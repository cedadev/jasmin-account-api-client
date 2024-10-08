"""Retrieve list of usernames who hold access to a service."""

import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.services as jservices

SERVICE_ID = 148
ROLE_NAME = "USER"

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=["jasmin.services.serviceroles.all:read"],
)

# Get all the roles which are active in a service.
service_roles = jservices.services_roles_list.sync(
    SERVICE_ID, name=ROLE_NAME, client=client
)
# If there are no roles service_roles will be None.
if service_roles:
    # Transform list of accesses to retrieve username only.
    usernames = [x.user.username for x in service_roles[0].accesses]
    print(usernames)
    print(len(usernames))
