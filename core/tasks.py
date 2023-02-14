from urllib.request import HTTPBasicAuthHandler
import uuid
from datetime import datetime, timedelta

import jwt
import requests
from celery import shared_task

from core.models import EHRConnection


@shared_task
def refresh_epic_backend_system_token():

    is_test_environment = True
    payload = {}
    current_datetime = datetime.now()
    time_difference = current_datetime - timedelta(minutes=1)

    ehrconnections = EHRConnection.objects.filter(updated_at__lte=time_difference
                                                  )

    for ehr_connection in ehrconnections:
        auth_url = (
            ehr_connection.auth_url_test
            if is_test_environment
            else ehr_connection.auth_url_prod
        )

        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        uuid_str = str(uuid.uuid4())
        date_and_time = datetime.now()
        add_time = timedelta(minutes=2)
        date_and_time += add_time
        payload = {
            "iss": ehr_connection.client_id,
            "sub": ehr_connection.client_id,
            "aud": auth_url,
            "jti": uuid_str,
            "exp": date_and_time.strftime("%s"),
        }
        private_key = ehr_connection.private_key
        token = jwt.encode(
            payload=payload, algorithm="RS384", key=private_key)

        data = {
            "grant_type": ehr_connection.grant_type,
            "scope": ehr_connection.scope,
            "client_assertion_type": "urn:ietf:params:oauth:client-assertion-type:jwt-bearer",
            "client_assertion": token
        }
        payload["client_assertion"] = token

        response = requests.request(
            "POST", auth_url, headers=headers, data=data
        )
        access_token = response.json()["access_token"]
        ehr_connection.access_token = access_token
        ehr_connection.save()

    return "Epic Backend System Token Renewed"


@shared_task(bind=True)
def epic_provider_token(provider, connection):

    payload = {
        "grant_type": connection.grant_type,
        "code": provider.authorize_code,
        "client_id": connection.client_id,
        # "scope": connection.scope,
        "redirect_uri": connection.redirect_uri,
    }

    response = requests.request("POST", auth=HTTPBasicAuthHandler(
        connection.client_id, connection.client_secret), url=connection.auth_url_test, data=payload, )
    provider.access_token = response.json().get("access_token")
    provider.refresh_token = response.json().get("refresh_token")
    provider.save()
    return response
