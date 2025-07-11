from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()   
    return render(request, 'index.html',{'posts' : posts})

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'post.html',{'posts' : posts})

def about(request):
    return render(request, 'about.html')