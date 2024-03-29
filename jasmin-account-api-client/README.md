# jasmin-account-api-client
A client library for accessing JASMIN Account API

## Usage
First, create a client:

```python
from jasmin_account_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com")
client.client_credentials_flow(client_id="your-client-id", client_secret="your-client-secret", scopes=["scope1", "scope2"])
```

Now call your endpoint and use your models:

```python
from jasmin_account_api_client.models import MyDataModel
from jasmin_account_api_client.api import get_my_data_model
from jasmin_account_api_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from jasmin_account_api_client.models import MyDataModel
from jasmin_account_api_client.api import get_my_data_model
from jasmin_account_api_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `jasmin_account_api_client.api.default`
