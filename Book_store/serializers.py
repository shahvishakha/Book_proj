from dataclasses import fields
from rest_framework import serializers

from Book_store.models import Book_store

class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book_store
        fields = '__all__'
