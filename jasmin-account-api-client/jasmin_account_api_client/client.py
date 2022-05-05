"""Modified client which provides oauth2 authentication."""
import ssl
from typing import Dict, Union

import attr
import oauthlib.oauth2
import requests.auth
import requests_oauthlib


@attr.s(auto_attribs=True)
class Client:
    """A class for keeping track of data related to the API"""

    base_url: str
    cookies: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    headers: Dict[str, str] = attr.ib(factory=dict, kw_only=True)
    timeout: float = attr.ib(5.0, kw_only=True)
    verify_ssl: Union[str, bool, ssl.SSLContext] = attr.ib(True, kw_only=True)

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def with_headers(self, headers: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional headers"""
        return attr.evolve(self, headers={**self.headers, **headers})

    def get_cookies(self) -> Dict[str, str]:
        return {**self.cookies}

    def with_cookies(self, cookies: Dict[str, str]) -> "Client":
        """Get a new client matching this one with additional cookies"""
        return attr.evolve(self, cookies={**self.cookies, **cookies})

    def get_timeout(self) -> float:
        return self.timeout

    def with_timeout(self, timeout: float) -> "Client":
        """Get a new client matching this one with a new timeout (in seconds)"""
        return attr.evolve(self, timeout=timeout)


@attr.s(auto_attribs=True)
class AuthenticatedClient(Client):
    """A Client which has been authenticated for use on secured endpoints"""

    # token: str

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in authenticated endpoints"""
        return {
            "Authorization": f"Bearer {self.token_response['access_token']}",
            **self.headers,
        }

    def client_credentials_flow(
        self,
        client_id: str,
        client_secret: str,
        scopes: list[str],
    ) -> None:
        """Get a token using a client_credentials flow."""
        oauth = requests_oauthlib.OAuth2Session(
            client=oauthlib.oauth2.BackendApplicationClient(client_id),
            scope=scopes,
        )
        self.token_response = oauth.fetch_token(
            token_url=f"{self.base_url}/oauth/token/",
            auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
            scope=" ".join(scopes),
        )