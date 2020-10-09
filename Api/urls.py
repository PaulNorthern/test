from django.urls import path
from .views import BooksView, BookDeatil, AuthorDetail, AuthorsView

app_name = "books"

urlpatterns = [
    path('books/', BooksView.as_view()),
    path('books/<int:book_id>/', BookDeatil.as_view()),
    path('authors/', AuthorsView.as_view()),
    path('authors/<int:author_id>/', AuthorDetail.as_view()),
]
