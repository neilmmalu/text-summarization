from django.contrib import admin
from .models import Text


# Register your models here.
class TextAdmin(admin.ModelAdmin):
    list = ('inputText', 'summarizedText', 'upload', 'completed')


admin.site.register(Text, TextAdmin)
