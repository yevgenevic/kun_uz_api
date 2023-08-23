from django.shortcuts import render
from drf_yasg.openapi import Responses
from rest_framework.generics import UpdateAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, SAFE_METHODS, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from apps.models import Post, Category, User
from apps.permissions import IsAuthor, IsSuperUser
from apps.serializzers import PostModelSerializer, ChangePostModelSerializer, CategoryModelSerializer, \
    UserModelSerializer, UserCreateModelSerializer, ChangeUserStatusSerializer


# Create your views here.

class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.select_related('author', 'category').filter(status=True)
    serializer_class = PostModelSerializer
    permission_classes = (IsSuperUser,)
    parser_classes = [MultiPartParser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.method == SAFE_METHODS:
            instance.view += 1
            instance.save()
        serializers = self.get_serializer(instance)
        return Responses(serializers.data)


class ChangePostAPIView(UpdateAPIView):
    serializer_class = ChangePostModelSerializer
    queryset = Post.objects.all()
    permission_classes = (IsSuperUser,)
    http_method_names = ('patch',)


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthor | IsSuperUser)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateModelSerializer
        return super().get_serializer_class()


class ChangeStaffStatusAPIView(CreateAPIView):
    serializer_class = ChangeUserStatusSerializer
    queryset = User.objects.all()
    permission_classes = (IsSuperUser,)


class ProfileRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    http_method_names = ('get', 'patch', 'delete')

    def get_object(self):
        return self.request.user
