from django.db import models


class Book(models.Model):
    isbn = models.CharField(primary_key=True, max_length=13, blank=False, default='')
    bookName = models.CharField(max_length=50, blank=False, default='')
    company = models.CharField(max_length=50, blank=False, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genreCode = models.IntegerField(blank=False)
