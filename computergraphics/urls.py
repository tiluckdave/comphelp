from django.urls import path
from . import views

urlpatterns = [
    path('', views.cg, name='cg'),
    path('notes', views.cgNotes, name='cgNotes'),
    path('mcqs', views.cgMcqs, name='cgMcqs'),
    path('links', views.cgLinks, name='cgLinks'),
    # API for comments
    path('postComment', views.postComment, name="postComment"),


    path('<str:slug>', views.cgPosts, name='cgPosts'),
]