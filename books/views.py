from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})


def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_books')
    return render(request, "books/add_book.html", {"form": form})


def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    # album = get_object_or_404(Album, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect(to='list_books')
    return render(request, "books/delete_book.html", {"book": book})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = BookForm(instance=book)
    else:
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')
    return render(request, "books/edit_book.html", {"form": form, "book": book})