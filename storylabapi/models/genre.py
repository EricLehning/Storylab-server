from django.db import models

class Genre(models.Model):
    category = models.CharField(max_length=50)