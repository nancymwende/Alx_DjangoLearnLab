from django.shortcuts import render # type: ignore
from django.contrib.auth import login 
from django.views.generic.detail import DetailView # type: ignore
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm # type: ignore
from django.shortcuts import redirect # type: ignore
from django.contrib.auth.decorators import user_passes_test



def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


# Admin-only view
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian-only view
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member-only view
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')