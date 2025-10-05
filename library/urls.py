# library/urls.py
from django.urls import path
from .views import BookUpdateView, BookListView, BookCreateView, BookDeleteView, BookDetailView, AuthorCreateView, AuthorListView

# from .views import books_list, book_detail

app_name = 'library'
urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='authors_list'),
    path('author/new/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorCreateView.as_view(), name='author_update'),

    path('books/', BookListView.as_view(), name='books_list'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]