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
        # get data from db
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.content, JsonResponse(
            serializer.data, safe=False).content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleBookTest(TestCase):
    """ Test module for GET single book API """

    def setUp(self):
        self.book1 = Book.objects.create(
            isbn='0000000000001',
            bookName='sample book 1',
            company='sample company 1',
            price=1.00,
            genreCode=1
        )
        self.book2 = Book.objects.create(
            isbn='0000000000002',
            bookName='sample book 2',
            company='sample company 2',
            price=2.00,
            genreCode=2
        )
        self.book3 = Book.objects.create(
            isbn='0000000000003',
            bookName='sample book 3',
            company='sample company 3',
            price=3.00,
            genreCode=3
        )

    def test_get_valid_single_book(self):
        response = client.get(
            reverse('book_detail', kwargs={'pk': self.book2.pk})
        )
        book = Book.objects.get(pk=self.book2.pk)
        serializer = BookSerializer(book)
        self.assertEqual(response.content, JsonResponse(
            serializer.data, safe=False).content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_book(self):
        response = client.get(
            reverse('book_detail', kwargs={'pk': '0000000000004'})
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewBookTest(TestCase):
    """ Test module for inserting a new book """

    def setUp(self):
        self.valid_payload = {
            'isbn': '0000000000001',
            'bookName': 'sample book 1',
            'company': 'sample company 1',
            'price': 1.00,
            'genreCode': 1
        }
        self.invalid_payload = {
            'isbn': '00000000000001',
            'bookName': 'sample book 1',
            'company': 'sample company 1',
            'price': 1.00,
            'genreCode': 1
        }

    def test_create_valid_book(self):
        response = client.post(
            reverse('book_list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_book(self):
        response = client.post(
            reverse('book_list'),
            data=json.dumps(self.invalid_payload),
            content_type='aplication/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSingleBookTest(TestCase):
    """ Test module for updating an existing book record """

    def setUp(self):
        self.book1 = Book.objects.create(
            isbn='0000000000001',
            bookName='sample book 1',
            company='sample company 1',
            price=1.00,
            genreCode=1
        )
        self.book2 = Book.objects.create(
            isbn='0000000000002',
            bookName='sample book 2',
            company='sample company 2',
            price=2.00,
            genreCode=2
        )

        self.valid_payload = {
            'isbn': '0000000000003',
            'bookName': 'sample book 2',
            'company': 'sample company 2',
            'price': 2.22,
            'genreCode': 2
        }
        self.invalid_payload = {
            'isbn': '00000000000001',
            'bookName': 'sample book 1',
            'company': 'sample company 1',
            'price': 1.00,
            'genreCode': 1
        }

    def test_valid_update_book(self):
        responese = client.put(
            reverse('book_detail', kwargs={'pk': self.book1.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(responese.status_code, status.HTTP_200_OK)

    def test_invalid_update_book(self):
        response = client.put(
            reverse('book_detail', kwargs={'pk': self.book2.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='appliction/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleBookTest(TestCase):
    """ Test module for deleting an existing book record """

    def setUp(self):
        self.book1 = Book.objects.create(
            isbn='0000000000001',
            bookName='sample book 1',
            company='sample company 1',
            price=1.00,
            genreCode=1
        )
        self.book2 = Book.objects.create(
            isbn='0000000000002',
            bookName='sample book 2',
            company='sample company 2',
            price=2.00,
            genreCode=2
        )

    def test_valid_delete_book(self):
        response = client.delete(
            reverse('book_detail', kwargs={'pk': self.book1.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_book(self):
        response = client.delete(
            reverse('book_detail', kwargs={'pk': '0000000000003'})
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
