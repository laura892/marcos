from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"libros", views.LibroViewSet)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs/", include_docs_urls(title="Api_libros")),
]