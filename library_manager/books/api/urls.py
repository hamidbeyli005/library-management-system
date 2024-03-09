from django.urls import path
from books.api import views as api_views

urlpatterns = [
    path('books/', api_views.BookListCreateAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view(), name='book_detail'),
<<<<<<< HEAD
    path('categories/', api_views.CategoryListCreateAPIView.as_view(), name='category_list'),
    path('categories/<int:pk>/', api_views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_detail'),
=======
>>>>>>> d27ea519bb268256099257c9097feaf17ed38e22
]
