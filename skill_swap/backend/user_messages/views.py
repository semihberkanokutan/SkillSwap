from django.shortcuts import render
from .models import UserMessage
from .serializers import UserMessageSerializer
from rest_framework import viewsets

# Create your views here.

class UserMessageViewSet(viewsets.ModelViewSet):
    queryset = UserMessage.objects.all()
    serializer_class = UserMessageSerializer
