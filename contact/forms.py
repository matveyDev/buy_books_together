from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    '''Форма подписки по email'''
    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email...'
            })
        }
        labels = {
            'email': ''
        }