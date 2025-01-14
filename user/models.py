from django.db import models


class User(models.Model):
    name = models.CharField(verbose_name="Ваше имя(до 50 символов)", name="username", max_length=50)
    email = models.EmailField(verbose_name="Ваша почта", name="email", unique=True)
    password = models.CharField(verbose_name="Ваш пароль", max_length=100)
    
