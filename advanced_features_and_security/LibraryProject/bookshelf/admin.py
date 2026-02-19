from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser

# Book admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')  # remove publication_year if not in model
    list_filter = ('author',)
    search_fields = ('title', 'author__name')

admin.site.register(Book, BookAdmin)

# CustomUser admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
