from django.db import models

from django.utils.timezone import now

class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.DateField(default=now)
    author = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

