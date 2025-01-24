from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from user.models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ("username", "email")
        labels = {
            "username": "Юзернейм",
            "email": "E-mail",
            MyUser.password.field.name: "Парооль",
        }
        help_texts = {
            "email": "Обязательное поле"
        }


class LoginForm(AuthenticationForm):
    pass
