from django.urls import path
from . import views

urlpatterns = [
    path('', views.ds, name='ds'),
    path('notes', views.dsNotes, name='dsNotes'),
    path('mcqs', views.dsMcqs, name='dsMcqs'),
    path('links', views.dsLinks, name='dsLinks'),
    # API for comments
    path('postComment', views.postComment, name="postComment"),
    path('<str:slug>', views.dsPosts, name='dsPosts'),
]