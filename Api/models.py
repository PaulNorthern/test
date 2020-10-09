from django.db import models

GENDER_CATEGORY = (
    ('U', 'Undefined'),
    ('F', 'Female'),
    ('M', 'Male'))


class Author(models.Model):
    name = models.CharField(max_length=64)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER_CATEGORY,
                              max_length=2, default='U')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ForeignKey(
        Author, related_name='library', on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
