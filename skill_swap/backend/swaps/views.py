from django.shortcuts import render
from .models import Swap
from .serializers import SwapSerializer
from rest_framework import viewsets

# Create your views here.

class SwapViewSet(viewsets.ModelViewSet):
    queryset = Swap.objects.all()
    serializer_class = SwapSerializer
