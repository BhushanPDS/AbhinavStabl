import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('ehr-bridge')


app.config_from_object(settings, namespace='CELERY')

# Celery beat setting
app.conf.beat_schedule = {
    'refresh-token': {
        'task': 'endpoint.tasks.refresh_token',
        'schedule': crontab(minute='*/9')
    },
    "epic-system": {
        "task": "core.tasks.refresh_epic_backend_system_token",
        "schedule": crontab(minute="*/1"),
    }
}

app.autodiscover_tasks()
