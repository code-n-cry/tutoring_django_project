from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm, LoginForm, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


class LoginView(FormView):
    template_name = "user/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy("mem:index")

    def post(self, request, *args, **kwargs):
        user = authenticate(request, username=request.POST["username"],
                            password=request.POST["password"])
        if user:
            login(request, user)
        return super().post(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "user/sign_up_form.html"
    success_url = reverse_lazy("user:login")


class ProfileView(TemplateView):
    template_name = "user/profile.html"


class ChangeView(FormView):
    template_name = "user/change.html"
    form_class = None


def logout_view(request):
    logout(request)
    return redirect('/')
