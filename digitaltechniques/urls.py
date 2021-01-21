from django.urls import path
from . import views

urlpatterns = [
    path('', views.dt, name='dt'),
    path('<str:slug>', views.dtPosts, name='dtPosts'),
]