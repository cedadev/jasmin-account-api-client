"""Quick demonstration of jasmin_accounts api."""

import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.categories as jcats
import jasmin_account_api_client.api.services as jservices
import jasmin_account_api_client.api.users as jusers

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=[
        "jasmin.auth.users.all:read",  # users_retrieve and users_list
        "jasmin.services.userservices.all:read",  # users_services_retrieve
        "jasmin.services.serviceroles.all:read",  # services_roles_retrieve
        "jasmin.services.categories.all:read",  # categories_retrieve and categories_list
        "jasmin.services.services.all:read",  # services_retrieve and services_list
    ],
)

single_user = jusers.users_retrieve.sync("amanning", client=client)
all_users = jusers.users_list.sync(client=client)
user_services = jusers.users_services_retrieve.sync("amanning", client=client)

single_service = jservices.services_retrieve.sync(1, client=client)
all_services = jservices.services_list.sync(client=client)
service_users = jservices.services_roles_retrieve.sync(1, client=client)

single_category = jcats.categories_retrieve.sync("login-services", client=client)
all_categories = jcats.categories_list.sync(client=client)
