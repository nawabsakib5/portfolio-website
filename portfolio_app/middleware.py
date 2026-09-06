import threading
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR')


def send_visitor_email_async(ip, user_agent, page, time):
    try:
        send_mail(
            subject=f'🔔 New Visitor on Your Portfolio!',
            message=f'''
New visitor detected!

🌐 IP Address: {ip}
📄 Page Visited: {page}
🕐 Time: {time}
💻 Browser: {user_agent[:100]}

Visit your portfolio: https://portfolio-website-aey7.onrender.com
            ''',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL],
            fail_silently=True,
        )
    except Exception as e:
        print(f"Email error: {e}")


class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # শুধু main page track করবো, admin/static বাদ
        skip_paths = ['/admin', '/static', '/media', '/favicon', '/api']
        should_skip = any(
            request.path.startswith(p) for p in skip_paths
        )

        if not should_skip and response.status_code == 200:
            try:
                from .models import VisitorLog
                ip = get_client_ip(request)
                user_agent = request.META.get('HTTP_USER_AGENT', '')
                page = request.path
                now = timezone.now().strftime('%Y-%m-%d %H:%M:%S UTC')

                # Database-এ save
                VisitorLog.objects.create(
                    ip_address=ip,
                    user_agent=user_agent,
                    page_visited=page,
                )

                # Email background thread-এ পাঠাবো
                thread = threading.Thread(
                    target=send_visitor_email_async,
                    args=(ip, user_agent, page, now)
                )
                thread.daemon = True
                thread.start()

            except Exception as e:
                print(f"Visitor tracking error: {e}")

        return response