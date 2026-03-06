from django.db import models


class Decision(models.Model):
    OUTCOME_APPROVE = "approve"
    OUTCOME_REVIEW = "review"
    OUTCOME_REJECT = "reject"
    OUTCOME_CHOICES = [
        (OUTCOME_APPROVE, "Approve"),
        (OUTCOME_REVIEW, "Review"),
        (OUTCOME_REJECT, "Reject"),
    ]

    decision_id = models.CharField(max_length=36, unique=True)
    product = models.CharField(max_length=64)
    applicant_id = models.CharField(max_length=128)
    outcome = models.CharField(max_length=16, choices=OUTCOME_CHOICES)
    reason_codes = models.JSONField(default=list)

    model_version = models.CharField(max_length=32)
    prompt_id = models.CharField(max_length=64, null=True, blank=True)
    prompt_version = models.CharField(max_length=32, null=True, blank=True)
    retrieval_sources = models.JSONField(default=list)
    confidence = models.FloatField()
    explanation = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.decision_id} ({self.outcome})"
