from django.core.mail import send_mail

def send(email):
    send_mail(
        'Вы подписались на рассылку!',
        'Мы будем присылать вам уведомления о новинках!',
        'noreplyarenda@gmail.com',
        [email,],
        fail_silently=False,
    )