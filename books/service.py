from django.core.mail import send_mail

def send(emails, book_title):
    send_mail(
        'Goal was completed!',
        f'{book_title} goal was ended! In near future you will get a book!',
        'noreplyarenda@gmail.com',
        emails,
        fail_silently=True
    )

def send_all_emails(emails):
    send_mail(
        'All emails',
        f'{emails}',
        'noreplyarenda@gmail.com',
        'noreplyarenda@gmail.com',
        fail_silently=False
    )