from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm


class LoginView(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "user/sign_up_form.html"
    success_url = reverse_lazy("mem:index")
