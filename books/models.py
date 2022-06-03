from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name="Title category")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('books_for_buy_list_by_category', kwargs={'category_slug': self.slug})

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class BooksForBuy(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Title')
    description = models.TextField(max_length=5000, blank=True, verbose_name='Descriptions')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Cover')
    slug = models.SlugField(max_length=255, allow_unicode=True, unique=True, db_index=True, verbose_name='URL')
    buyers = models.ManyToManyField(get_user_model(), related_name='books_for_buy', blank=True, verbose_name='Buyer')
    finish_goal = models.PositiveIntegerField(blank=False, verbose_name='Goal')
    book_url = models.URLField(blank=False, null=True, verbose_name='Link on book')
    current_goal = models.PositiveIntegerField(default=0, verbose_name='collected')
    end = models.BooleanField(default=False, verbose_name='Goal end')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category, verbose_name='Category', related_name='books_for_buy',
        null=True, on_delete=models.SET_NULL
    )
    
    def get_absolute_url(self):
        return reverse('books_for_buy_detail', kwargs={'slug': self.slug, 'category_slug': self.category.slug})

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга для покупки'
        verbose_name_plural = 'Книги для покупок'
        ordering = ['-id']


class BooksForFree(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Title')
    description = models.TextField(max_length=5000, blank=True, verbose_name='Description')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Cover')
    book_file = models.FileField(blank=False, null=True, upload_to='files/%Y/%m/%d/', verbose_name='Book')
    views = models.IntegerField(default=0, verbose_name='Views')
    user = models.ForeignKey(
        get_user_model(), related_name='books_for_free', null=True,
        verbose_name='User', on_delete=models.SET_NULL
    )
    slug = models.SlugField(max_length=255, allow_unicode=True, unique=True, db_index=True, null=True, verbose_name='URL')
    category = models.ForeignKey(
        Category, verbose_name='Category', null=True,
        related_name='books_for_free', on_delete=models.SET_NULL
    )

    def get_absolute_url(self):
        return reverse('books_for_free_detail', kwargs={'slug': self.slug, 'category_slug': self.category.slug})

    def get_reviews(self):
        return self.reviews.filter(parent__isnull=True)

    def __str__(self):
        return str(self.title)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Книга бесплатная'
        verbose_name_plural = 'Книги бесплатные'
        ordering = ['-id']