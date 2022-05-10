from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    # album = get_object_or_404(Album, pk=pk)
    return render(request, "books/book_detail.html", context)


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    return render(request,'books/books_by_category.html', {"books": books, "category": category})
