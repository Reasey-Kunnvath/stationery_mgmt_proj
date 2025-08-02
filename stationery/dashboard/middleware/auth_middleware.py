# your_app/middleware.py
from django.http import HttpResponseRedirect
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class RestrictURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.debug(f"Request path: {request.path}, User: {request.user}, Authenticated: {hasattr(request, 'user') and request.user.is_authenticated}")

        exempt_urls = [
            settings.LOGIN_URL,
            '/static/',
            '/media/',
        ]

        if not any(request.path.startswith(url) for url in exempt_urls):
            if not hasattr(request, 'user') or not request.user.is_authenticated:
                logger.debug(f"Redirecting to: {settings.LOGIN_URL}")
                return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)