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
    ],
)

# Get a single category by name.
single_category = jcats.categories_retrieve.sync("login_services", client=client)
if single_category:
    single_service = [x for x in single_category.services if x.name == "jasmin-login"][0]
    print(single_service)
