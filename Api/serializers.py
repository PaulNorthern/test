from rest_framework import serializers
from . import models


class BookSerializer(serializers.ModelSerializer):

    author_name = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = models.Book
        fields = ('id', 'name', 'author_name')


class AuthorSerializer(serializers.ModelSerializer):

    library = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Author
        fields = ('id', 'name', 'library')
