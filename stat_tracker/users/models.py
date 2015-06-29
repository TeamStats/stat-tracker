from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    bio = models.TextField()

    def __str__(self):
        return str(self.user)