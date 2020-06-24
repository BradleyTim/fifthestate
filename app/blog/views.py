from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
  return redirect('blog-home')

def home(request):
  context = {
    'title': 'Home',
    'posts': Post.objects.all()
  }
  return render(request, 'blog/home.html', context)

def about(request):
  context = {
    'title': 'About'
  }
  return render(request, 'blog/about.html', context)
