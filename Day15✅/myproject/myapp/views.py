from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")

def register_view(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        messages.success(request, "Welcome! You have registered successfully.")
        return redirect("dashboard")

    return render(request, "register.html")

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")  # Prevent redirect loop if already logged in

    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Welcome! You have logged in successfully.")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials!")
            return redirect("login")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect("login")
