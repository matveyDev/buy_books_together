from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, AddBookForFree, AddBookForBuy

urlpatterns = [
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/update_profile/<int:pk>/', ProfileUpdateView.as_view(), name='update_profile'),
    path('add_free_book', AddBookForFree.as_view(), name='add_free_book'),
    path('add_buy_book', AddBookForBuy.as_view(), name='add_buy_book'),
]
