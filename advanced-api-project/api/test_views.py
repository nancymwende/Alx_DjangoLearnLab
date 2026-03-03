from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
       
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        
        self.book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_year=2020
        )

      
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])

    def test_get_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)