from django import forms
from django.contrib.auth.forms import UserCreationForm

from workflows.models import Worker, Position


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control form-control-lg"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class": "form-control form-control-lg"
            }
        ))


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "username",
                "class": "form-control form-control-lg"
            }
        )
    )
    position = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        empty_label="Select a position",
        widget = forms.Select(attrs={"class": "form-control form-control-lg"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "email",
                "class": "form-control form-control-lg"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control form-control-lg"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Repead password",
                "class": "form-control form-control-lg"
            }
        )
    )


    class Meta:
        model = Worker
        fields = ("username", "position" ,"email", "password1", "password2")
