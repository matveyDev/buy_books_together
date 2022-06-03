from .models import Reviews
from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(required=True)
    text = forms.CharField(max_length=5000, required=True,
        widget=forms.Textarea(attrs={'rows': 6})
    )


class ReviewForm(forms.ModelForm):
    
    class Meta:
        model = Reviews
        fields = ['text',]