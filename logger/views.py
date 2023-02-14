from logger.serializers import APILogSerializer
from drf_api_logger.models import APILogsModel
from drf_api_logger.admin import APILogsAdmin
from rest_framework import viewsets

# Create your views here.


class APILogsViewSet(viewsets.ModelViewSet):
    queryset = APILogsModel.objects.all()
    serializer_class = APILogSerializer
