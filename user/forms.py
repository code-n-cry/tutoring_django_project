from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import MyUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
