from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Burrow, Post, Comment, Profile
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'total_carrots']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class BurrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burrow
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user.all(), many=True).data
        response['post'] = PostSerializer(instance.user.all(), many=True).data

        return response


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(read_only=True, many=True)
    burrow = BurrowSerializer(read_only=True, many=True)
    user = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializer(instance.user.all(), many=True)
        response['burrow'] = BurrowSerializer(instance.burrow.all(), many=True)

        return response
