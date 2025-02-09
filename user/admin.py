from django.contrib import admin
from .models import MyUser  # Импортируем вашу модель Article

admin.site.register(MyUser)  # Регистрируем модель в админ-панели

from django.contrib import admin
