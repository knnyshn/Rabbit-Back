from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from django.contrib.auth import get_user_model
from .models import Burrow, Post, Comment, Profile
from .serializers import UserSerializer, BurrowSerializer, PostSerializer, CommentSerializer, ProfileSerializer
from django.contrib.auth.hashers import make_password


# Create your views here.
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = make_password(self.request.data['password'])
        serializer.save(password=password)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class BurrowViewSet(viewsets.ModelViewSet):

    queryset = Burrow.objects.all()
    serializer_class = BurrowSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)
    hashed_password = make_password(password)
    try:
        user = User.objects.create(username=username, password=hashed_password)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'success': f'User {username} created successfully.'}, status=status.HTTP_201_CREATED)
