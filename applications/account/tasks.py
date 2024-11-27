from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_activation_mail(email, activation_code):
    activation_url = f'http://localhost:8000/account/activate/{activation_code}/'
    message = f'''
    Спасибо за регистрацию!
    Активируйте аккаунт!
    Активационная ссылка: {activation_url}
    '''

    send_mail(
        'Activate your account',
        message,
        'test@umanga.kg',
        [email, ],
        fail_silently=False
    )