from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField()


class Burrow(models.Model):
    name = models.CharField()
    total_carrots = models.IntegerField()


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
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
