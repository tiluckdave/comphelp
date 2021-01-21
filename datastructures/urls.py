from django.urls import path
from . import views

urlpatterns = [
    path('', views.ds, name='ds'),
    path('<str:slug>', views.dsPosts, name='dsPosts'),
]