from django.db import models

class Obstacle(models.Model):
    obstruction = models.CharField(max_length=50)