from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.shortcuts import reverse
from books.models import BooksForFree

class Reviews(models.Model):
    likes = models.PositiveIntegerField(default=0, verbose_name='Лайки')
    text = models.TextField(blank=False, max_length=5000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано:')
    parent = models.ForeignKey(
        'self', verbose_name='Родитель',
        related_name='children', blank=True, null=True, on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        get_user_model(), verbose_name='Автор',
        related_name='reviews', null=True, on_delete=models.SET_NULL
    )
    book = models.ForeignKey(
        BooksForFree, verbose_name='Книга',
        related_name='reviews', null=True, on_delete=models.SET_NULL
    )

    def get_absolute_url(self):
        return reverse('books for free', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.author) + ' | ' + str(self.book)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['likes']


class Rating(models.Model):
    rating = models.IntegerField(
        blank=False, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='Рейтинг'
    )
    author = models.ForeignKey(
        get_user_model(), verbose_name='Автор',
        related_name='ratings', null=True, on_delete=models.SET_NULL
    )
    book = models.ForeignKey(
        BooksForFree, verbose_name='Книга',
        related_name='ratings', null=True, on_delete=models.SET_NULL
    )

    def get_absolute_url(self):
        return reverse('rating', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.author) + ' ' + str(self.rating)

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'
        ordering = ['rating']