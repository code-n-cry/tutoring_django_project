from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    FormView,
    TemplateView,
    UpdateView,
)

from user.forms import LoginForm, SignUpForm
from user.models import MyUser


class LoginView(FormView):
    template_name = "user/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy("mem:index")

    def post(self, request, *args, **kwargs):
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user:
            login(request, user)
        return super().post(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "user/sign_up_form.html"
    success_url = reverse_lazy("user:login")


class ProfileView(TemplateView):
    template_name = "user/profile.html"


class AboutView(DetailView):
    template_name = "user/detail.html"
    context_object_name = "user"
    model = MyUser


class ChangeView(LoginRequiredMixin, UpdateView):
    template_name = "user/change.html"
    fields = ["detail", "avatar"]
    model = MyUser
    success_url = "/user/profile"

    def get(self, request, *args, **kwargs):
        if int(self.request.get_full_path().split('/')[-1]) == request.user.pk:
            self.object = request.user
            return super().get(request, *args, **kwargs)
        raise PermissionDenied


def logout_view(request):
    logout(request)
    return redirect('/')
