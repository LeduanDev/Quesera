# middleware.py

from django.http import HttpResponseNotFound

class ForbiddenAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 302 and response.url.startswith('/accounts/login'):
            return HttpResponseNotFound('<h1>Error 404 - Not Found</h1><p>The requested page was not found.</p>')
        return response
