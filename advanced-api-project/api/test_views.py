from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        # Create authors
        self.author1 = Author.objects.create(name="John Doe")
        self.author2 = Author.objects.create(name="Jane Doe")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author1,
            publication_year=2020
        )

        # URL endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book.id])
        self.delete_url = reverse("book-delete", args=[self.book.id])

  
    # READ TESTS
 

    def test_get_books(self):
        """Retrieve list of books"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Book")

    def test_get_book_detail(self):
        """Retrieve single book by ID"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")
        self.assertEqual(response.data["author"], self.author1.id)

    # CREATE TESTS
  

    def test_create_book_authenticated(self):
        """Authenticated user can create a book"""
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "New Book",
            "author": self.author2.id,  # must use Author ID
            "publication_year": 2023
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(response.data["title"], "New Book")

    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        data = {
            "title": "New Book",
            "author": self.author2.id,
            "publication_year": 2023
        }

        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

  
    # UPDATE TESTS
 
    def test_update_book_authenticated(self):
        """Authenticated user can update a book"""
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Title",
            "author": self.author1.id,
            "publication_year": 2021
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")
        self.assertEqual(self.book.publication_year, 2021)

    def test_update_book_unauthenticated(self):
        """Unauthenticated users cannot update a book"""
        data = {
            "title": "Hacker Update",
            "author": self.author1.id,
            "publication_year": 2022
        }

        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

   
    # DELETE TESTS
   

    def test_delete_book_authenticated(self):
        """Authenticated user can delete a book"""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        """Unauthenticated users cannot delete a book"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)