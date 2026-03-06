import uuid

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Decision
from .serializers import DecisionCreateSerializer, DecisionSerializer


class SubmitDecisionView(APIView):
    def post(self, request):
        serializer = DecisionCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        decision_id = str(uuid.uuid4())

        decision = Decision.objects.create(
            decision_id=decision_id,
            product=data["product"],
            applicant_id=data["applicant_id"],
            outcome=Decision.OUTCOME_REVIEW,
            reason_codes=["INSUFFICIENT_EVIDENCE"],
            model_version="0.1.0",
            prompt_id="decision_rationale",
            prompt_version="1.0.0",
            retrieval_sources=[],
            confidence=0.42,
            explanation={
                "note": "Day Zero stub: deterministic routing to REVIEW",
                "correlation_id": getattr(request, "correlation_id", None),
            },
        )

        out = DecisionSerializer(decision).data
        return Response(out, status=status.HTTP_201_CREATED)
