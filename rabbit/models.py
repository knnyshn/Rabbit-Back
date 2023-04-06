from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Burrow(models.Model):
    name = models.CharField()


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts', null=True)
    burrow = models.ForeignKey(
        Burrow, on_delete=models.CASCADE, related_name='posts', null=True)
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


class TotalCarrots(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='total_carrots', null=True)
