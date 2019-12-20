from django.db import models
from datetime import date, datetime

# Create your models here.


class TypeBooks(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type


class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_published = models.DateField(
        auto_now_add=False, auto_now=False, blank=True)
    number_of_pages = models.IntegerField()
    type_of_book = models.ForeignKey(TypeBooks, on_delete=models.CASCADE)
