from ..celery import app
from .models import Text
import os


@app.task
def task1():
    texts = Text.objects.all()

    for text in texts:
        if text.completed:
            f = str(text.upload)
            if os.path.exists(f):
                os.remove(f)
            text.delete()
