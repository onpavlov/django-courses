from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    groups = 2
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput,
        strip=False
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class UserLoginForm(forms.ModelForm):
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username',)