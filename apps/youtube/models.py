from django.db import models

# Create your models here.

class Usage(models.Model):
    size = models.FloatField()
    link = models.CharField(max_length=1000)
