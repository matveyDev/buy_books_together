from django.views.generic import DetailView, FormView, View
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib import messages
from .forms import CustomUserForm, BookForFreeTagForm, BookForBuyTagForm

from .logic import age_is_valid, photo_is_valid, username_is_valid
from .service import create_free_book, create_buy_book
from .tasks import email_free_book, email_buy_book

class ProfileDetailView(DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'client'


class ProfileUpdateView(FormView):
    template_name = 'update_profile.html'
    context_object_name = 'client'
    form_class = CustomUserForm

    def post(self, request, pk):
        form = CustomUserForm(request.POST, request.FILES)

        if form.is_valid():
            full_name = request.POST.get('full_name')
            age = request.POST.get('age')
            photo = request.FILES.get('photo')
            username = form.cleaned_data['username']

            user = get_user_model().objects.get(pk=pk)
            user.full_name = full_name

            if age_is_valid(age):
                user.age = age
            
            if photo_is_valid(photo):
                user.photo = photo

            if username_is_valid(username, pk):
                user.username = username
            else:
                messages.warning(request, 'This username is already taken!')
                return redirect('update_profile', pk)
            
            user.save()

            messages.success(request, 'Successful!')

        else:
            form = CustomUserForm()
            messages.error(request, 'Error...')

        return redirect('update_profile', pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['client'] = get_user_model().objects.get(pk=self.kwargs['pk'])
        return context


class AddBookForFree(View):
    form_class = BookForFreeTagForm

    def post(self, request):
        form = BookForFreeTagForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                create_free_book(request)
                email_free_book.delay(request.user.username)
                messages.success(request, 'Successfuly add!')
            except:
                messages.warning(request, 'This title already taken')

        else:
            messages.error(request, 'Error...')
            form = BookForFreeTagForm()
            
        return redirect('profile', request.user.pk)


class AddBookForBuy(View):
    form_class = BookForBuyTagForm

    def post(self, request):
        form = BookForBuyTagForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                create_buy_book(request)
                email_buy_book.delay(request.user.username)
                messages.success(request, 'Successfuly add!')
            except:
                messages.warning(request, 'This title already taken')

        else:
            messages.error(request, 'Error...')
            form = BookForBuyTagForm()
            
        return redirect('profile', request.user.pk)