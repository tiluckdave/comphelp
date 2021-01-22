from django.urls import path
from . import views

urlpatterns = [
    path('', views.mp, name='mp'),
    path('notes', views.mpNotes, name='mpNotes'),
    path('mcqs', views.mpMcqs, name='mpMcqs'),
    path('links', views.mpLinks, name='mpLinks'),
    path('<str:slug>', views.mpPosts, name='mpPosts'),
]