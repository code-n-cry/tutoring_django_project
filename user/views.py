from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm

class LoginView(TemplateView):
    pass


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "sign_up_form.html"
    success_url = reverse_lazy("")
