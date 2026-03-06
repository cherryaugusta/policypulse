from django.urls import path
from .views import SubmitDecisionView

urlpatterns = [
    path("decisions/submit", SubmitDecisionView.as_view(), name="decisions-submit"),
]
