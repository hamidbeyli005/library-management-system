from rest_framework import serializers
<<<<<<< HEAD
from books.models import Book, Category

=======
from books.models import Book
>>>>>>> d27ea519bb268256099257c9097feaf17ed38e22


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
<<<<<<< HEAD


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
=======
>>>>>>> d27ea519bb268256099257c9097feaf17ed38e22
