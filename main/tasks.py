from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from main.models import SendMessage


@shared_task
def add(a, b):
    return a + b


@shared_task
def send_mail_func(title, message):
    users = SendMessage.objects.get(title=title, body=message).emails.all()

    for user in users:
        to_email = user.email

        html_content = render_to_string('send_message.html', {
            'title': title,
            'message': message
        })  # render with dynamic value

        text_content = strip_tags(html_content)  # Strip the html tag. So people can see the pure text at least.

        # create the email, and attach the HTML version as well.
        msg = EmailMultiAlternatives(
            subject=title,
            body=text_content,
            from_email=settings.EMAIL_HOST_USER,
            to=[to_email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
    return "Done"

# @shared_task
# def send_mail_func(title, message):
#     users = SendMessage.objects.get(title=title, body=message).emails.all()
#
#     for user in users:
#         mail_subject = title
#         message = message
#         to_email = user.email
#         send_mail(
#             subject=mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=True,
#         )
#     return "Done"
# celery -A config worker -l INFO --pool=solo
# celery -A config beat -l info
