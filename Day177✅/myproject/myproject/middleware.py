import time
from django.utils.deprecation import MiddlewareMixin

class SimpleLogMiddleware(MiddlewareMixin):
    
    def process_request(self,request):
        request.start_time = time.time()
        print(f"Request URL: {request.path}")
    
    def process_response(self, request, response):
        duration = None
        if hasattr(request,"start_time"):
            duration = time.time() - request.start_time
        print(f"Response Status: {response.status_code}")
        if duration:
            print(f"Execution Time: {duration:.4f} seconds")
        response["X-Custom-Header"] = "MaroofLearning"
        return response        