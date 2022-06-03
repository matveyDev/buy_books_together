from django.contrib import admin
from .models import Contact
from django import forms


class ContactAdminForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


@admin.register(Contact)
class BooksForBuyAdmin(admin.ModelAdmin):
    form = ContactAdminForm