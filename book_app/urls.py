from django.contrib import admin
from django.urls import path, include, re_path
from . views import BookListView, AuthorDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name="book_list"),
    path('books/<int:id>/', AuthorDetailView.as_view(), name="author-detail"),
]
