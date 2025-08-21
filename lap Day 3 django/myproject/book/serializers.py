from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'description', 'price', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be positive.")
        return value
