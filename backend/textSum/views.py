from django.shortcuts import render
from .serializers import TextSerializer
from rest_framework import viewsets
from .models import Text


# Create your views here.
class TextView(viewsets.ModelViewSet):
    lookup_field = 'transactionID'
    serializer_class = TextSerializer
    queryset = Text.objects.all()
