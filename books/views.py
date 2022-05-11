from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Favorite
from .forms import FavoriteForm

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {"books": books})


def book_detail(request, pk):
    form = FavoriteForm()
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
        'form': form
    }
    # album = get_object_or_404(Album, pk=pk)
    return render(request, "books/book_detail.html", context)


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)

    return render(request,'books/books_by_category.html', {"books": books, "category": category})


def add_favorite(request,pk):
    if request.method == 'POST':
        book = get_object_or_404(Book,pk=pk)
        user = request.user
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.book = book
            favorite.user = user
            favorite.save()
            return redirect(to='book_detail', pk=pk)


def books_by_favorite(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'books/books_by_favorite.html', {"favorites": favorites})