"""
HTTP Headers Management for API Requests.

This module provides a class for managing HTTP headers used in API requests.
It includes methods for adding, removing, and retrieving headers, as well as
convenience methods for setting common headers like authentication tokens
and content types.

Key Features:
- Header management (add, remove, get)
- Authentication token handling
- Content type and user agent configuration
- Default header generation
"""


class HTTPHeaders:

    def __init__(self, headers=None):
        self._headers = headers or {}

    def add_header(self, key, value):
        self._headers[key] = value

    def remove_header(self, key):
        if key in self._headers:
            del self._headers[key]

    def get_header(self, key):
        return self._headers.get(key, None)

    def set_accept_json(self):
        self.add_header("User-Agent", "application/json")

    def set_tableau_auth(self, auth_token):
        self.add_header("X-Tableau-Auth", auth_token)

    def set_user_agent(self, user_agent):
        self.add_header("User-Agent", user_agent)

    def to_dict(self):
        return self._headers.copy()


def default_headers():
    headers = HTTPHeaders()
    headers.add_header("Content-Type", "application/json")
    headers.set_accept_json()
    headers.set_user_agent("python-sdk-client")
    return headers
