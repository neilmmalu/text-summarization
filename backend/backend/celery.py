from django.conf import settings
from celery import Celery
from celery.schedules import crontab

redis_host = settings.REDIS_HOST

app = Celery('project',
             broker='redis://' + settings.REDIS_HOST + ':6379',
             backend='redis://’ + settings.REDIS_HOST + ‘:6379',
             include=['textSum.tasks'])

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

if __name__ == "__main__":
    app.start()
