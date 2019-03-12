from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)
    year = models.IntegerField()

