from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notices', views.notices, name='notices'),
    path('request', views.request, name='request'),
    path('search', views.search, name='search'),
]