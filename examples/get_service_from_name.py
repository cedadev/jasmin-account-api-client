"""Quick demonstration of jasmin_accounts api."""

import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.categories as jcats

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=[
        "jasmin.services.categories.all:read",  # categories_retrieve and categories_list
        "jasmin.services.services.all:read",  # categories_services_retrieve
    ],
)

# Get a single category by name.
single_service = jcats.categories_services_retrieve.sync(
    category_name="login_services", name="jasmin-login", client=client
)
print(single_service)
