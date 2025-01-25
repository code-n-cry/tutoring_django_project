from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login


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
