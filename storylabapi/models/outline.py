from django.db import models

class Outline(models.Model):
    writer = models.ForeignKey("Writer", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    prose = models.CharField(max_length=1200)
