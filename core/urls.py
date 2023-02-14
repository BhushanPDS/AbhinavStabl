# from django.urls import path, include

# urlpatterns = [
#     path("api/", include("core.api_router")),
# ]
from django.urls import path

from core import views

urlpatterns = [
    path(
        "api/connections",
        views.EHRConectionViewSet.as_view(
            {
                "post": "create",
            }
        ),
    ),
    path(
        "api/connections/<uuid:cid>",
        views.DetailConnectionViewSet.as_view(),
    ),
    path(
        "api/customers",
        views.CustomerViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "api/customers/<uuid:cid>",
        views.DetailCustomerViewSet.as_view(),
    ),

]
