from django.db import models

class Character(models.Model):
    description = models.CharField(max_length=50)