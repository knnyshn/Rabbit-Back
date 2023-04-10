from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    total_carrots = models.IntegerField(default=0)


class Burrow(models.Model):
    name = models.CharField()


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', default='')
    burrow = models.ForeignKey(
        Burrow, on_delete=models.CASCADE, related_name='posts', default='')
    title = models.CharField()
    content = models.TextField()
    carrots = models.IntegerField()


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    carrots = models.IntegerField()
