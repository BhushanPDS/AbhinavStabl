from drf_api_logger.models import APILogsModel
from rest_framework import serializers

class APILogSerializer(serializers.ModelSerializer):
    class Meta:
        model = APILogsModel
        fields = '__all__'