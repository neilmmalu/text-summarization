# Generated by Django 3.2 on 2021-04-10 15:19

from django.db import migrations, models
import textSum.models
import textSum.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('textSum', '0005_alter_text_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='transactionID',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='text',
            name='upload',
            field=models.FileField(blank=True, upload_to=textSum.models.PathAndRename('uploads/'), validators=[textSum.validators.validate_file_extension]),
        ),
    ]
