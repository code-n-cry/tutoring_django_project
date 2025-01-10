from django.db import models
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


def resize_image(image_field, max_width=800):
    img = Image.open(image_field)
    if img.width > max_width:
        ratio = max_width / img.width
        new_height = int(img.height * ratio)
        img = img.resize((max_width, new_height))

        buffer = BytesIO()
        img.save(buffer, format="JPEG")
        return ContentFile(buffer.getvalue())
    return image_field


class MyModel(models.Model):
    image = models.ImageField(upload_to="images/")

    def save(self, *args, **kwargs):
        if self.image:
            new_image = resize_image(self.image)
            self.image.save(self.image.name, new_image, save=False)
        super().save(*args, **kwargs)


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="home_images/", null=True, blank=True)

    def __str__(self):
        return self.title
