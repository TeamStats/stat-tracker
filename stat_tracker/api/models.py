from django.db import models

# Create your models here.

class Activity(models.Model):
    title = models.CharField(max_length=255)
    stat = models.ForeignKey(Stat)


class Stat(models.Model):
    timestamp = models.DateTimeField(null=True)