from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Article


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
admin.site.register(Article)


