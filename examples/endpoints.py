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

# Retrieve a single user by username.
single_user = jusers.users_retrieve.sync("amanning", client=client)
# Retrieve all users. Can filter by institution service_user and active status. Can also search and change ordering.
all_users = jusers.users_list.sync(client=client, is_active=True, service_user=False)
# Get all services a given user belongs to.
user_services = jusers.users_services_retrieve.sync("amanning", client=client)

# Get all information about a single service, by service id..
single_service = jservices.services_retrieve.sync(1, client=client)
# Get all services. Can fileter by hidden state, category, and ceda_managed. Can also search and change ordering.
all_services = jservices.services_list.sync(
    client=client, hidden=False, ceda_managed=False
)
# Get all the roles which are active in a service, by service id.
service_users = jservices.services_roles_retrieve.sync(148, client=client)
service_users = [x for x in service_users if x.name == "USER"][0]
print(len(service_users.accesses))

# Get a single category by name.
single_category = jcats.categories_retrieve.sync("login-services", client=client)
# Get all categories. Can search and change ordering.
all_categories = jcats.categories_list.sync(client=client)
