## Getting started

* Install the library using pip:
  * If you prefer https: `pip install 'jasmin_account_api_client @ git+https://github.com/cedadev/jasmin-account-api-client.git@main#egg=jasmin_account_api_client&subdirectory=jasmin-account-api-client'`
  * If you prefer ssh: `pip install 'jasmin_account_api_client @ git+ssh://git@github.com/cedadev/jasmin-account-api-client.git@main#egg=jasmin_account_api_client&subdirectory=jasmin-account-api-client'`
* Create an application with your required scopes on the jasmin accounts site and get the client_id and client_secret.
* Have a look in the examples folder to see how to use the endpoints.

## Rebuilding the client

* Everything inside the jasmin-account-api-client folder is managed by https://github.com/openapi-generators/openapi-python-client .
* When the API changes, update schema.yaml and run the `generate` make target.
* The only files which should be edited manually in the jasmin-account-api-client folder are project metadata: README.md, .gitignore, pyproject.toml and poetry.lock
