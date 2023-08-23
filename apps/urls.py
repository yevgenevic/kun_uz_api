from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import PostModelViewSet, UserModelViewSet, ProfileRetrieveUpdateDestroyAPIView, CategoryModelViewSet, \
    ChangePostAPIView, ChangeStaffStatusAPIView

router = DefaultRouter()
router.register('posts', PostModelViewSet, basename='posts')
router.register('category', CategoryModelViewSet, basename='category')
router.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/status', ChangePostAPIView.as_view(), name='post-change'),
    path('auth/profile/', ProfileRetrieveUpdateDestroyAPIView.as_view(), name='profile'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user-position', ChangeStaffStatusAPIView.as_view(), name='user-position'),
]
