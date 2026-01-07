import requests
from django.shortcuts import render

def chat_view(request):
    response = None
    if request.method == "POST":
        user_text = request.POST.get("user_text")

        api_response = requests.post(
            "https://127.0.0.1:8000/chat",
            json={"message": user_text}
        )
        response = api_response.json()
    return render(request, "chat.html", {"response": response})

