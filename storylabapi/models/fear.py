from django.db import models

class Fear(models.Model):
    fearName = models.CharField(max_length=50)