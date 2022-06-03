from allauth.account.forms import SignupForm, LoginForm
from rest_framework.authtoken.models import Token
from django import forms

class CustomSignupForm(SignupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password1'].widget.attrs['placeholder']
        del self.fields['password2'].widget.attrs['placeholder']

    email = forms.EmailField(label='E-mail', required=True)
    username = forms.CharField(label='Логин', max_length=50, required=True)
    password1 = forms.CharField(label='Пароль', max_length=100, required=True)
    password2 = forms.CharField(label='Пароль(ещё раз)', max_length=100, required=True)
    full_name = forms.CharField(label='ФИО', max_length= 250, required=False)
    age = forms.CharField(label='Дата рождения', min_length=4, max_length=4, required=False)
    photo = forms.ImageField(label='Фото профиля', required=False)

    def save(self, request):
        user = super().save(request)
        new_token = Token.objects.create(user=user)
        return user

    def signup(self, user):
        user.username = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.email = self.cleaned_data['email']
        user.full_name = self.cleaned_data['full_name']
        user.age = self.cleaned_data['age']
        user.photo = self.cleaned_data['photo']
        user.subscriber = False
        user.save()
        return user
    

class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['login'].widget.attrs['placeholder']
        del self.fields['password'].widget.attrs['placeholder']