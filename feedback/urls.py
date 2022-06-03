from django.urls import path
from .views import FeedbackFormView, ReviewsListView, AddReview, DeleteReview

urlpatterns = [
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('reviews/', ReviewsListView.as_view(), name='reviews'),
    path('review/<int:pk>/', AddReview.as_view(), name='add_review'),
    path('review/delete/<int:pk>/', DeleteReview.as_view(), name='delete_review'),
]
