from django.contrib.auth import login, authenticate, get_user
from django.contrib.auth.forms import UserCreationForm #, PasswordChangeForm
from django.shortcuts import render, redirect
from ladybugs.models import Ingredients, Recipes
from django.contrib.auth.models import User, UserManager
from django.db import models
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
from ladybugs.forms import SignUpForm, UserEditForm, PasswordChangeForm
from ladybugs.models import CustomUser


def main_page(request):
    random_recipes = Recipes.objects.order_by('?')
    random_recipes = random_recipes[:2]
    print(random_recipes)
    if request.method == 'POST':
        which_act = request.GET["act"]
        if which_act == "1":
            post = dict(request.POST)
            try:
                ing_ids = [int(i) for i in post['ingredients']]
            except KeyError:
                return redirect('/')
            recipes = Recipes.objects.exclude(ingredients__id__in=Ingredients.objects.exclude(id__in=ing_ids).values_list('id',flat=True))

            try:
                comp = [int(i) for i in post['comp']]
                recipes = recipes.filter(complexity__in=comp)
            except:
                pass

            try:
                meal = [int(i) for i in post['meal']]
                recipes = recipes.filter(meal_time__in=meal)
            except:
                pass

            try:
                speed = [int(i) for i in post['speed']]
                recipes = recipes.filter(speed__in=speed)
            except:
                pass

            return render(request, 'main.html',
                          {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all(),
                           'recipes': recipes, 'random_recipes': random_recipes})
        elif which_act == "2":
            search = request.POST['recipe_title_search'].capitalize()
            recipes = Recipes.objects.filter(title__icontains=search)
            return render(request, 'main.html',
                          {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all(),
                           'recipes': recipes, 'random_recipes': random_recipes})
        else:
            return render(request, 'main.html',
                          {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all(),
                           'random_recipes': random_recipes})
    else:
        return render(request, 'main.html',
                          {"name": get_user(request).get_username(), 'ingredients': Ingredients.objects.all(),
                           'random_recipes': random_recipes})


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
    return render(request, 'userpage.html', {"username":  username, "fullname": fullname})


def edit_password(request):
    username = get_user(request).get_username()
    user = get_user(request)
    if request.method == 'POST':
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            if user.check_password(form.cleaned_data.get('old_password')):
                user = User.objects.get(username=username)
                newpass=form.cleaned_data.get('new_password1')
                user.set_password(newpass)
                user.save()
                user = authenticate(username=username, password=newpass)
                login(request, user)
                messages.success(request, 'Ваш пароль успешно изменен!')
                return redirect('/userpage')
            else:
                messages.error(request, 'Исправьте ошибки!')
        else:
            messages.error(request, 'Исправьте ошибки!')
    else:
        form = PasswordChangeForm()
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