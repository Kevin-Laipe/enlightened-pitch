from django.db import models

class Set(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=5)