from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Burrow, Post, Comment, TotalCarrots
from .serializers import UserSerializer, BurrowSerializer, PostSerializer, CommentSerializer, TotalCarrotsSerializer

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BurrowViewSet(viewsets.ModelViewSet):
    queryset = Burrow.objects.all()
    serializer_class = BurrowSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TotalCarrotsViewSet(viewsets.ModelViewSet):
    queryset = TotalCarrots.objects.all()
    serializer_class = TotalCarrotsSerializer
