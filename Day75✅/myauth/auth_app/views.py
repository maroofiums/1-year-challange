from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# Dashboard (only for logged-in users)
@login_required
def dashboard_view(request):
    return render(request, "dashboard.html")  # FIXED: render, not redirect

# Signup view
def signup_view(request):
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already exists.")
            return redirect('login_signup')  # FIXED

        user = User.objects.create_user(username=email, email=email, password=password, first_name=name)
        user.save()
        messages.success(request, 'Account created successfully. Please log in.')
        return redirect("login_signup")

    return redirect("login_signup")  # Always go back if not POST

# Login view
def login_view(request):
    if request.method == "POST":
        data = request.POST
        email = data.get("email")
        password = data.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login_signup')

    return redirect('login_signup')

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("login_signup")
def login_signup_view(request):
    return render(request, "login.html")