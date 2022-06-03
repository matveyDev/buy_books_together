from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from contact.models import Contact
from .config import SITE_URL
from books.models import BooksForFree, BooksForBuy, Category


def create_free_book(request):
    title = request.POST['title']
    description = request.POST['description']
    image = request.FILES['image']
    book_file = request.FILES['book_file']
    user = get_user_model().objects.get(pk=request.user.pk)
    category_pk = request.POST['category']
    category = Category.objects.get(pk=category_pk)

    BooksForFree.objects.create(
        title=title, description=description,
        category=category, image=image,
        book_file=book_file, user=user,
    )

def create_buy_book(request):
    title = request.POST['title']
    description = request.POST['description']
    image = request.FILES['image']
    user = get_user_model().objects.get(pk=request.user.pk)
    category_pk = request.POST['category']
    category = Category.objects.get(pk=category_pk)
    book_url = request.POST['book_url']
    finish_goal = request.POST['finish_goal']

    book = BooksForBuy.objects.create(
        title=title, description=description,
        category=category, image=image,
        book_url=book_url,
        finish_goal=finish_goal,
    )
    book.buyers.add(user)

def get_emails():
    emails = []
    queryser_emails = Contact.objects.values_list('email')
    for email in queryser_emails:
        emails += email

    return emails

def send(user, Model):
    emails = get_emails()
    book = Model.objects.first()
    send_mail(
        f'{user} added new book!',
        f'{book.title} - {SITE_URL}{book.get_absolute_url()}',
        'noreplyarenda@gmail.com',
        emails,
        fail_silently=True,
    )

def send_notification_free_book(user):
    send(user, BooksForFree)

def send_notification_buy_book(user):
    send(user, BooksForBuy)