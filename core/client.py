from abc import ABC


class ClientBase(ABC):
    """
    A client to call API's for GET, POST, PUT, PATCH, DELETE methods for given URL & Payload.
    """

    global ehr_data
    ehr_data = []

    def get_ehr_data(self, ehr_element):
        ehr_data.append(ehr_element)

    def __init__(self):
        self.url = None
        self.is_test_environment = True
        self.base_url = None
        self.auth_url = None
        self.auth_token = None
        self.auth_token_type = None
        self.auth_token_expires_in = None
        self.is_token_expired = False
        self.scope = None
        self.practice_id = None
        self.auth_url = None
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self.payload = {}

    def build_url(self):
        """
        Build URL for request.
        """
        raise NotImplementedError

    def build_headers(self):
        """
        Build headers for request.
        """
        raise NotImplementedError

    def build_payload(self):
        """
        Build payload for request.
        """
        raise NotImplementedError

    def authenticate(self):
        """
        Authenticate user with given username and password.
        """
        raise NotImplementedError

    def refresh_token(self):
        """
        Refresh token.
        """
        raise NotImplementedError

    def persist_token(self):
        """
        Persist token to file.
        """
        raise NotImplementedError

    def read_token(self):
        """
        Read stored token from file.
        """
        raise NotImplementedError

    def get(self):
        """
        GET method to get data from given URL.
        """
        raise NotImplementedError

    def post(self):
        """
        POST method to post data to given URL.
        """
        raise NotImplementedError

    def put(self):
        """
        PUT method to put data to given URL.
        """
        raise NotImplementedError

    def patch(self):
        """
        PATCH method to patch data to given URL.
        """
        raise NotImplementedError

    def delete(self):
        """
        DELETE method to delete data to given URL.
        """
        raise NotImplementedError


class RequestBase(ABC):
    def buildJSON(self):
        """
        Build JSON for given action, appname, username, password, token, and data.
        """
        raise NotImplementedError


class ResponseBase(ABC):
    pass
