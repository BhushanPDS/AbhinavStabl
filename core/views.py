import urllib
from .serializers import (
    CustomerSerializer,
    EHRConnectionSerializer,

    UpdateCustomerSerializer,

)
from .models import (
    Customer,
    EHRConnection,
    Patient,
    Provider,
)
from rest_framework.response import Response
from rest_framework import generics, mixins, status, viewsets
from django.shortcuts import get_object_or_404
from core.serializers import APILogSerializer
from drf_api_logger.models import APILogsModel
from rest_framework import viewsets

# Create your views here.


class APILogsViewSet(viewsets.ModelViewSet):
    queryset = APILogsModel.objects.all()
    serializer_class = APILogSerializer


class EHRConectionViewSet(viewsets.ModelViewSet):
    queryset = EHRConnection.objects.all()
    serializer_class = EHRConnectionSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DetailConnectionViewSet(
    generics.RetrieveUpdateDestroyAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = EHRConnection.objects.all()
    serializer_class = EHRConnectionSerializer

    def retrieve(self, *args, **kwargs):
        customer = get_object_or_404(EHRConnection, uuid=kwargs["cid"])
        serializer = self.get_serializer(customer)
        return Response(serializer.data)

    def update(self, *args, **kwargs):
        customer = get_object_or_404(EHRConnection, uuid=kwargs["cid"])
        serializer = self.serializer_class(
            data=self.request.data, instance=customer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, *args, **kwargs):
        customer = get_object_or_404(EHRConnection, uuid=kwargs["cid"])
        customer.delete()
        return Response(
            {"detail": "Item Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class DetailCustomerViewSet(
    generics.RetrieveUpdateDestroyAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Customer.objects.all()
    serializer_class = UpdateCustomerSerializer

    def retrieve(self, *args, **kwargs):
        customer = get_object_or_404(Customer, uuid=kwargs["cid"])
        serializer = self.get_serializer(customer)
        return Response(serializer.data)

    def update(self, *args, **kwargs):
        customer = get_object_or_404(Customer, uuid=kwargs["cid"])

        serializer = self.serializer_class(
            data=self.request.data, instance=customer)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, *args, **kwargs):
        customer = get_object_or_404(Customer, uuid=kwargs["cid"])
        customer.delete()
        return Response(
            {"detail": "Item Deleted Successfully"}, status=status.HTTP_204_NO_CONTENT
        )



# class PatientViewSet(viewsets.ModelViewSet):

#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer
#     lookup_field = "cid"

#     def get_queryset(self, *args, **kwargs):

#         webhooks = Patient.objects.filter(customer=self.kwargs["cid"])
#         return webhooks


# class ProviderViewSet(viewsets.ModelViewSet):

#     queryset = Provider.objects.all()
#     serializer_class = ProviderSerializer
#     lookup_field = "cid"

#     def get_queryset(self, *args, **kwargs):

#         webhooks = Provider.objects.filter(customer=self.kwargs["cid"])
#         return webhooks


# class ServerStatus(View):
#     authentication_classes = []  # disables authentication
#     permission_classes = []  # disables permission

#     def get(self, request, format=None):
#         server_health = {
#             "status": "active",
#             "version": "1",
#             "releaseId": "1.0.0",
#             "notes": [],
#             "output": None,
#             "description": "health of ma-engine service",
#             "links": {"API Docs": "https://docs.medarch.com"},
#         }
#         return JsonResponse(server_health)


# def epic_redirectUrl(request):
#     code = request.GET.get("code")
#     state = request.GET.get("state").split(",")
#     customer_id = state[1]
#     app_type = state[0]
#     customer = Customer.objects.get(uuid=customer_id)

#     model_name = Provider if app_type == "provider" else Patient

#     epic_connection = customer.connection.get(ehr_name="epic", app_type=app_type)

#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }

#     payload = {
#         "grant_type": epic_connection.grant_type,
#         "client_id": epic_connection.client_id,
#         "code": code,
#         "redirect_uri": epic_connection.redirect_uri,
#     }

#     response = requests.request(
#         "POST",
#         url=epic_connection.auth_url_test,
#         headers=headers,
#         data=payload,
#         auth=HTTPBasicAuth(epic_connection.client_id, epic_connection.client_secret),
#     )

#     jwt_decode = jwt.decode(response.json().get("access_token"), options={"verify_signature": False})
#     provider_or_patient_id = jwt_decode.get("sub")

#     obj = model_name.objects.filter(ehr_id=provider_or_patient_id).first()
#     if  obj is None:
#         obj = model_name(customer=customer, authorize_code=code)
#         obj.save()
#     obj.access_token = response.json().get("access_token")
#     obj.refresh_token = response.json().get("refresh_token")
#     obj.refresh_token_last_updated_at = timezone.now()
#     obj.save()

#     if app_type == "provider":
#         provider_query = EpicPractitioner(obj.uuid, epic_connection.uuid)
#         provider_query.authenticate()
#         epic_response = provider_query.get_specific_practitioner(provider_or_patient_id)
#         obj.firstname = " ".join(epic_response.get("name")[0].get("given"))
#         obj.lastname = epic_response.get("name")[0].get("family")
#         obj.status = epic_response.get("active")
#         obj.ehr_id = epic_response.get("id")
#         obj.save()
#     else:
#         patient_query = EpicPatient(obj.uuid, epic_connection.uuid)
#         patient_query.authenticate()
#         epic_response = patient_query.get_specific_patient(provider_or_patient_id)

#     redirect_url = (
#         epic_connection.org_redirect_uri + "?" + urllib.parse.urlencode(epic_response)
#     )

#     return redirect(redirect_url)

