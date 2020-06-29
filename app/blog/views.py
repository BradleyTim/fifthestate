from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
  return redirect('blog-home')

def home(request):
  context = {
    'title': 'Home',
    'posts': Post.objects.order_by('date_posted')[::-1]
  }
  return render(request, 'blog/home.html', context)

def detail(request, pk):
  context = {
    'title': 'Detail',
    'post': Post.objects.get(id=pk)
  }
  return render(request, 'blog/detail.html', context)

def about(request):
  context = {
    'title': 'About'
  }
  return render(request, 'blog/about.html', context)
