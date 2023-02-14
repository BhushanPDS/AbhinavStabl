from core.models import Customer, Provider
from core.tasks import epic_provider_token
from ehr.workflows.clinical_summary import PatientQuery
from ehr.workflows.provider import ProviderQuery
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers
from drf_spectacular.utils import inline_serializer, extend_schema

from .utils import get_connection
from django.http.response import JsonResponse
import requests
from requests.auth import HTTPBasicAuth


@extend_schema(
    request=inline_serializer(
        name="Patient Query Demographics",
        fields={
            "Source_json": serializers.CharField(),
        }
    )
)
@api_view(["POST"])
def clinical_summary_patient_query_demographics(request):

    event = ["demographics"]
    request_body = request.data
    customer_id, ehr_connection_id, ehr_name, name = get_connection(
        request_body)
    if isinstance(customer_id, list):
        return Response(
            {"error": customer_id[1]}, status=status.HTTP_400_BAD_REQUEST
        )
    if customer_id is None or ehr_connection_id is None:
        return Response(
            {"error": "Customer not found or no connection associated with this customer"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if ehr_connection_id != "Source name must be CustomerID":
        patient_query = PatientQuery(
            request_body, ehr_connection_id, customer_id, ehr_name, name=name
        )
        ehr_response = patient_query.patient_query(event)

        return ehr_response

    return Response(
        {"error": ehr_connection_id}, status=status.HTTP_400_BAD_REQUEST
    )


@extend_schema(
    request=inline_serializer(
        name="Patient Query Insurances",
        fields={
            "Source_json": serializers.CharField(),
        }
    )
)
@api_view(["POST"])
def clinical_summary_patient_query_insurances(request):

    event = ["insurances"]
    request_body = request.data
    customer_id, ehr_connection_id, ehr_name, name = get_connection(
        request_body)
    if isinstance(customer_id, list):
        return Response(
            {"error": customer_id[1]}, status=status.HTTP_400_BAD_REQUEST
        )
    if customer_id is None or ehr_connection_id is None:
        return Response(
            {"error": "Customer not found or no connection associated with this customer"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if ehr_connection_id != "Source name must be CustomerID":
        patient_query = PatientQuery(
            request_body, ehr_connection_id, customer_id, ehr_name, name=name
        )
        ehr_response = patient_query.patient_query(event)

        return ehr_response

    return Response(
        {"error": ehr_connection_id}, status=status.HTTP_400_BAD_REQUEST
    )


@extend_schema(
    request=inline_serializer(
        name="Patient Query Allergies",
        fields={
            "Source_json": serializers.CharField(),
        }
    )
)
@api_view(["POST"])
def clinical_summary_patient_query_allergies(request):

    event = ["allergies"]
    request_body = request.data
    customer_id, ehr_connection_id, ehr_name, name = get_connection(
        request_body)
    if isinstance(customer_id, list):
        return Response(
            {"error": customer_id[1]}, status=status.HTTP_400_BAD_REQUEST
        )
    if customer_id is None or ehr_connection_id is None:
        return Response(
            {"error": "Customer not found or no connection associated with this customer"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if ehr_connection_id != "Source name must be CustomerID":
        patient_query = PatientQuery(
            request_body, ehr_connection_id, customer_id, ehr_name, name=name
        )
        ehr_response = patient_query.patient_query(event)

        return ehr_response

    return Response(
        {"error": ehr_connection_id}, status=status.HTTP_400_BAD_REQUEST
    )


@extend_schema(
    request=inline_serializer(
        name="Patient Query Medications",
        fields={
            "Source_json": serializers.CharField(),
        }
    )
)
@api_view(["POST"])
def clinical_summary_patient_query_medications(request):

    event = ["medications"]
    request_body = request.data
    customer_id, ehr_connection_id, ehr_name, name = get_connection(
        request_body)
    if isinstance(customer_id, list):
        return Response(
            {"error": customer_id[1]}, status=status.HTTP_400_BAD_REQUEST
        )
    if customer_id is None or ehr_connection_id is None:
        return Response(
            {"error": "Customer not found or no connection associated with this customer"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if ehr_connection_id != "Source name must be CustomerID":
        patient_query = PatientQuery(
            request_body, ehr_connection_id, customer_id, ehr_name, name=name
        )
        ehr_response = patient_query.patient_query(event)

        return ehr_response

    return Response(
        {"error": ehr_connection_id}, status=status.HTTP_400_BAD_REQUEST
    )


@extend_schema(
    request=inline_serializer(
        name="Patient Query Medications",
        fields={
            "Source_json": serializers.CharField(),
        }
    )
)
@api_view(["POST"])
def clinical_summary_patient_query_procedure(request):

    event = ["procedure"]
    request_body = request.data
    customer_id, ehr_connection_id, ehr_name, name = get_connection(
        request_body)
    if isinstance(customer_id, list):
        return Response(
            {"error": customer_id[1]}, status=status.HTTP_400_BAD_REQUEST
        )
    if customer_id is None or ehr_connection_id is None:
        return Response(
            {"error": "Customer not found or no connection associated with this customer"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if ehr_connection_id != "Source name must be CustomerID":
        patient_query = PatientQuery(
            request_body, ehr_connection_id, customer_id, ehr_name, name=name
        )
        ehr_response = patient_query.patient_query(event)

        return ehr_response

    return Response(
        {"error": ehr_connection_id}, status=status.HTTP_400_BAD_REQUEST
    )


@extend_schema(
    request=inline_serializer(
        name="Provider Query Demographics",
        fields={
            "Source_json": serializers.CharField(),
        }
    )
)
@api_view(["POST"])
def provider_query_demographics(request):

    request_body = request.data
    customer_id, ehr_connection_id, ehr_name, name = get_connection(
        request_body)
    if isinstance(customer_id, list):
        return Response(
            {"error": customer_id[1]}, status=status.HTTP_400_BAD_REQUEST
        )
    if customer_id is None or ehr_connection_id is None:
        return Response(
            {"error": "Customer not found or no connection associated with this customer"},
            status=status.HTTP_404_NOT_FOUND,
        )

    if ehr_connection_id != "Source name must be CustomerID":
        patient_query = ProviderQuery(
            request_body, ehr_connection_id, customer_id, ehr_name, name=name
        )
        ehr_response = patient_query.provider_query()

        return ehr_response

    return Response(
        {"error": ehr_connection_id}, status=status.HTTP_400_BAD_REQUEST
    )


def redirect_uri(request):
    code = request.GET.get("code")
    id = request.GET.get("state")
    provider_obj = Provider.objects.get(uuid=id)

    customer_obj = provider_obj.customer
    epic_connection = customer_obj.connection.get(
        ehr_name="epic", app_type="provider")

    if provider_obj:

        payload = {
            "grant_type": epic_connection.grant_type,
            "code": code,
            "client_id": epic_connection.client_id,
            "redirect_uri": epic_connection.redirect_uri,
            }

        response = requests.request("POST", auth=HTTPBasicAuth(epic_connection.client_id, epic_connection.client_secret), url=epic_connection.auth_url_test, data=payload )
        provider_obj.access_token = response.json().get("access_token")
        provider_obj.refresh_token = response.json().get("refresh_token")
        provider_obj.save()
    return JsonResponse(response.json())
