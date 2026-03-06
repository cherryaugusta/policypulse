import uuid

HEADER_IN = "HTTP_X_CORRELATION_ID"
HEADER_OUT = "X-Correlation-ID"


class CorrelationIdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cid = request.META.get(HEADER_IN) or str(uuid.uuid4())
        request.correlation_id = cid
        response = self.get_response(request)
        response[HEADER_OUT] = cid
        return response
