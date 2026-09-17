from django.utils import timezone


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        skip_paths = ['/admin', '/static', '/media', '/favicon', '/api']
        should_skip = any(
            request.path.startswith(p) for p in skip_paths
        )

        if not should_skip and response.status_code == 200:
            try:
                from .models import VisitorLog
                VisitorLog.objects.create(
                    ip_address=get_client_ip(request),
                    user_agent=request.META.get('HTTP_USER_AGENT', ''),
                    page_visited=request.path,
                )
            except Exception as e:
                print(f"Visitor tracking error: {e}")

        return response