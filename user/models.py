from django.db import models
from django.contrib.auth.models import AbstractUser
from django.templatetags.static import static

# from sorl.thumbnail import  get_thumbnail
import time


def avatar_image_path(instance, filename):
    return f'uploads/{instance.id}-{time.strftime("%Y%m%d-%H%M%S")}/{filename}'


class MyUser(AbstractUser):
    avatar = models.ImageField(
        upload_to=avatar_image_path,
        null=True,
        blank=True,
        verbose_name="Аватарка",
    )
    detail = models.TextField(
        null=True,
        max_length=550,
        verbose_name='детали',
        help_text='расскажите о себе детальнее',
    )

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        default_related_name = 'user'

    def __str__(self):
        return self.username

    '''def get_avatar_300x300(self):
        if self.avatar:
            return get_thumbnail(
                self.avatar, '300x300', crop='center', quality=65
            )
        return {'url': static('img/avatar_default.jpg')}'''
