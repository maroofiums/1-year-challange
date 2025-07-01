from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
import json
from .gemini import get_gemini_response
from .models import ChatMessage

# Authentication Views
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered!')
            return render(request, 'auth/register.html')
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'auth/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat_interface')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

# Chat Views (with authentication required)
@login_required(login_url='login')
def chat_interface(request):
    # Only show messages for the current user
    messages = ChatMessage.objects.filter(user=request.user).order_by('timestamp')
    return render(request, 'chat.html', {'messages': messages})

@csrf_exempt
@login_required(login_url='login')
def chatbot_response(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "")

        # Get response from Gemini
        bot_response = get_gemini_response(user_message)

        # Save chat in DB with user association
        ChatMessage.objects.create(
            user=request.user,  # Associate with current user
            user_message=user_message,
            bot_reply=bot_response
        )

        return JsonResponse({"reply": bot_response})
    
    return JsonResponse({"error": "Invalid request method"}, status=405)