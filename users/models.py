from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models


# Create your models here.
class CustomUser(AbstractUser, PermissionsMixin):
    mobile = models.CharField(max_length=10)
    place = models.CharField(max_length=50)
