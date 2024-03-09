from rest_framework import generics
<<<<<<< HEAD
from books.models import Book, Category
from books.api.serializers import BookSerializer, CategorySerializer
=======
from books.api.serializers import BookSerializer
from books.models import Book
>>>>>>> d27ea519bb268256099257c9097feaf17ed38e22


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
<<<<<<< HEAD


class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
=======
>>>>>>> d27ea519bb268256099257c9097feaf17ed38e22
