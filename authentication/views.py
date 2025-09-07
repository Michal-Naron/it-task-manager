from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from workflows.models import Worker
from .forms import LoginForm, SignUpForm

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = "Invalid credentials"
        else:
            msg = "Error validating the form"

    return render(request,"accounts/login.html", {"form": form, "msg": msg})


class RegisterView(generic.CreateView):
    model = Worker
    form_class = SignUpForm
    success_url = reverse_lazy("authentication:login")
    template_name = "accounts/register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            if not SignUpForm(self.request.POST).is_valid():
                context["msg"] = "Form is not valid"
            else:
                context["msg"] = 'User created - please <a href="/login">login</a>.'

        return context
