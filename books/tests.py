from django.test import TestCase
from .models import Book

# Create your tests here.
# d


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
