import json

from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import CrontabSchedule, PeriodicTask

from main.models import SendMessage


@receiver(post_save, sender=SendMessage)
def send_message_via_email(sender, instance, created, **kwargs):
    if created:
        t = instance.send_at
        schedule, created = CrontabSchedule.objects.get_or_create(hour=t.hour, minute=t.minute)
        task = PeriodicTask.objects.create(
            crontab=schedule, name=instance.title, description=instance.body,
            task='main.tasks.send_mail_func',
            kwargs=json.dumps({
                "title": instance.title,
                "message": instance.body
                # "users": instance.emails.all()
            }))
