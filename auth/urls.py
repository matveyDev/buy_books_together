from .views import user_logout
from django.urls import path

urlpatterns = [
    path('logout/', user_logout, name='logout'),
]
