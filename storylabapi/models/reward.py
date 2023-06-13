from django.db import models

class Reward(models.Model):
    prize = models.CharField(max_length=50)