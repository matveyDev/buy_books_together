from django.contrib import admin
from django import forms
from .models import Reviews, Rating

class ReviewsAdminForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = '__all__'

class RatingAdminForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = '__all__'


@admin.register(Reviews)
class BooksForBuyAdmin(admin.ModelAdmin):
    form = ReviewsAdminForm


@admin.register(Rating)
class BooksForBuyAdmin(admin.ModelAdmin):
    form = RatingAdminForm