from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time

# Simulate expensive computation
def compute_data():
    time.sleep(2)
    return {'msg': 'This is heavy data!'}

# ✅ Per-view cache for 2 minutes
@cache_page(120)
def home_view(request):
    return render(request, 'home.html')

# ✅ Low-level manual cache
def data_view(request):
    data = cache.get('expensive_data')
    if not data:
        data = compute_data()
        cache.set('expensive_data', data, timeout=120)
    return render(request, 'home.html', {'data': data})
