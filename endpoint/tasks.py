import requests
from celery import shared_task
from core.models import EHRConnection
from datetime import datetime, timedelta


@shared_task(bind=True)
def refresh_token(self):

    is_test_environment = True
    payload = {}
    current_datetime = datetime.now()
    time_difference = current_datetime - timedelta(minutes=8)
    ehrconnections = EHRConnection.objects.filter(
        updated_at__lte=time_difference)

    for ehr_connection in ehrconnections:

        client_id = ehr_connection.client_id
        client_secret = ehr_connection.client_secret
        auth_url = ehr_connection.auth_url_test if is_test_environment else ehr_connection.auth_url_prod

        payload["grant_type"] = ehr_connection.grant_type
        payload["scope"] = ehr_connection.scope

        response = requests.request("POST",
                                    auth_url,
                                    data=payload,
                                    auth=(client_id, client_secret)
                                    )

        access_token = response.json()["access_token"]
        ehr_connection.access_token = access_token
        ehr_connection.save()

    return "Access Token Renewed"
