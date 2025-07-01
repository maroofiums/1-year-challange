from django.shortcuts import render, redirect
from .models import Post
from django.contrib import messages

def post_view(request):
    if request.method == "POST":
        file = request.FILES
        data = request.POST
        title = data.get('title')
        descriptions = data.get('descriptions')
        image = file.get('image')

        if title and descriptions and image:
            Post.objects.create(
                title=title,
                descriptions=descriptions,
                image=image,
            )
            messages.success(request, "Post added successfully!")
        else:
            messages.error(request, "All fields are required.")

        return redirect('/')
    
    queryset = Post.objects.all()
    context = {'post': queryset}
    return render(request, "post.html", context)

def delete_view(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.success(request,"Deleted ")
    return redirect('/')

def update_view(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        file = request.FILES
        data = request.POST
        title = data.get('title')
        descriptions = data.get('descriptions')
        image = file.get('image')

        post.title = title
        post.descriptions = descriptions

        if image:
            post.image = image

        post.save()
        messages.info(request, "Updated!")

        return redirect('/')
    context = {"post":post}
    return render(request,"update_post.html",context)