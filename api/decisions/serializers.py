from rest_framework import serializers
from .models import Decision


class DecisionCreateSerializer(serializers.Serializer):
    applicant_id = serializers.CharField(max_length=128)
    product = serializers.CharField(max_length=64)
    features = serializers.DictField(child=serializers.JSONField(), required=True)


class DecisionSerializer(serializers.ModelSerializer):
    provenance = serializers.SerializerMethodField()

    class Meta:
        model = Decision
        fields = [
            "decision_id",
            "product",
            "applicant_id",
            "outcome",
            "reason_codes",
            "provenance",
            "created_at",
        ]

    def get_provenance(self, obj: Decision):
        return {
            "model_version": obj.model_version,
            "prompt_id": obj.prompt_id,
            "prompt_version": obj.prompt_version,
            "retrieval_sources": obj.retrieval_sources,
            "confidence": obj.confidence,
            "explanation": obj.explanation,
            "created_at": obj.created_at.isoformat(),
        }
