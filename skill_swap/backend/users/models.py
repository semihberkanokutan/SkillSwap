from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    skills = models.ManyToManyField('Skill')
    bio = models.TextField(null=True, blank=True)
    email = models.EmailField(null=False)
    username = models.CharField(null=False)
    