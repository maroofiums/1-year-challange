import time
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

@cache_page(10)  # View-level cache for 10 seconds
def slow_view(request):
    time.sleep(3)  # Simulate heavy computation
    return HttpResponse(f"Slow response generated at {time.time()}")

def fast_view(request):
    return HttpResponse(f"Fast response generated at {time.time()}")
