from django.urls import path,include

from logger.router import router
from . import views

urlpatterns = [
    path('log',views.APILogsViewSet.as_view({
        "get":"list"
    }),name='logs')
]