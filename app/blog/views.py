from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  context = {
    'title': 'Home',
    'blog': 'THIS BLOG IS ABOUT TO GO VIRAL'
  }
  return render(request, 'blog/home.html', context)

def about(request):
  context = {
    'title': 'About'
  }
  return render(request, 'blog/about.html', context)
