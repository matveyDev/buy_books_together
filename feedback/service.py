from django.core.mail import send_mail

def send(email, text, author):
    send_mail(
        f'Обращение от {author}, {email}.',
        text,
        'noreplyarenda@gmail.com',
        ['noreplyarenda@gmail.com',],
        fail_silently=False,
    )