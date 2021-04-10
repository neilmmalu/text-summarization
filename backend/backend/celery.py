import os
from celery import Celery

from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

app.conf.update(CELERY_TASK_SERIALIZER='json',
                CELERY_RESULT_SERIALIZER='json',
                CELERY_TASK_RESULT_EXPIRES=3600,
                CELERY_TIMEZONE='EST',
                CELERYBEAT_SCHEDULE={
                    'task1': {
                        'task': 'textSum.tasks.task1',
                        'schedule': crontab(minute=0, hour=0)
                    }
                })

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
