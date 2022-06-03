from django.views.generic import FormView, ListView, View
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import get_user_model

from .models import Reviews
from books.models import BooksForFree
from .forms import FeedbackForm, ReviewForm
from .tasks import send_feedback


class FeedbackFormView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback_form.html'

    def post(self, request):
        form = FeedbackForm(request.POST)

        if form.is_valid():
            cleaned_form = form.cleaned_data
            email = cleaned_form['email']
            text = cleaned_form['text']

            if request.user.is_authenticated:
                author = request.user.full_name
            else:
                author = request.user

            send_feedback.delay(email, text, author)
            messages.success(request, 'Successfully send!')

        else:
            messages.error(request, 'Error send...')
            form = FeedbackForm()
        
        return redirect('feedback')


class ReviewsListView(ListView):
    model = BooksForFree
    context_object_name = 'books'
    template_name = 'reviews_list.html'
        

class AddReview(View):
    
    def post(self, request, pk):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            author = get_user_model().objects.get(pk=request.POST['author'])
            book = BooksForFree.objects.get(pk=pk)

            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))

            form.book = book
            form.author = author
            form.save()

            messages.success(request, 'Successfully!')
        
        else:
            messages.error(request, 'You couldn`t send an empty review')
            form = ReviewForm()

        try:
            return redirect(book.get_absolute_url())
        except UnboundLocalError:
            return redirect('home')


class DeleteReview(View):

    def post(self, request, pk):
        review = Reviews.objects.get(pk=pk)
        book = BooksForFree.objects.get(pk=review.book_id)

        try:
            review.delete()
            messages.success(request, 'Successfully delete!')
            return redirect(book.get_absolute_url())
        except:
            messages.error(request, 'Error...')
            return redirect('home')