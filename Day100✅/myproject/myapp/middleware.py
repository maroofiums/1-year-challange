class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware started🕑")
        response = self.get_response(request)
        print("Middleware Done✅")
        return response