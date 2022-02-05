from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index),
    path('blogs/new', views.new),
    path('blogs/create', views.create),
    path('blogs/<int:id>', views.show),
    path('blogs/<int:id>/edit', views.edit),
    path('blogs/<int:id>/delete', views.destroy),
    path('blogs/json', views.blogsJson),
    path('blogs/getpost', views.some_function),
    path('users', views.create_user),
]