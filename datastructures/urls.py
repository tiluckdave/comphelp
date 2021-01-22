from django.urls import path
from . import views

urlpatterns = [
    path('', views.ds, name='ds'),
    path('notes', views.dsNotes, name='dsNotes'),
    path('mcqs', views.dsMcqs, name='dsMcqs'),
    path('links', views.dsLinks, name='dsLinks'),
    path('<str:slug>', views.dsPosts, name='dsPosts'),
]