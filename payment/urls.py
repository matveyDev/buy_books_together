from django.urls import path

from .views import PaymentFormView

urlpatterns = [
    path('payment', PaymentFormView.as_view(), name='payment'),
]
