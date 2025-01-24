from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm, LoginForm


class LoginView(FormView):
    template_name = "user/login_form.html"
    form_class = LoginForm
    success_url = reverse_lazy("mem:index")


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "user/sign_up_form.html"
    success_url = reverse_lazy("user:login")
