from django.utils.safestring import mark_safe
from django.contrib import admin
from django import forms
from .models import BooksForBuy, BooksForFree, Category

class BooksForBuyAdminForm(forms.ModelForm):
    class Meta:
        model = BooksForBuy
        fields = '__all__'

class BooksForFreeAdminForm(forms.ModelForm):
    class Meta:
        model = BooksForFree
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


@admin.register(BooksForBuy)
class BooksForBuyAdmin(admin.ModelAdmin):
    form = BooksForBuyAdminForm

    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return "Нет фото"
    
    get_image.short_description = "Фото"


@admin.register(BooksForFree)
class BooksForBuyAdmin(admin.ModelAdmin):
    form = BooksForFreeAdminForm

    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return "Нет фото"
    
    get_image.short_description = "Фото"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm

    prepopulated_fields = {'slug': ('title',)}