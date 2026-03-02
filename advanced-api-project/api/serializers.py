from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author']

    # Custom validation: publication_year cannot be in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for Author model
# Includes nested BookSerializer to dynamically serialize related books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested relationship

    class Meta:
        model = Author
        fields = ['name', 'books']