from django.test import TestCase
from ..models import Book


class BookTest(TestCase):
    """ Test module for Book model """

    def setUp(self):
        Book.objects.create(
            isbn='0000000000001',
            bookName='book name 1',
            company='company 1',
            price=1.00,
            genreCode=1
        )
        Book.objects.create(
            isbn='0000000000002',
            bookName='book name 2',
            company='company 2',
            price=2.00,
            genreCode=2
        )
