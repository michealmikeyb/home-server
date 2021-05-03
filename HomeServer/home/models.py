from django.db import models

# Create your models here.
class Poll(models.Model):
    name = models.CharField(max_length=64)
    total = models.IntegerField(default=0)