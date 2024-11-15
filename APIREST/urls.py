from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"sala", views.RoomViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("docs/", include_docs_urls(title="Api_sala")),
]