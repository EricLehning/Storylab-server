from django.db import models

class Consequence(models.Model):
    negResult = models.CharField(max_length=50)