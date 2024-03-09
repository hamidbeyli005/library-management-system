from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view(), name='book-retrieve-update-destroy'),
]
