from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, ImageField, TextField, IntegerField, ForeignKey, CASCADE, DateTimeField, \
    BooleanField, ManyToManyField
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    update_at = DateTimeField(auto_now_add=True)


class Category(Model):
    title = CharField(max_length=100)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Post(Model):
    title = CharField(max_length=100)
    subject = CharField(max_length=255)
    image = ImageField(upload_to='images_post', null=True)
    descriptions = TextField(null=True)
    views = IntegerField(default=0)
    author = ForeignKey('User', CASCADE)
    category = ManyToManyField('apps.Category', related_name='posts')
    add_time = DateTimeField(auto_now_add=True)
    status = BooleanField(default=False)

    class Meta:
        ordering = ['-add_time']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title


@property
def image_url(self):
    try:
        return self.image.url
    except ValueError:
        return "https://storage.kun.uz/source/thumbnails/_medium/9/-s_RNFKgzfyXrRpnqL6puF3vnKf68uF-_medium.jpg"


def __str__(self) -> str:
    return self.title
