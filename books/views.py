from .models import BooksForBuy, BooksForFree, Category
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.dates import MonthArchiveView
from django.utils import timezone
from django.db.models import F


class HomePage(MonthArchiveView):
    model = BooksForBuy
    template_name = 'home_list_books.html'
    context_object_name = 'books'
    date_field = 'created_at'
    allow_future = True
    month_format = '%m'
    year = str(timezone.now())[0:4]
    month = str(timezone.now())[5:7]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Taken first 4 items
        context['popular_buy'] = BooksForBuy.objects.order_by('current_goal').reverse()[0:4]
        context['popular_free'] = BooksForFree.objects.order_by('views').reverse()[0:4]
        return context


class BooksList(ListView):
    context_object_name = 'books'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class BooksForBuyList(BooksList):
    model = BooksForBuy
    template_name = 'books_for_buy_list.html'
    

class BooksForFreeList(BooksList):
    model = BooksForFree
    template_name = 'books_for_free_list.html'


class BooksListByCategory(ListView):
    context_object_name = 'books'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['category_slug'])
        return context

    def get_queryset(self, Model, **kwargs):
        queryset = super().get_queryset()
        category_id = Category.objects.get(slug=self.kwargs['category_slug']).pk
        queryset = Model.objects.filter(category_id=category_id)
        return queryset


class BooksForBuyListByCategory(BooksListByCategory):
    model = BooksForBuy
    template_name = 'books_for_buy_list_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, **kwargs):
        return super().get_queryset(BooksForBuy)


class BooksForFreeListByCategory(BooksListByCategory):
    model = BooksForFree
    template_name = 'books_for_free_list_by_category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def get_queryset(self, **kwargs):
        return super().get_queryset(BooksForFree)


class BooksForBuyDetailView(DetailView):
    model = BooksForBuy
    template_name = 'books_for_buy_detail.html'
    context_object_name = 'book'


class BooksForFreeDetailView(DetailView):
    model = BooksForFree
    template_name = 'books_for_free_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context