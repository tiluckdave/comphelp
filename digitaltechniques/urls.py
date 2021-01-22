from django.urls import path
from . import views

urlpatterns = [
    path('', views.dt, name='dt'),
    path('notes', views.dtNotes, name='dtNotes'),
    path('mcqs', views.dtMcqs, name='dtMcqs'),
    path('links', views.dtLinks, name='dtLinks'),
    path('<str:slug>', views.dtPosts, name='dtPosts'),
]