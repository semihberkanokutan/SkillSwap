from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(null=False)
    username = models.CharField(max_length=150, unique=True)
    