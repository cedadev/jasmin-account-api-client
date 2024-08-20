"""Number of users who have an active jasmin_accounts_portal account.."""

import collections
import json
import os

import jasmin_account_api_client as jclient
import jasmin_account_api_client.api.users as jusers
import pandas as pd

client = jclient.AuthenticatedClient("https://accounts.jasmin.ac.uk")
client.client_credentials_flow(
    client_id=os.environ["JASMIN_CLIENT_ID"],
    client_secret=os.environ["JASMIN_CLIENT_SECRET"],
    scopes=[
        "jasmin.auth.users.all:read",  # users_retrieve and users_list
    ],
)

# Institution data is not yet available from the api. Load it from a file.
inst = pd.read_json("./jasmin_accounts_institutions.json")
inst = pd.json_normalize(inst["fields"]).set_index(inst["pk"])

# Make the api result into a dict for pandas, and unwrap the institution_id.
active_users = (
    x.to_dict() | {"institution_id": x.institution.id}
    for x in jusers.users_list.sync(client=client, is_active=False)
)

users = pd.DataFrame.from_dict(active_users)
df = pd.DataFrame()
df["counts_per_inst"] = users["institution_id"].value_counts()
