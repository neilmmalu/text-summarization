from django.db import models
from .validators import validate_file_extension

# Create your models here.


class Text(models.Model):
    inputText = models.CharField(max_length=10000000, blank=True)
    summarizedText = models.CharField(max_length=10000000, blank=True)
    upload = models.FileField(blank=True,
                              validators=[validate_file_extension],
                              upload_to="uploads/")
    completed = models.BooleanField(default=False)
