from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time

def home(request):
    return HttpResponse("Hello from Home!")

@cache_page(60)
def slow_view(request):
    time.sleep(2)
    return HttpResponse("This was a slow response ⏳")

def cached_data(request):
    data = cache.get("my_data")
    if not data:
        print(f"cache MISS: computing data...")
        time.sleep(3)
        data = "Heavy Data Calculated!"
        cache.set("my_data",data,timeout=300)
    else:
        print("Cache HIT: serving from cache") 
    
    return HttpResponse(data)