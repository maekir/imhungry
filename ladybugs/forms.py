# -*- coding: cp1251 -*-

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


class UserEditForm(forms.Form):
    username = forms.CharField(max_length=150, required=False, help_text='<br>', label='Логин')
    email = forms.EmailField(max_length=254, required=False, label='E-mail', help_text='<br>')
    first_name = forms.CharField(max_length=30, required=False, label='Имя', help_text='<br>')
    last_name = forms.CharField(max_length=30, required=False, label='Фамилия', help_text='<br>')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'information')


class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(max_length=150, help_text='<br>', label='Старый пароль:', widget=forms.PasswordInput)
    new_password1 = forms.CharField(max_length=150, label='Новый пароль:', help_text='<br>', widget=forms.PasswordInput)
    new_password2 = forms.CharField(max_length=150, label='Подтвердите новый пароль:', help_text='<br>', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')