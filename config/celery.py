from __future__ import absolute_import, unicode_literals  # for python2
import os
from celery import Celery

from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
# this is also used in manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Get the base REDIS URL, default to redis' default
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'main.tasks.add',
        'schedule': crontab(hour=17, minute=31, day_of_week=1),
        'args': (16, 16)
    },
}
