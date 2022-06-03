from django.db import models

class Contact(models.Model):
    email = models.EmailField(max_length=254, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Email`s'
        ordering = ['-id']