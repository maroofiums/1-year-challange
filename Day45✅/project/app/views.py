from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Posts

def add_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        Posts.objects.create(title=title, description=description)
        messages.success(request, "Recipe added successfully!")
        return redirect('/')

    queryset = Posts.objects.all().order_by('-created_at')  # Latest first
    return render(request, 'post.html', {'posts': queryset})

def delete(request, id):
    post = Posts.objects.get(id=id)
    post.delete()
    messages.success(request, "Recipe deleted successfully!")
    return redirect('/')