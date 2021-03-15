from books.serializers import BookSerializer
from django.http import response
from django.test import TestCase, Client
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.http.response import JsonResponse
from .models import Book
from rest_framework.response import Response
import json

# Create your tests here.
# d

client = Client()
apiClient = APIClient()

class ModelTestCase(TestCase):
    """This class defines the test suite for book model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.book_isbn = "1234567890123"
        self.book = Book(isbn=self.book_isbn)

    def test_model_can_create_a_book(self):
        """Test the book model can create a book."""
        old_count = Book.objects.count()
        self.book.save()
        new_count = Book.objects.count()
        self.assertNotEqual(old_count, new_count)


class GetAllBooksTest(TestCase):
    """  Test module for GET all books API """

    def setUp(self):
        Book.objects.create(
            isbn='0000000000001',
            bookName='sample book 1',
            company='sample company 1',
            price=1.00,
            genreCode=1
        )
        Book.objects.create(
            isbn='0000000000002',
            bookName='sample book 2',
            company='sample company 2',
            price=2.00,
            genreCode=2
        )
        Book.objects.create(
            isbn='0000000000003',
            bookName='sample book 3',
            company='sample company 3',
            price=3.00,
            genreCode=3
        )

    def test_get_all_books(self):
        # get API response
        response = client.get(reverse('book_list'))
        apiResponse = apiClient.get(reverse('book_list'))
        # get data from db
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.content, JsonResponse(serializer.data, safe=False).content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
