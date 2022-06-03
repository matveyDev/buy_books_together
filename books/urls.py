from django.urls import path
from .views import HomePage, BooksForBuyList, BooksForBuyListByCategory,\
    BooksForFreeList, BooksForFreeListByCategory, BooksForBuyDetailView,\
    BooksForFreeDetailView

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('books_for_buy/', BooksForBuyList.as_view(), name='books_for_buy_list'),
    path('books_for_buy/<slug:category_slug>/', BooksForBuyListByCategory.as_view(), name='books_for_buy_list_by_category'),
    path('books_for_buy/<slug:category_slug>/<slug:slug>/', BooksForBuyDetailView.as_view(), name='books_for_buy_detail'),

    path('books_for_free/', BooksForFreeList.as_view(), name='books_for_free_list'),
    path('books_for_free/<slug:category_slug>/', BooksForFreeListByCategory.as_view(), name='books_for_free_list_by_category'),
    path('books_for_free/<slug:category_slug>/<slug:slug>/', BooksForFreeDetailView.as_view(), name='books_for_free_detail'),
]