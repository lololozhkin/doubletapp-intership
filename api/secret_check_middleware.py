from django.http import HttpRequest
from django.core.exceptions import PermissionDenied
import os


class SecretCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        if request.path.startswith('/api/') or request.path == '/api':
            secret = request.headers.get('Secret')
            local_secret = os.environ.get('API_SECRET')
            if not secret or secret != local_secret:
                raise PermissionDenied

        return self.get_response(request)

