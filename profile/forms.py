from django import forms

from books.models import BooksForFree, BooksForBuy


class CustomUserForm(forms.Form):
    full_name = forms.CharField(max_length=250, required=False)
    age = forms.DateField(required=False)
    photo = forms.ImageField(required=False)
    username = forms.CharField(max_length=250, required=False)


class BookForFreeForm(forms.ModelForm):

    class Meta:
        model = BooksForFree
        fields = [
            'title', 'description',
            'image', 'user', 'category',
        ]


class BookForFreeTagForm(forms.ModelForm):

    class Meta:
        model = BooksForFree
        fields = [
            'title', 'description',
            'image', 'book_file',
            'category',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'category': forms.Select(attrs={'class': 'browser-default', 'name': 'category'}),
        }


class BookForBuyTagForm(forms.ModelForm):

    class Meta:
        model = BooksForBuy
        fields = [
            'title', 'description',
            'image', 'category',
            'book_url', 'finish_goal'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'category': forms.Select(attrs={'class': 'browser-default', 'name': 'category'}),
        }