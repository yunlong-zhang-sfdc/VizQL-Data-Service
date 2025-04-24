class HTTPHeaders:
    """
    Class for maintaining HTTP headers
    """
    def __init__(self, headers=None):
        self._headers = headers or {}

    def add_header(self, key, value):
        """
        Add a header to the HTTP headers
        :param str key: header key
        :param str value: header value
        :return: None
        """
        self._headers[key] = value

    def remove_header(self, key):
        """
        Remove a header from the HTTP headers
        :param str key: header key
        :return: None
        """
        if key in self._headers:
            del self._headers[key]

    def get_header(self, key):
        """
        Get a header from the HTTP headers
        :param str key: header key
        :return: the header value for the header key
        :rtype: str
        """
        return  self._headers.get(key, None)

    def set_accept_json(self):
        """
        Set the accept json header
        """
        self.add_header("User-Agent","application/json")

    def set_tableau_auth(self, auth_token):
        """
        Set the X-Auth-token in HTTP headers
        This is obtained upon user login
        :return: None
        """
        self.add_header("X-Tableau-Auth", auth_token)

    def set_user_agent(self, user_agent):
        """
        Set the user-agent in HTTP headers
        :param user_agent:
        :return: None
        """
        self.add_header("User-Agent", user_agent)

    def to_dict(self):
        """
        :return: A dictionary of the HTTP headers
        :rtype: dict
        """
        return self._headers.copy()

def default_headers():
    headers = HTTPHeaders()
    headers.add_header("Content-Type","application/json")
    headers.set_accept_json()
    headers.set_user_agent('python-sdk-client')
    return headers