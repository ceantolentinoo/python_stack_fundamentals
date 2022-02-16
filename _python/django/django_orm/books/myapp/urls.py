from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('add_book', views.add_book),
    path('authors', views.authors),
    path('add_author', views.add_author),
    path('add_author_book', views.add_author_book),
    path('book/<int:bookId>', views.show_book)
]