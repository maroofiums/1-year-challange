from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request,"home.html",{'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogPostForm()
    return render(request,'add_post.html',{'form':form})
    
def delete_post(request, post_id):
    post = get_object_or_404(BlogPost,id=post_id)
    post.delete()
    return redirect('home')