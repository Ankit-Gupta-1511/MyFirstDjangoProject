from django import forms
from .models import EndUsers
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        widgets = {
        'password': forms.PasswordInput(),
        'email': forms.EmailInput(),
        }
        fields = ['username','email','password']
