from .models import Book    
from rest_framework import serializers

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'
        #fields=['id','title','isbn','publisher','author']