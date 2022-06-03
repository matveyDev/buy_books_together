from .forms import SearchForm
from django.views.generic import ListView

from .service import get_correct_queryset
from books.models import BooksForBuy, BooksForFree


class SearchForm(ListView):
    template_name = 'search.html'
    context_object_name = 'queryset'
    form_class = SearchForm

    def get_queryset(self):
        query = self.request.GET.get('text')
        queryset_buy_books = get_correct_queryset(query, BooksForBuy)
        queryset_free_books = get_correct_queryset(query, BooksForFree)

        queryset = [queryset_buy_books, queryset_free_books]

        return queryset