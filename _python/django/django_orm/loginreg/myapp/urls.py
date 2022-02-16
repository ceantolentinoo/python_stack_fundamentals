from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('add_user', views.user_reg),
    path('login', views.user_login),
]
