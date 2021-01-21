from django.urls import path
from . import views

urlpatterns = [
    path('', views.cg, name='cg'),
    path('<str:slug>', views.cgPosts, name='cgPosts'),
]