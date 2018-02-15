from django.shortcuts import render
from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from ladybugs.models import Ingredients, Recipes
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
from ladybugs.forms import SignUpForm, UserEditForm
from ladybugs.models import CustomUser


def main_page(request):
    if request.method == 'POST':
        # вывод тех рецептов, которые подходят по продуктам
        ing_ids = request.POST['ingredients']
        recipes = Recipes.objects.filter(ingredients__id__in=ing_ids)
        return render(request, 'main.html',
                      {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all(),
                       'recipes': recipes})
    else:
        return render(request, 'main.html',
                      {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all()})


def register_page(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})


def login_page(request):
    return render(request, 'login.html', {})

def user_page(request):
    username = get_user(request).get_username()
    # проверяем, юзер аноним или нет
    if username != '':
        fullname = get_user(request).get_full_name()
    else:
        fullname = None
    #info = CustomUser.user_info
    return render(request, 'userpage.html', {"username":  username, "fullname": fullname})

def edit_password(request):
    username = get_user(request).get_username()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Ваш пароль успешно изменен!')
            return redirect('/userpage')
        else:
            messages.error(request, 'Исправьте ошибки!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'edit_password.html', {'form': form, 'username': username})

def user_edit_view(request):
    username = get_user(request).get_username()
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            new_username = form.cleaned_data.get('username')
            new_first_name = form.cleaned_data.get('first_name')
            new_last_name = form.cleaned_data.get('last_name')
            new_email = form.cleaned_data.get('email')
            user = User.objects.get(username=request.user.username)
            user.username = new_username
            user.first_name = new_first_name
            user.last_name = new_last_name
            user.email = new_email
            user.save()
            return redirect('/userpage')
        else:
            messages.error(request, 'Исправьте ошибки!')
    else:
        form = UserEditForm()
    return render(request, 'edit_user.html', {'form': form, 'username': username})