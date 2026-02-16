from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# 1️⃣ Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# 2️⃣ Class-based view to display a specific library and its books
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

