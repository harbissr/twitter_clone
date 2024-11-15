from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(blank=True, upload_to="profile_pic/", null=True)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Tweet(models.Model):
    message = models.TextField(blank=True, null=True, max_length=140)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    timestamp = models.DateTimeField(auto_now_add=True)
    media = models.ImageField(upload_to="tweets_media/", blank=True, null=True)
    retweet = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="retweets",
    )

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}..."
