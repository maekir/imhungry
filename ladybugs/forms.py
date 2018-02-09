from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=150, help_text='', label='Логин')
    first_name = forms.CharField(max_length=30, required=False, label='Имя')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия')
    email = forms.EmailField(max_length=254, label='E-mail')
    password2 = forms.CharField(label=("Подтвердите пароль"), widget=forms.PasswordInput, strip=False, help_text=(""))
    password1 = forms.CharField(label=("Пароль"), widget=forms.PasswordInput, strip=False, help_text=(
    "<br>Ваш пароль не должен быть похожим на ваши персональные данные, должен содержать минимум 8 символов и не может состоять только из чисел."))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
