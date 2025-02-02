from operator import index

from django.urls import path, re_path


from user.views import SignUpView, LoginView, logout_view

app_name = "user"

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout")
]
