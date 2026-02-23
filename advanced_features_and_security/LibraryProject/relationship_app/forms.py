from django import forms
from .models import Book
from .models import Article

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']       
