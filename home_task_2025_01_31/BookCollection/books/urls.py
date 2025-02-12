from django.urls import path
from .views import BooksView

urlpatterns = [
    path('books/', BooksView.as_view(), name='books'),
    path('books/<str:book_id>/', BooksView.as_view(), name='book_detail'),
]