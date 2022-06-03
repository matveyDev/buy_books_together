from django.urls import path
from .views import SearchForm

urlpatterns = [
    path('search/', SearchForm.as_view(), name='search'),
]
