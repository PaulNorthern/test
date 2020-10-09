from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from django.http import Http404

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BooksView(APIView):
    ''' Получить список всех книг '''

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})


class BookDeatil(APIView):
    ''' Получить одну книгу по /:id '''

    def get(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404
        serializer = BookSerializer(book)
        return Response(serializer.data)


class AuthorsView(APIView):
    ''' Получить список авторов и их книг '''

    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        print(serializer)
        return Response({"authors": serializer.data})


class AuthorDetail(APIView):
    ''' Получить одного автора по /:id '''

    def get(self, request, author_id):
        try:
            author = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            raise Http404
        serializer = AuthorSerializer(author)
        return Response(serializer.data)
