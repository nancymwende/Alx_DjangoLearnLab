from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm, BookForm
from django.db.models import Q


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def search_books(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()

    return render(request, 'bookshelf/book_list.html', {'books': books})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})SS