from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Burrow, Post, Comment, TotalCarrots


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class BurrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burrow
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    def get_user(self, obj):
        return obj.id

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['user', 'post', 'content', 'carrots']


class TotalCarrotsSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TotalCarrots
        fields = '__all__'
