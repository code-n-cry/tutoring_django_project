from django.urls import path

from user.views import SignUpView, LoginView, logout_view, ProfileView, ChangeView

app_name = "user"

urlpatterns = [
    path("signup", SignUpView.as_view(), name="signup"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", logout_view, name="logout"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("change", ChangeView.as_view(), name="change")
]
