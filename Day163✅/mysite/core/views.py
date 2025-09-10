import time
from django.http import JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page

def expensive_view(request):
    data = cache.get("expensive_data")
    if not data:
        print("Cache MISS - running heavy task...")
        time.sleep(5)
        data = {"message": "This took5 seconds first time!"}
        cache.set("expensive_data",data,30)
    else:
        print("Cache HIT - served instantly!")
    return JsonResponse(data)


@cache_page(15)
def fast_view(request):
    print("View executed!")
    return JsonResponse({"time":time.time()})