from django.db import models

class Sets(models.Model):
    name = models.Charfield(max_length=50)
    tag = models.Charfield(max_length=5)