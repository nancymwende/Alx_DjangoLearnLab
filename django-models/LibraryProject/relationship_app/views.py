from django.shortcuts import render # type: ignore
from django.contrib.auth import login # type: ignore
from django.views.generic.detail import DetailView # type: ignore
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.shortcuts import redirect # type: ignore



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'relationship_app/register.html', {'form': form})