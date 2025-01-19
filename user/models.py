from django.db import models
from django.contrib.auth import User


class MyUser(User):
    name = models.CharField(verbose_name="Ваше имя(до 50 символов)", name="username", max_length=50)
    email = models.EmailField(verbose_name="Ваша почта", name="email", unique=True)

    def __str__(self):
        return self.name
