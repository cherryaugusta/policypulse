from django.contrib import admin
from .models import Decision


@admin.register(Decision)
class DecisionAdmin(admin.ModelAdmin):
    list_display = ("decision_id", "product", "outcome", "confidence", "created_at")
    search_fields = ("decision_id", "applicant_id", "product")
    list_filter = ("outcome", "product")
