from django.urls import path
from .views import healthcheck_view

urlpatterns = [
    path("ops/health", healthcheck_view, name="ops-health"),
]
