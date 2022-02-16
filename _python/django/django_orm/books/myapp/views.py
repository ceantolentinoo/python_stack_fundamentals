from django.shortcuts import render,redirect
from .models import Book, Author

def index(request):
    all_books = Book.objects.all()
    context = {"books": all_books}
    return render(request, "index.html", context)

def authors(request):
    all_authors = Author.objects.all()
    context = {"authors": all_authors}
    return render(request, "authors.html", context)

def show_book(request, bookId):
    book = Book.objects.get(id=bookId)
    all_authors = Author.objects.all()
    context = {"book": book, "authors": all_authors}
    return render(request, "books.html", context)

def add_book(request):
    data = request.POST
    new_book = Book.objects.create(title=data['title'], description=data['desc'])
    return redirect('/')

def add_author(request):
    data = request.POST
    new_author = Author.objects.create(first_name=data['fname'], last_name=data['lname'])
    return redirect('/authors')

def add_author_book(request):
    data = request.POST
    bookId = data['bookId']
    author = Author.objects.get(id=data['author'])
    book = Book.objects.get(id=bookId)
    book.authors.add(author)
    return redirect(f'/book/{bookId}')
# Create your views here.
