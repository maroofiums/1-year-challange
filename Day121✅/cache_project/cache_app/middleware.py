from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"[LOG] Request path: {request.path}")

    def process_response(self, request, response):
        print(f"[LOG] Status Code: {response.status_code}")
        return response
