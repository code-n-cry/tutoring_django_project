from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UserChangeForm,
)
from user.models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "email", "avatar")
        labels = {
            "username": "Юзернейм",
            "email": "E-mail",
            "avatar": "Аватар",
            MyUser.password.field.name: "Пароль",
        }
        help_texts = {
            "avatar": "Картинка вашего профиля",
            "email": "Обязательное поле",
        }


class LoginForm(AuthenticationForm):
    pass
