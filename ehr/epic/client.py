import uuid
from datetime import datetime, timedelta

import jwt
import requests
from core.client import ClientBase
from core.models import Customer, EHRConnection, Patient, Provider


class EpicFHIRClient(ClientBase):
    """
    A client to call API's for GET, POST, PUT, PATCH, DELETE methods for given URL & Payload.
    """

    def __init__(self, customer_id, connection_id):
        super().__init__()
        self.ehr = EHRConnection.objects.get(uuid=connection_id)

        try:
            self.customer = Customer.objects.get(uuid=customer_id)
        except Customer.DoesNotExist:
            if self.ehr.app_type == "provider":
                self.customer = Provider.objects.get(uuid=customer_id)
            else:
                self.customer = Patient.objects.get(uuid=customer_id)

        self.is_test_environment = True
        self.base_url = (
            self.ehr.base_url_test
            if self.is_test_environment
            else self.ehr.base_url_prod
        )
        self.auth_url = None
        self.auth_token = None
        self.auth_token_type = None
        self.auth_token_expires_in = None
        self.is_token_expired = False
        self.scope = None
        self.app_type = self.ehr.app_type
        self.headers = {}
        self.payload = {}
        self.auth_url = (
            self.ehr.auth_url_test
            if self.is_test_environment
            else self.ehr.auth_url_prod
        )
        self.epic_client_id = self.ehr.client_id
        self.epic_client_secret_key = self.ehr.client_secret
        self.epic_grant_type = self.ehr.grant_type
        self.epic_api_scope = self.ehr.scope
        self.redirect_url = self.ehr.redirect_uri

    def authenticate(self):
        """
        Get Auth Token from EPIC Health API.
        """
        try:
            """
            Comment this if condition in case of production environment.
            this condition is for testing purpose only.
            the idea is to override read_token function to fetch data from
            Database
            """
            if self.read_token():
                self.auth_token = self.read_token()
                self.headers["Authorization"] = "Bearer " + self.auth_token
                return 200

            self.headers["Content-Type"] = "application/x-www-form-urlencoded"
            self.payload["grant_type"] = self.epic_grant_type
            uuid_str = str(uuid.uuid4())
            date_and_time = datetime.now()
            add_time = timedelta(minutes=2)
            date_and_time += add_time

            payload = {
                "iss": self.epic_client_id,
                "sub": self.epic_client_id,
                "aud": self.auth_url,
                "jti": uuid_str,
                "exp": date_and_time.strftime("%s"),
            }
            private_key = self.ehr.private_key
            token = jwt.encode(
                payload=payload, algorithm="RS384", key=private_key)

            self.payload["scope"] = self.epic_api_scope
            self.payload[
                "client_assertion_type"
            ] = "urn:ietf:params:oauth:client-assertion-type:jwt-bearer"
            self.payload["client_assertion"] = token
            response = requests.request(
                "POST", self.auth_url, headers=self.headers, data=self.payload
            )
            self.auth_token_type = response.json()["token_type"]
            self.auth_token = response.json()["access_token"]
            self.auth_token_expires_in = response.json()["expires_in"]
            self.scope = response.json()["scope"]

            self.headers["Authorization"] = "Bearer " + self.auth_token
            self.persist_token()
            return response.status_code
        except Exception:
            return response.status_code

    def persist_token(self):
        """
        Persist token to database.
        """
        self.ehr.access_token = self.auth_token
        self.ehr.save()

    def read_token(self):
        """
        Read stored token from database.
        """

        if self.ehr.app_type in ("provider", "patient"):
            token = self.customer.access_token
            return token if token else False

        token = self.ehr.access_token
        return token if token else False

    def build_url(self, rawurl: str, **kwargs) -> str:
        url = self.base_url + rawurl.format(**kwargs)
        return url

    def get(self, url: str = "", params: list = None) -> str:
        """
        Get data from EPIC Health API.
        """

        try:
            self.headers["Accept"] = "application/json"
            self.headers["X-Requested-With"] = "XMLHttpRequest"
            response = requests.request(
                "GET", url, headers=self.headers, params=params)

            return response.json()
        except Exception:
            return response.status_code
