from django.urls import path
from . import views

urlpatterns = [
    path('', views.cg, name='cg'),
    path('notes', views.cgNotes, name='cgNotes'),
    path('mcqs', views.cgMcqs, name='cgMcqs'),
    path('links', views.cgLinks, name='cgLinks'),
    path('<str:slug>', views.cgPosts, name='cgPosts'),
]