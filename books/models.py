from django.db import models

# Create your models here.


class Books(models.Model):
    isbn = models.CharField(max_length=13, blank=False, default='')
    book_name = models.CharField(max_length=50, blank=False, default='')
    company = models.CharField(max_length=50, blank=False, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre_code = models.IntegerField(blank=False)
