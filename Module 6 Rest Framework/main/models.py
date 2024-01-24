from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.CharField(max_length=255)
    isbn=models.CharField(max_length=254)
    publisher=models.CharField(max_length=254)
    
    def __str__(self):
        return self.title
    