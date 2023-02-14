from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from core.views import APILogsViewSet

if settings.DEBUG:
    router = DefaultRouter(trailing_slash=False)
else:
    router = SimpleRouter(trailing_slash=False)

router.register("logs", APILogsViewSet, basename="apilogger")


app_name = "core"
urlpatterns = router.urls
