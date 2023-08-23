from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name="category", lookup_expr="exact")

    class Meta:
        model = Post
        fields = "category",


class PostSearchFilter(filters.FilterSet):
    title_uz = filters.CharFilter(field_name="title_uz", lookup_expr="icontains", )
    title_en = filters.CharFilter(field_name="title_en", lookup_expr="icontains", )
    title_ru = filters.CharFilter(field_name="title_ru", lookup_expr="icontains", )

    class Meta:
        model = Post
        fields = "title_uz", "title_en", "title_ru"
