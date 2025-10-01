from django.shortcuts import render,HttpResponse

# Create your views here.

def greet(request):
    return HttpResponse("<center><h1><b>Hello This is Middleware Testing.</b></h1></center>")