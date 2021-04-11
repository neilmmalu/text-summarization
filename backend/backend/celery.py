import os
from celery import Celery

from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

app = Celery('textSum',
             broker='redis://' + settings.REDIS_HOST + ':6379',
             backend='redis://' + settings.REDIS_HOST + ':6379')

app.conf.update(
    CELERYBEAT_SCHEDULE={
        'task1': {
            'task': 'textSum.textSum.task1',
            'schedule': crontab(minute=33, hour=2)
        }
    })

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
