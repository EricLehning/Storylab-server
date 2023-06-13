from django.db import models

class Desire(models.Model):
    wish = models.CharField(max_length=50)