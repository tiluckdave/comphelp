from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('notices', views.notices, name='notices'),
    path('request', views.request, name='request'),
    path('search', views.search, name='search'),
    path('signup', views.handelSignup, name='handelSignup'),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]