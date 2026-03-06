from django.core.cache import cache
from django.db import connection
from django.http import JsonResponse


def healthcheck_view(request):
    db_ok = False
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1;")
            cursor.fetchone()
        db_ok = True
    except Exception:
        db_ok = False

    redis_ok = False
    try:
        cache.set("healthcheck", "ok", timeout=5)
        redis_ok = cache.get("healthcheck") == "ok"
    except Exception:
        redis_ok = False

    payload = {
        "service": "policypulse-api",
        "database": db_ok,
        "redis": redis_ok,
    }

    status = 200 if (db_ok and redis_ok) else 503
    return JsonResponse(payload, status=status)
