from .models import (
    Customer,
    EHRConnection,
)
from drf_api_logger.models import APILogsModel
from rest_framework import serializers


class APILogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APILogsModel
        fields = '__all__'


class EHRConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EHRConnection
        fields = '__all__'


class UpdateCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    connection = EHRConnectionSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for connection in data["connection"]:
            if connection["app_type"] != "system":
                connection.update(
                    customer_auth_url_prod=connection["customer_auth_url_prod"]
                    + data["uuid"]
                )
                connection.update(
                    customer_auth_url_test=connection["customer_auth_url_test"]
                    + data["uuid"]
                )
        return data


# class PatientSerializer(serializers.ModelSerializer):
#     customer = CustomerSerializer(read_only=True)

#     class Meta:
#         model = Patient
#         fields = "__all__"


# class ProviderSerializer(serializers.ModelSerializer):
#     customer = CustomerSerializer(read_only=True)

#     class Meta:
#         model = Provider
#         fields = "__all__"
