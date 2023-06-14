from django.db import models
from django.contrib.auth.models import User


class Writer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    penName = models.CharField(max_length=25)
    profilePic = models.URLField(default="https://static.vecteezy.com/system/resources/thumbnails/009/734/564/small/default-avatar-profile-icon-of-social-media-user-vector.jpg")