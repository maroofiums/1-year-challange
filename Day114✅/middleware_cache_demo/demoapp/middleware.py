class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"📥 Request Path: {request.path}")
        response = self.get_response(request)
        print(f"📤 Response Status: {response.status_code}")
        return response
