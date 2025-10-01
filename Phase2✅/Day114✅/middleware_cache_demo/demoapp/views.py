from django.shortcuts import render
from django.views.decorators.cache import cache_page
import time

@cache_page(30)  # Cache this view for 30 seconds
def home(request):
    current_time = time.strftime('%H:%M:%S')
    context = {"time": current_time}
    return render(request, "home.html", context)
