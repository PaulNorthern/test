from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Api.models import Book, Author
# Create your views here.


class BookListView(ListView):
    ''' Список всех книг '''
    model = Book
    template_name = 'book.html'
    paginate_by = 2
    context_object_name = 'books'


class AuthorDetailView(DetailView):
    ''' Информация об авторе '''
    model = Author
    pk_url_kwarg = 'id'
    template_name = 'author.html'
