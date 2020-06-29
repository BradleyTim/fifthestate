from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def index(request):
  return redirect('blog-home')

def home(request):
  # if request.method == 'GET' and request.GET['tag']:
  #   context = {
  #     'title': request.GET['tag'],
  #     'posts': Post.objects.filter(tags__name=request.GET['tag'])
  #   }
  # else:
  #   context = {
  #     'title': 'Home',
  #     'posts': Post.objects.order_by('date_posted')[::-1]
  #   }
  
  context = {
    'title': 'Posts',
    'posts': Post.objects.order_by('date_posted')[::-1]
  }
  return render(request, 'blog/home.html', context)

def detail(request, pk):
  context = {
    'title': 'Detail',
    'post': Post.objects.get(id=pk)
  }
  return render(request, 'blog/detail.html', context)

def get_by_tags(request):
  if request.method == 'GET' and request.GET['tag']:
    context = {
      'title': request.GET['tag'],
      'posts': Post.objects.filter(tags__name=request.GET['tag'])
    }
  return render(request, 'blog/home.html', context)

def about(request):
  context = {
    'title': 'About'
  }
  return render(request, 'blog/about.html', context)
