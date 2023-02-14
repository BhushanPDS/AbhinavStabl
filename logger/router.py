
from logger.views import APILogsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', APILogsViewSet, basename='apilogger')