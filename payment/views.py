from django.views.generic import View
from django.contrib import messages
from django.db.models import F
from django.shortcuts import redirect

from .tasks import send_mails, add_user_in_buyers
from books.models import BooksForBuy
from .forms import PaymentTagForm

class PaymentFormView(View):
    
    def post(self, request):
        form = PaymentTagForm(request.POST)
        
        if form.is_valid():
            amount = request.POST['amount']
            book_pk = request.POST['book_pk']

            book = BooksForBuy.objects.get(pk=book_pk)
            book.current_goal = F('current_goal') + int(amount)
            book.save()

            send_mails.delay(request.user.username, book_pk, amount)
            add_user_in_buyers.delay(book_pk, request.user.pk)
            messages.success(request, f'Successfuly invest {amount} RUB !')

        else:
            form = PaymentTagForm()
            messages.error(request, 'Error...')
        
        return redirect('home')

    def get(self, request):
        print(request.GET)