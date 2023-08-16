from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254, required=True,
                               help_text='نام کاربری را وارد کنید')
    password1 = forms.CharField(max_length=254, required=True,
                                help_text='رمز عبور را وارد کنید')
    password2 = forms.CharField(max_length=254, required=True,
                                help_text='رمز عبور را مجددا وارد کنید')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
