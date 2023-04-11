from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    total_carrots = models.IntegerField(default=0)


class Burrow(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name


class Post(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', default='')
    burrow = models.ForeignKey(
        Burrow, on_delete=models.CASCADE, related_name='posts', default='')
    title = models.CharField()
    content = models.TextField()
    carrots = models.IntegerField(default=0)

    @property
    def username(self):
        return User.objects.get(id=self.user_id).username

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    carrots = models.IntegerField(default=0)
