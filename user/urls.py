from django.urls import path

from user.views import (AboutView, ChangeView, LoginView, ProfileView,
                        SignUpView, logout_view)

app_name = "user"

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("change/<int:pk>", ChangeView.as_view(), name="change"),
    path("detail/<int:pk>", AboutView.as_view(), name="detail"),
]
