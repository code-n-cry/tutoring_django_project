from io import BytesIO

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.db import models
from PIL import Image


def resize_image(image_field, max_width=300):
    img = Image.open(image_field)
    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height))
        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        return ContentFile(buffer.getvalue())
    return image_field


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержание", null=False)
    image = models.ImageField(
        upload_to="home_images/",
        null=True,
        blank=True,
        verbose_name="Картинка",
    )
    author = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.image:
            new_image = resize_image(self.image)
            self.image.save(self.image.name, new_image, save=False)
        super().save(*args, **kwargs)

    def get_user_who_liked(self):
        likes_id = []
        for like in self.likes.filter(article=self).all():
            likes_id.append(like.user.id)
        return likes_id

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
