from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('add_ninja', views.create_ninja),
    path('add_dojo', views.create_dojo),
]
