from django.contrib.auth.hashers import make_password
from rest_framework.exceptions import ValidationError

from .models import User
from rest_framework.fields import HiddenField, CurrentUserDefault, BooleanField, CharField
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from apps.models import Category, Post


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostModelSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Post
        fields = "id", "image", "title_uz", "title_en", "title_ru", "subject_uz", "subject_en", "subject_ru", "descriptions_uz", "descriptions_en", "descriptions_ru", "views", "category", "status", "add_time", "author"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['author'] = UserModelSerializer(instance.author).data
        data['category'] = CategoryModelSerializer(instance.category).data
        return data


2


class ChangePostModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('status',)


class UserCreateModelSerializer(ModelSerializer):
    confirm_password = CharField(max_length=255, write_only=True)

    class Meta:
        model = User
        fields = 'username', 'password', 'confirm_password'

    def create(self, validated_data):
        password = validated_data['password']
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise ValidationError('Invalid password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)

    def to_representation(self, instance):
        return UserModelSerializer(instance).data


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = 'user_permissions', 'groups', 'password', 'update_at'


class ChangeUserStatusSerializer(Serializer):
    is_staff = BooleanField(default=False)
    user = PrimaryKeyRelatedField(queryset=User.objects.all())

    def create(self, validated_data):
        user = validated_data['user']
        user.is_staff = validated_data['is_staff']
        user.save()
        return validated_data
