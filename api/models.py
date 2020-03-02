from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)



