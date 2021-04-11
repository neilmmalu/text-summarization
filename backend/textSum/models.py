from django.db import models
from .validators import validate_file_extension
from django_lifecycle import LifecycleModelMixin, hook, AFTER_CREATE
import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible


@deconstructible
class PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(self.path, filename)


path_and_rename = PathAndRename("uploads/")

# Create your models here.


class Text(LifecycleModelMixin, models.Model):
    inputText = models.CharField(max_length=10000000, blank=True)
    summarizedText = models.CharField(max_length=10000000, blank=True)
    upload = models.FileField(blank=True,
                              validators=[validate_file_extension],
                              upload_to=path_and_rename)
    completed = models.BooleanField(default=False)
    transactionID = models.CharField(max_length=100,
                                     blank=True,
                                     unique=True,
                                     default=uuid4)

    @hook(AFTER_CREATE)
    def summarizeText(self):
        txt = ""

        if self.inputText:
            txt = self.inputText
        else:
            #read file
            f = open(str(self.upload))

            txt = f.read()

        sumStr = "Dummy summarized text"
        # sumStr = summarize(txt)

        t = Text.objects.get(transactionID=self.transactionID)
        t.summarizedText = sumStr
        t.completed = True
        t.save()
