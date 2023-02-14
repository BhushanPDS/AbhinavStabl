from django.contrib import admin

from .models import (
    Customer,
    EHRConnection,
    Patient,
    Provider,
)


@admin.register(EHRConnection)
class EHRConnectionAdmin(admin.ModelAdmin):

    search_fields = ["uuid", "ehr_name", "client_id"]

    fields = [
        "ehr_name",
        "client_id",
        "client_secret",
        "grant_type",
        "app_type",
        "scope",
        "audiance",
        "redirect_uri",
        "access_token",
        "customer_auth_url_test",
        "private_key",
        "tenant",
        
        
    ]

    list_display = ["uuid", "ehr_name", "app_type"]


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    def get_connections(self, object):
        return [connection for connection in object.connection.all()]

    search_fields = [
        "uuid",
        "name",
        "connection__connection_name",
        "email",
    ]

    list_display = ["uuid", "name", "get_connections", "email"]



@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):

    search_fields = [
        "uuid",
        "customer__uuid",
        "customer__name",
    ]
    list_display = ["uuid", "customer"]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    search_fields = [
        "uuid",
        "customer__uuid",
        "customer__name",
    ]
    list_display = ["uuid", "customer"]
