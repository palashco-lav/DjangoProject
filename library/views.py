# library/views.py
from django.shortcuts import render
from .models import Book

from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView
from django.views.generic.edit import  CreateView, UpdateView, DeleteView

class BookListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(publication_date__year__gt=2000)

class BookCreateView(CreateView):
    model = Book
    fields = ('title', 'publication_date', 'author')
    template_name = 'library/book_form.html'
    success_url = reverse_lazy("library:books_list")

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_books_count'] = Book.objects.filter(author=self.object.author).count()
        return context

class BookUpdateView(UpdateView):
    model = Book
    fields = ('title', 'publication_date', 'author')
    template_name = 'library/book_form.html'
    success_url = reverse_lazy("library:books_list")

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy("library:books_list")
