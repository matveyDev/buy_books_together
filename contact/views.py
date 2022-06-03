from django.views.generic import CreateView
from django.shortcuts import redirect
from django.contrib import messages

from .models import Contact
from .forms import ContactForm
from .tasks import send_contact


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            send_contact.delay(email)

            messages.success(request, 'Successfuly send!')

        else:
            messages.error(request, 'Error...')
            form = ContactForm()
            
        return redirect('home')