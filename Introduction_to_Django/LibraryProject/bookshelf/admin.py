from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add filters for these fields
    list_filter = ('author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')

# Register the Book model with the custom BookAdmin
admin.site.register(Book, BookAdmin)