from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('You are home')

def about(request):
  return HttpResponse('You are on about page')