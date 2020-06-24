from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-index"),
    path('blog/', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]