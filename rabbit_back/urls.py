
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from rest_framework import routers
from rabbit.views import PostViewSet, UserViewSet, BurrowViewSet, CommentViewSet, ProfileViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')
router.register(r'burrows', BurrowViewSet, basename='burrow')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'profiles', ProfileViewSet, basename='profile')

urlpatterns = [

    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api-auth/', include('rest_framework.urls')),

]
