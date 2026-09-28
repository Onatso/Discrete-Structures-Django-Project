from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import User, Achievement



@shared_task(bind=True, max_retries=3)
def send_achievement_email(self, user_id, achievement_id):
    #self - сама задача
    user = User.objects.get(id=user_id)
    achievement = Achievement.objects.get(id=achievement_id)

    subject = f'Вы получили достижение "{achievement.name}"'
    # HTML-версия письма
    html_content = render_to_string(
        'get_achievement.html',
        {
            'user': user,
            'achievement': achievement
        }
    )

    # Текстовая версия
    text_content = ''

    email = EmailMultiAlternatives(
        subject=subject,
        body='Поздравляем с новым достижением!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

