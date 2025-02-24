from django.db import models
from django.urls import reverse


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
