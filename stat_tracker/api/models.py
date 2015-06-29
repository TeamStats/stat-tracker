from django.db import models
from users.models import Profile

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(Profile, null=True)

class Stat(models.Model):
    timestamp = models.DateField(null=True)
    stat = models.IntegerField()
    activity = models.ForeignKey(Activity)

    class Meta:
        unique_together = ('timestamp', 'activity')
