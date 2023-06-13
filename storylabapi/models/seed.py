from django.db import models
from django.contrib.auth.models import User

class Seed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    desire = models.ForeignKey("Desire", on_delete=models.CASCADE)
    fear = models.ForeignKey("Fear", on_delete=models.CASCADE)
    obstacles = models.ManyToManyField("Obstacle", related_name="seed_obstacles")
    consequence = models.ForeignKey("Consequence", on_delete=models.CASCADE)
    reward = models.ForeignKey("Reward", on_delete=models.CASCADE)