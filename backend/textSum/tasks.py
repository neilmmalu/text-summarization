from root.celery import app
from .models import Text


@app.task
def task1():
    texts = Text.objects.all()

    for text in texts:
        if text.completed:
            text.delete()