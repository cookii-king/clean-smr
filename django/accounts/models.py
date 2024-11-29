import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    username = models.CharField(max_length=255, unique=True, null=True, blank=True )
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)